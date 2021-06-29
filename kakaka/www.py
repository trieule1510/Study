import argparse
from flask import Flask,request,render_template,redirect
import commands
import sqlite3
import datetime
import os

app =Flask(__name__)
parser = argparse.ArgumentParser(description='db')
parser.add_argument('--port', dest='port',default=1234,type=int,help='www port''mlr')
parser.add_argument('--db_file', dest='db_file', default="db_file.db", help='dbfile')
parser.add_argument('--db_table_devices', dest='db_table_devices',default="db_table",help='db_table')
parser.add_argument('--db_element_devices', dest='db_element_devices',default="id,Chip,Vendor,Part_number,Note,Interface,Type,Ranks,RCD_Vendor,Capacity,speed,Count,Stock,Fail,Owner,Remark,Share",help='dbname')
parser.add_argument('--db_table_request', dest='db_table_request',default="db_table_request",help='db_table_request')
parser.add_argument('--db_element_request', dest='db_element_request',default="id,device_id,email,Part_number,number,note,info,client_info,time",help='db_element_request')
parser.add_argument('--db_table_denied', dest='db_table_denied',default="db_table_denied",help='db_table_denied')
parser.add_argument('--db_table_shared', dest='db_table_shared',default="db_table_shared",help='db_table_shared')


parser.add_argument('--email_user', dest='email_user',default="diag_equip@amperemail.onmicrosoft.com",help='email_user')
parser.add_argument('--email_password', dest='email_password',default="Ampere@2020",help='email_password')
parser.add_argument('--email_list', dest='email_list',default="trle",help='email_lists')

args = parser.parse_args()

def id_by_time():
    return str(datetime.datetime.today().strftime('%y%m%d%H%M%S%f'))

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

def db_request():
    return [args.db_file,args.db_table_request,args.db_element_request]
def db_devices():
    return [args.db_file,args.db_table_devices,args.db_element_devices]
def db_denied():
    return [args.db_file,args.db_table_denied,args.db_element_request]
def db_shared():
    return [args.db_file,args.db_table_shared,args.db_element_request]
def db_element(db):
    return db[2].split(",")

#def send_email_th(to,subject,body,attachment_location):
#    bg = Thread(target = send_email, args = (to,ascii(subject),ascii(body),attachment_location))
#    bg.do_run = True
#    bg.start()

def get_db_index(element,db):
    db_file, db_table,db_element = db_unpark(db)
    index = -1
    for e in db_element.split(","):
        index = index + 1
        if e == element:
            return index
    return -1

def email_type(type, db, device, attachment_location):
    email = device[get_db_index("email", db)]
    part_number = device[get_db_index("Part_number", db)]
    number = device[get_db_index("number", db)]
    id = device[get_db_index("id", db)]

    email_list = args.email_list + "," + email
    email_list_all = ""
    for e in email_list.split(","):
        if e == "":
            continue
        if e.find("@") == -1:
            e = e + "@amperecomputing.com"
        email_list_all = email_list_all + e + ","
    email_list_all = email_list_all[0:len(email_list_all) - 1]
    if type == "REQUEST":
        html_link = "/page_request_submit/" + str(id)
    if type == "APPROVED":
        html_link = "/page_shared_submit/" + str(id)
    if type == "RETURN":
        html_link = "/page_history_submit/" + str(id)
    if type == "DENIED":
        html_link = "/page_denied_submit/" + str(id)

    title = "Request device %s x %s  by %s" % (number, part_number, email)
    body = "Hi %s!\n" % (email.split("@")[0])
    body = "%sYour device <strong>%s %s</strong>!\n" % (body, href(part_number, html_link), type)
    body = "%s SUBMIT_ID:   %s \n" % (body, device[get_db_index("id", db)])
    body = "%s ID:          %s \n" % (body, device[get_db_index("device_id", db)])
    body = "%s EMAIL:       %s \n" % (body, email_list_all)
    body = "%s PART:        <b>%s</b> \n" % (body, part_number)
    body = "%s NUMBER:      <b>%s</b> \n" % (body, device[get_db_index("number", db)])
    body = "%s NOTE:        <b>%s</b> \n" % (body, device[get_db_index("note", db)])
    body = "%s INFO:        %s \n" % (body, device[get_db_index("info", db)])
    body = "%s CLIENT_INFO: %s \n" % (body, device[get_db_index("client_info", db)])
    body = "%s TIME:        %s \n" % (body, device[get_db_index("time", db)])

    # body = "%s <img src='http://%s:%s/static/qr/%s.png'> \n" %(body,args.web_ip,str(args.port),part_number)
    body = body.replace("\n", "<br>\n")
    #send_email_th(email_list_all, title, body, attachment_location)

