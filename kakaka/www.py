import argparse
from flask import Flask,request, render_template
import commands
import sqlite3
import datetime

app =Flask(__name__)
parser = argparse.ArgumentParser(description='db')
parser.add_argument('--port', dest='port',default=1234,type=int,help='www port''mlr')
parser.add_argument('--db_file', dest='db_file', default="db_file.db", help='dbfile')
parser.add_argument('--db_table_devices', dest='db_table_devices',default="db_table",help='db_table')
parser.add_argument('--db_element_devices', dest='db_element_devices',default="id,Chip,Vendor,Part_number,Note,Interface,Type,Ranks,RCD_Vendor,Capacity,speed,Count,Stock,Fail,Owner,Remark,Share",help='dbname')


args = parser.parse_args()

def now():
    return str(datetime.datetime.today().strftime('%y%m%d_%H%M%S'))

def exec_cmd(e,retry = 3):
    for i in range(0,retry):
        re = commands.getstatusoutput(e)
        if re[0] != 0:
            print re[1]
        else:
            return re
    return -1,"exec_cmd %s retry" %(e,retry)

def db_devices():
    return [args.db_file,args.db_table_devices,args.db_element_devices]

def db_element(db):
    return db[2].split(",")

def open_file(filename):
    try:
        f = open(filename, "r")
        text = f.read()
        f.close()
        return text;
    except:
        return ""

def is_admin(key):
    cfg = open_file("admin.cfg")
    for e in cfg.split(","):
        if e == key:
            return True
    return False

def backup_db(db_file,dir="backup/"):
    exec_cmd("mkdir -p %s" %(dir))
    exec_cmd("cp -rf %s %s/%s-%s" %(db_file,dir,db_file,now()))

def db_unpark(db):
    return db[0],db[1],db[2]

def sql_db(db,value=None,id=None,get_max_id=None,rm_by_id=False):
    db_file, db_table,db_element = db_unpark(db)
    db_element_table = ""
    db_element_v = ""
    for e in db_element.split(","):
        if e.find("id") != -1:
            db_element_table = db_element_table + e + " int,"
        else:
            db_element_table = db_element_table + e + " text,"
        db_element_v = db_element_v + "?,"
    db_element_table = db_element_table[0:len(db_element_table) -1 ]
    db_element_v = db_element_v[0:len(db_element_v) -1 ]
    if rm_by_id == True or value != None:
        backup_db(db_file)
    con = sqlite3.connect(db_file)
    db = con.cursor()
    db.execute('''CREATE TABLE IF NOT EXISTS %s(%s)''' %(db_table,db_element_table))
    con.commit()
    if rm_by_id:
        db.execute('''DELETE FROM %s WHERE id=%s''' % (db_table,id))
        con.commit()
        con.close()
        return 0
    if get_max_id != None:
        db.execute('''SELECT MAX(%s) FROM %s''' %(get_max_id,db_table))
        data = db.fetchall()
        try:
            if data[0][0] == None:
                data = 0
            data = int(data[0][0])
        except:
            data = None
        con.close()
        return data
    if value == None:
        if id != None:
            db.execute('''SELECT * FROM %s WHERE id=%s''' %(db_table,id))
            data = db.fetchall()
            try:
                data = [e for e in data[0]]
            except:
                data = None
            con.close()
            return data
        else:
            db.execute('''SELECT * FROM %s ORDER BY id ''' %(db_table))
            data = db.fetchall()
            con.close()
            return data
    else:
        if id != None:
            db.execute('''DELETE FROM %s WHERE id=%s''' % (db_table,id))
        db.execute('''INSERT INTO %s VALUES(%s)'''%(db_table,db_element_v),value)
        con.commit()
        con.close()

def get_db_index(element,db):
    db_file, db_table,db_element = db_unpark(db)
    index = -1
    for e in db_element.split(","):
        index = index + 1
        if e == element:
            return index
    return -1

def str2int(str):
    try:
        return int(str)
    except:
        return 0

def format_devices_main(e,db):
    Index=e[get_db_index("id",db)]
    Count=e[get_db_index("Count",db)]
    Stock=e[get_db_index("Stock",db)]
    Fail=e[get_db_index("Fail",db)]
    Share=e[get_db_index("Share",db)]
    Part_number=e[get_db_index("Part_number",db)]
    Other =""
    key = ["id","Count","Stock","Fail","Share"]
    for ee in db_element(db):
        if (ee in key) == True:
            continue
        Other = "%s%s:%s\n" %(Other,ee,e[get_db_index(ee,db)])
    if str2int(Count) != (str2int(Stock) + str2int(Fail) + str2int(Share)):
        Other = "%s!!!ERROR: total count is INVALID!!!\n" %(Other)
    return [Index,Count,Stock,Fail,Share,Part_number,Other]

def get_devices_main(db,id=None,filter=""):
    devices = []
    data = sql_db(db,id=id)
    if id != None:
        if data == None:
            return data
        return format_devices_main(data,db)
    for e in data:
        value = format_devices_main(e,db)
        append = True
        if filter != "":
            for s in filter.split(","):
                if value[6].find(s) == -1:
                    append = False
                    break
        if append:
            devices.append(value)
    return devices

@app.route("/", methods=['POST', 'GET'])
def hello():
    global args
    filter = ""
    for e in request.form:
        if e == "filter" and request.form[e] !="":
            filter = request.form[e]

    msg="Welcome %s to home filter = %s admin=%s" %(request.remote_addr,filter,is_admin(request.remote_addr))
    devices=get_devices_main(db_devices(),filter=filter)
    return render_template('home.html',devices=devices,msg=msg,filter=filter)

if __name__=="__main__":
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host= '0.0.0.0', port=args.port)

