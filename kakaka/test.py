import argparse
import sqlite3
import commands

parser = argparse.ArgumentParser(description='db')
parser.add_argument('--db_file', dest='db_file', default="hahaha.db", help='dbfile')
parser.add_argument('--db_table_devices', dest='db_table_devices',default="db_table",help='db_table')
parser.add_argument('--db_element_devices', dest='db_element_devices',default="id,Chip,Vendor,Part_number,Note,Interface,Type,Ranks,RCD_Vendor,Capacity,speed,Count,Stock,Fail,Owner,Remark,Share",help='dbname')

args = parser.parse_args()

def exec_cmd(e,retry = 3):
    for i in range(0,retry):
        re = commands.getstatusoutput(e)
        if re[0] != 0:
            print re[1]
        else:
            return re
    return -1,"exec_cmd %s retry" %(e,retry)

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