def email_request(db,device,attachment_location):
    email_type("REQUEST",db,device,attachment_location)

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

def save_file_upload(id,request,type):
    file_upload =""
    f = request.files['file']
    f_pwd = ""
    if f:
        filename, file_extension = os.path.splitext(f.filename)
        file_upload = id + "_"+ type  + file_extension
        f_pwd =  args.upload_dir +"/" + file_upload
        f.save(os.path.join(args.upload_dir, file_upload))
    return f_pwd

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

def devices_filter(devices,filter=""):
    devices_filter = []
    for e in devices:
        msg = ""
        for ee in e:
            msg = "%s%s" %(msg,ee)
        append = True
        for f in filter.split(",s"):
            if msg.find(f) == -1:
                append = False
        if append:
            devices_filter.append(e)
    return devices_filter

def get_devices(db,id,filter=""):
    devices = sql_db(db,id=id)
    if filter == "" or id != None:
        return devices
    else:
        return devices_filter(devices,filter)

@app.route("/", methods=['POST', 'GET'])
def hello():
    global args
    filter = ""
    for e in request.form:
        if e == "filter" and request.form[e] !="":
            filter = request.form[e]

    #print ("request.form=",request.form[e])
    msg="Welcome %s to home filter = %s admin=%s" %(request.remote_addr,filter,is_admin(request.remote_addr))
    devices=get_devices_main(db_devices(),filter=filter)
    return render_template('home.html',devices=devices,msg=msg,filter=filter)

@app.route("/share/<path:id>", methods=['POST', 'GET'])
def share(id):
    msg="Welcome to share = %s" %(id)
    device=get_devices_main(db_devices(),id=int(id))
    if device == None:
        return render_template('error.html',msg="INVALID ID")
    element = "Index,Count,Stock,Fail,Share,Part_number,Info".split(",")
    return render_template('share.html',msg=msg,len=len(device),device=device,element=element)


@app.route("/request_submit/<path:id>", methods=['POST', 'GET'])
def request_submit(id):
    msg = "Welcome to request_submit id = %s" % (id)
    submit_id = id_by_time()
    email = request.form["email"]
    number = request.form["number"]
    note = request.form["note"]
    if note != "":
        note = "REQUEST %s: %s x%s" % (now(), note, number)
    f_pwd = save_file_upload(submit_id, request, "request")

    device = get_devices_main(db_devices(), id=int(id))
    if device == None:
        return render_template('error.html', msg="INVALID ID")

    if email == "" or number == "" or (number.isnumeric() == False) or note == "":
        msg = msg + " Error miss info <br> email='%s' number='%s' note='%s'" % (email, number, note)
        element = "Index,Count,Stock,Fail,Share,Part_number,Info".split(",")
        return render_template('share.html', msg=msg, len=len(device), device=device, element=element)
    part_number = device[5]
    info = device[6]
    client_info = request.remote_addr
    time = now()
    value = [submit_id, id, email, part_number, number, note, info, client_info, time]
    sql_db(db_request(), value=value)
    #email_request(db_request(), value, f_pwd)
    return redirect("/submit_info/%s" % (id))

@app.route("/submit_info/<path:id>", methods=['POST', 'GET'])
def submit_info(id):
    #db_file,db_table,db_element = get_devices_db()
    device=get_devices_main(db_devices(),id=int(id))
    if device == None:
        return render_template('error.html',msg="INVALID ID")
    part_number = device[5]
    msg = "Your device %s it requested . Please check email !!!" %(part_number)
    element = "Index,Count,Stock,Fail,Share,Part_number,Info".split(",")
    return render_template('submit_info.html',msg=msg,len=len(device),device=device,element=element)

