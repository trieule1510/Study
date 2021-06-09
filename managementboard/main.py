import sqlite3
import argparse
import commands
import datetime
import socket
from flask import Flask,request,render_template
from collections import OrderedDict
from flask_login import LoginManager, login_user, current_user


app = Flask(__name__)
app.secret_key = '^.6'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
parser = argparse.ArgumentParser(description='db')

parser.add_argument('--port', dest='port',default=1234,type=int,help='www port''mlr')
parser.add_argument('--db_group', dest='db_group',default="",help='devices')
parser.add_argument('--backup_db', dest='backup_db',default=1,type=int,help='backup_db')


parser.add_argument('--db_platform', dest='db_platform',default="db_platform.db",help='db_platform')
parser.add_argument('--db_table_platform', dest='db_table_platform',default="db_table_platform3",help='db_table_platform')
parser.add_argument('--db_element_platform', dest='db_element_platform',default="id,Team,Name,Location,Serial_Number,Chassis_SN,HW_label,System_Type,Board_Rev,Occupation,Cielo,Board_Status,email,Task,CPU,VRD,CPLD_Main,CPLD_Backplane,bmcip,hostip,hostuser,hostpass,hostport,tty_bmc,tty_uefi,tty_atf,tty_s0cli,tty_s1cli,Note,client_info,time",help='db_element_platform')

parser.add_argument('--db_platform_devices', dest='db_platform_devices',default="db_platform_devices.db",help='db_platform_devices')
parser.add_argument('--db_table_platform_devices', dest='db_table_platform_devices',default="db_table_platform_devices",help='db_table_platform')
parser.add_argument('--db_element_platform_devices', dest='db_element_platform_devices',default="device_id,platform_id",help='db_element_platform_devices')

args = parser.parse_args()

def db_shared():
    return [args.db_file,args.db_table_shared,args.db_element_request]
def db_element(db):
    return db[2].split(",")
def db_platform():
    return [args.db_platform,args.db_table_platform,args.db_element_platform]
def db_platform_info(id):
    table = "platform_info_%s" %(id)
    return ["db_platform_info.db",table,"id,ddr_info,pci_info,cpu_info,time"]
def db_platform_devices():
    return [args.db_platform_devices,args.db_table_platform_devices,args.db_element_platform_devices]

def exec_cmd(e):
    if e.find("mkdir") != 0:
        print e
    re = commands.getstatusoutput(e)
    return re

def now():
    return str(datetime.datetime.today().strftime('%y%m%d_%H%M%S'))

def backup_db(db_file,dir="backup/"):
    if args.backup_db != 0:
        exec_cmd("mkdir -p %s" %(dir))
        exec_cmd("cp -rf %s %s/%s-%s" %(db_file,dir,db_file,now()))

def db_unpark(db):
    return db[0],db[1],db[2]

def get_db_index(element,db):
    db_file, db_table,db_element = db_unpark(db)
    index = -1
    for e in db_element.split(","):
        index = index + 1
        if e == element:
            return index
    return -1

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def href(name,pwd):
    if args.web_ip =="":
        args.web_ip = get_ip()
    return "<a href='http://%s:%s%s'> %s </a>" %(args.web_ip,str(args.port),pwd,name)

def platform_map_info(_id):
    re = ""
    platform_infos = sql_db(db_platform_info(_id),where="limit 1")
    if len(platform_infos) != 0:
        platform_info = platform_infos[0]
        for i in range(1,4):
            re ="%s %s\n" %(re,platform_info[i])
    return re.replace("<br>", "\n").replace("\n\n", "\n")

def platform_map_device(_id):
    re = "<br>"
    platform_devices = sql_db(db_platform_devices(),where="WHERE platform_id='%s'" %(_id))
    i = 1
    if len(platform_devices) != 0 or platform_devices != None:
        for platform_device in platform_devices:
            devices_shared = sql_db(db_shared(),id=platform_device[0])
            for device_shared in devices_shared:
                number = device_shared[get_db_index("number",db_shared())]
                part_number = device_shared[get_db_index("Part_number",db_shared())]
                email = device_shared[get_db_index("email",db_shared())]
                re = "%s %s - %s<br>" %(re,i,href("x%s %s %s" %(number,part_number,email),"/page_shared_submit/%s" %(platform_device[0])))
                i = i + 1
    return re.replace("<br>", "\n").replace("\n\n", "\n")

def sql_db(db,value=None,id=None,select_max=None,rm=False,where=None):
    db_file, db_table,db_element = db_unpark(db)
    if args.db_group != "":
        db_file = "%s_%s" %(args.db_group,db_file)
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
    if rm == True or value != None:
        backup_db(db_file)
    con = sqlite3.connect(db_file)
    db = con.cursor()
    db.execute('''CREATE TABLE IF NOT EXISTS %s(%s)''' %(db_table,db_element_table))
    con.commit()
    if rm:
        try:
            if where != None:
                db.execute('''DELETE FROM %s %s''' % (db_table,where))
            if id != None:
                db.execute('''DELETE FROM %s WHERE id=%s''' % (db_table,id))
            con.commit()
        except:
            pass
        con.close()
        return 0
    if select_max != None:
        try:
            db.execute('''SELECT MAX(%s) FROM %s''' %(select_max,db_table))
            data = db.fetchall()
            if data[0][0] == None:
                data = 0
            data = int(data[0][0])
        except:
            data = None
        con.close()
        return data
    if value == None:
        if id != None:
            try:
                db.execute('''SELECT * FROM %s WHERE id=%s''' %(db_table,id))
                data = db.fetchall()
                data = data
            except:
                data = None
            con.close()
            return data
        else:
            try:
                if where != None:
                    db.execute('''SELECT * FROM %s %s''' %(db_table,where))
                else:
                    db.execute('''SELECT * FROM %s ORDER BY id ''' %(db_table))
                data = db.fetchall()
            except:
                data = None
            con.close()
            return data
    else:
        try:
            if id != None:
                db.execute('''DELETE FROM %s WHERE id=%s''' % (db_table,id))
            if where != None:
                db.execute('''DELETE FROM %s %s''' % (db_table,where))
            db.execute('''INSERT INTO %s VALUES(%s)'''%(db_table,db_element_v),value)
            con.commit()
        except:
            pass
        con.close()