@app.route("/page_request", methods=['POST', 'GET'])
def page_request():
    msg = "page_request device"
    filter = ""
    for e in request.form:
        if e == "filter" and request.form[e] !="":
            filter = request.form[e]
    devices = get_devices(db_request(),id=None,filter=filter)
    action = "/page_request"
    return render_template('devices_page.html',devices=devices,msg=msg,action=action,filter=filter)

@app.route("/page_request_submit/<path:id>", methods=['POST', 'GET'])
def approve_page(id):
    msg = "approve_page "
    device = get_devices(db_request(),id=id)
    if device == None:
        return render_template('error.html',msg="INVALID ID")
    return render_template('approve_page.html',msg=msg,len=len(device),device=device,element=db_element(db_request()))


@app.route("/denied/<path:id>", methods=['POST', 'GET'])
def denied(id):
    msg = "page_denied"
    device = get_devices(db_request(), id=id)
    if device == None:
        return render_template('error.html', msg="INVALID ID")
    key = device[get_db_index("client_info", db_request())]
    if is_admin(request.remote_addr) == False and key != request.remote_addr:
        msg = msg + " denied Your is not admin"
        return render_template('denied.html', msg=msg, len=len(device), device=device, element=db_element(db_request()))

    # copy request_device to denied_device
    value = [e for e in device]
    number = value[get_db_index("number", db_devices())]
    note = request.form["note"]
    if note != "":
        note = "DENIED %s: %s x%s" % (now(), note, number)
        value[get_db_index("note", db_request())] = value[get_db_index("note", db_request())] + "\n" + note
    sql_db(db_denied(), value=value)

    msg = msg + " Your device denied. Please check email"
    # rm request_device
    sql_db(db_request(), id=id, rm_by_id=True)
    #email_denied(db_request(), device, "")
    return render_template('denied.html', msg=msg, len=len(device), device=device, element=db_element(db_request()))


@app.route("/approved/<path:id>", methods=['POST', 'GET'])
def approved(id):
    msg = "page_approved"
    # db_file,db_table,db_element = get_request_db()

    device_request = get_devices(db_request(), id=id)
    if device_request == None:
        return render_template('error.html', msg="INVALID ID")
    device_id = device_request[get_db_index("device_id", db_request())]
    number = request.form["number"]
    # number=device_request[get_db_index("number",db_request())]
    if is_admin(request.remote_addr) == False:
        msg = msg + " denied Your is not admin"
        return render_template('denied.html', msg=msg, len=len(device_request), device=device_request,
                               element=db_element(db_request()))
    f_pwd = save_file_upload(id, request, "approved")
    # copy device to shared_db
    value = [e for e in device_request]
    note = request.form["note"]
    if note != "":
        note = "APPROVE %s: %s x%s" % (now(), note, number)
        value[get_db_index("note", db_shared())] = value[get_db_index("note", db_shared())] + "\n" + note
    value[get_db_index("number", db_shared())] = number
    print "value",value
    sql_db(db_shared(), value=value)

    # update number of devices_db
    device_main = sql_db(db_devices(), id=device_id)
    value = [e for e in device_main]

    db_Stock = value[get_db_index("Stock", db_devices())]
    if db_Stock == None:
        db_Stock = 0
    db_Share = value[get_db_index("Share", db_devices())]
    if db_Share == None:
        db_Share = 0

    value[get_db_index("Stock", db_devices())] = int(db_Stock) - int(number)
    value[get_db_index("Share", db_devices())] = int(db_Share) + int(number)
    sql_db(db_devices(), value=value, id=device_id)

    # remove device form request_db
    sql_db(db_request(), id=id, rm_by_id=True)
    #email_approved(db_request(), device_request, f_pwd)
    return render_template('approve.html', msg=msg, len=len(device_request), device=device_request,
                           element=db_element(db_request()))

if __name__=="__main__":
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host= '0.0.0.0', port=args.port)