def to_dict(db,device):
    if device == None:
        return None
    re = OrderedDict()
    element = db_element(db)
    for i in range(0,len(element)):
        try:
            re[element[i]] = device[i].replace("@amperecomputing.com","")
        except:
            re[element[i]] = device[i]
    return re
def to_dicts(db,devices):
    re = []
    for device in devices:
        re.append(to_dict(db,device))
    return re

def get_search(request):
    f = ""
    if request.args.get("search")!=None:
        f = request.args.get("search")
    for e in request.form:
        if e == "search" and request.form[e] !="":
            f = request.form[e]
    return f

def get_devices(db,id=None,search="",is_map=False):
    devices = sql_db(db,id=id)
    if id == None:
        devices =  device_search(db,devices,search,is_map)
    else:
        if devices == None or len(devices) == 0:
            return None
        return devices[0]
    return devices

def device_search(db,devices,search="",is_map=False):
    _devices = []
    element = db_element(db)
    for device in devices:
        if is_map:
            device = [e for e in device]
        append = True
        msg = ""
        for i in range(0,len(element)):
            if is_map and element[i] == "Note" and db[0] == db_platform()[0]:
                device[i] = "%s %s" %(device[i],platform_map_info(device[0]))
                device[i] = "%s %s" %(device[i],platform_map_device(device[0]))
            msg = "%s %s:%s" %(msg,element[i],device[i])
        for f in search.split(","):
            if msg.lower().find(f.lower()) == -1:
                append = False
                break
        if append:
            _devices.append(device)
    return _devices

def get_titles(link):
    titles=[]
    for title in link.split("/"):
        name = title
        div_class = "m1"
        try:
            e = title.split(":")
            if len(e) == 2:
                name = e[0]
                div_class = "m%s" %(e[1])
        except:
            pass
        titles.append({"name":name,"class":div_class})
    return titles

def welcome(msg,request,search,devices=""):
    msg="[%s %s] user=[%s] ip=[%s] filter=[%s] is_admin=%s len=%s" %(args.db_group,msg,','.join(get_user(request)),request.remote_addr,search,is_admin(request),len(devices))
    return msg

def is_admin(request):
    users = get_user(request)
    for email_list in args.email_list.split(","):
        if email_list in users:
            return True
    return False
def get_user(request):
    #re = []
    #ip = request.remote_addr
    #users = sql_db(db_user(),where="")
    #users = to_dicts(db_user(),users)
    #for user in users:
    #    if user['ip'].find(ip) != -1:
    #        re.append(user['email'])
    #return re
    email = str(current_user)
    if email.find("flask_login") != -1:
        return ["unregistered"]
    else:
        return [email]

@app.route("/", methods=['POST', 'GET'])
def platform_def():
    return platforms("id/Team/Serial_Number/System_Type/Board_Rev/email/Task/Note/Board_Status")
@app.route("/platforms/<path:link>", methods=['POST', 'GET'])
def _platforms(link):
    return platforms(link)
@app.route("/platforms_map", methods=['POST', 'GET'])
def platforms_map():
    return platforms("id/Team/Serial_Number/System_Type/Board_Rev/email/Task/Note/Board_Status", is_map=True,
                     action="/platforms_map")
@app.route("/platforms_map/<path:link>", methods=['POST', 'GET'])
def _platforms_map(link):
    return platforms(link, is_map=True, action="/platforms_map")

def platforms(link, is_map=False, action="/platforms"):
    search = get_search(request)
    is_check_alive = False
    if search.find("alive") != -1:
        search = search.replace("alive", "")
        is_check_alive = True
    platforms = to_dicts(db_platform(), get_devices(db_platform(), search=search, is_map=is_map))
    msg = welcome("platforms", request, search, platforms)
    msg = msg + "<a href='/to_excel/platforms?search=%s'> export to excel</a> or <a href='/add_platform'> add new platforms</a>" % (
        search)

    titles = []
    for title in get_titles(link):
        href = ""
        if title["name"] == "id":
            href = "/add_platform_id"
        if title["name"] == "Serial_Number":
            href = "/console"
        if title["name"] == "System_Type":
            href = "/attached_id"
        if title["name"] == "Board_Rev":
            href = "/platform_history"
        if title["name"] == "Task":
            href = "/platform_import_log"
        titles.append({"name": title["name"], "class": title["class"], "href": href})

    return render_template('platforms.html', platforms=platforms, msg=msg, action="%s/%s" % (action, link),
                           search=search, titles=titles, is_check_alive=is_check_alive)

exec_cmd("mkdir -p static/upload")
exec_cmd("mkdir -p static/qr")

if __name__=="__main__":
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='0.0.0.0',port =args.port)