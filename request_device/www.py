import sqlite3
import argparse
import traceback
import datetime
from flask import Flask,request,redirect,render_template,url_for
import commands
import os
import string
import socket
from collections import OrderedDict
from flask import send_file
from flask_login import LoginManager, login_user, current_user


app = Flask(__name__)
app.secret_key = '^.6'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
parser = argparse.ArgumentParser(description='db')
parser.add_argument('--port', dest='port',default=2021,type=int,help='www port')
parser.add_argument('--db_group', dest='db_group',default="",help='devices')
parser.add_argument('--backup_db', dest='backup_db',default=1,type=int,help='backup_db')
parser.add_argument('--db_file', dest='db_file',default="db_file.db",help='db_file')
parser.add_argument('--db_table_devices', dest='db_table_devices',default="db_table",help='db_table')
parser.add_argument('--db_element_devices', dest='db_element_devices',default="id,Chip,Vendor,Part_number,Note,Interface,Type,Ranks,RCD_Vendor,Capacity,speed,Count,Stock,Fail,Owner,Remark,Share",help='dbname')

parser.add_argument('--db_table_request', dest='db_table_request',default="db_table_request",help='db_table_request')
parser.add_argument('--db_table_shared', dest='db_table_shared',default="db_table_shared",help='db_table_shared')
parser.add_argument('--db_table_history', dest='db_table_history',default="db_table_history",help='db_table_history')
parser.add_argument('--db_table_denied', dest='db_table_denied',default="db_table_denied",help='db_table_denied')
parser.add_argument('--db_element_request', dest='db_element_request',default="id,device_id,email,Part_number,number,note,info,client_info,time",help='db_element_request')

parser.add_argument('--db_platform', dest='db_platform',default="db_platform.db",help='db_platform')
parser.add_argument('--db_table_platform', dest='db_table_platform',default="db_table_platform3",help='db_table_platform')
parser.add_argument('--db_element_platform', dest='db_element_platform',default="id,Team,Name,Location,Serial_Number,Chassis_SN,HW_label,System_Type,Board_Rev,Occupation,Cielo,Board_Status,email,Task,CPU,VRD,CPLD_Main,CPLD_Backplane,bmcip,hostip,hostuser,hostpass,hostport,tty_bmc,tty_uefi,tty_atf,tty_s0cli,tty_s1cli,Note,client_info,time",help='db_element_platform')

parser.add_argument('--db_cpu', dest='db_cpu',default="db_cpu.db",help='db_cpu')
parser.add_argument('--db_cpu_table', dest='db_cpu_table',default="db_cpu_table",help='db_cpu_table')
parser.add_argument('--db_cpu_element', dest='db_cpu_element',default="id,version,sum,deliver,onwer_deliver,date_arrived,description,client_info,time",help='db_cpu_element')

parser.add_argument('--db_platform_devices', dest='db_platform_devices',default="db_platform_devices.db",help='db_platform_devices')
parser.add_argument('--db_table_platform_devices', dest='db_table_platform_devices',default="db_table_platform_devices",help='db_table_platform')
parser.add_argument('--db_element_platform_devices', dest='db_element_platform_devices',default="device_id,platform_id",help='db_element_platform_devices')

parser.add_argument('--db_user', dest='db_user',default="db_user.db",help='db_user')
parser.add_argument('--db_user_table', dest='db_user_table',default="db_user_table2",help='db_user_table')
parser.add_argument('--db_user_element', dest='db_user_element',default="email,passw,ip",help='db_user_element')

parser.add_argument('--email_list', dest='email_list',default="cpham,hqbui,nble,trle,tait",help='admin email_list')
parser.add_argument('--upload_dir', dest='upload_dir',default="static/upload/",help='upload_dir')
parser.add_argument('--web_ip', dest='web_ip',default="hcm-l-027",help='web_ip')
parser.add_argument('--ws_ip', dest='ws_ip',default="10.38.13.102:2120",help='ws_ip')
parser.add_argument('--fail_signal', dest='fail_signal',default="Call trace\|crashdump kernel\|Kernel panic\|Hardware error\|Synchronous Exception\|mismatch errors\|initialization failure\|Killed",help='fail_sign')


args = parser.parse_args()
g_boards = []
g_boards.append({"board":"jade","bmc_user":"root","bmc_pass":"root","U":"ADMIN","P":"ADMIN","cmd_before":"gpiotool --set-data-low 226","bmc_after":"gpiotool --set-data-high 226"})
g_boards.append({"board":"snow","bmc_user":"sysadmin","bmc_pass":"superuser","U":"admin","P":"password","cmd_before":"gpiotool --set-dir-output 139&&gpiotool --set-data-low 139","bmc_after":"gpiotool --set-dir-output 139&&gpiotool --set-data-high 139"})
g_boards.append({"board":"collins","bmc_user":"sysadmin","bmc_pass":"superuser","U":"admin","P":"admin","cmd_before":"echo ~","bmc_after":"echo ~"})

def db_devices():
    return [args.db_file,args.db_table_devices,args.db_element_devices]
def db_shared():
    return [args.db_file,args.db_table_shared,args.db_element_request]
def db_history():
    return [args.db_file,args.db_table_history,args.db_element_request]
def db_denied():
    return [args.db_file,args.db_table_denied,args.db_element_request]
def db_request():
    return [args.db_file,args.db_table_request,args.db_element_request]
def db_platform():
    return [args.db_platform,args.db_table_platform,args.db_element_platform]
def db_platform_history(id):
    table = "platform_%s" %(id)
    return ["db_platform_history.db",table,args.db_element_platform]
def db_platform_info(id):
    table = "platform_info_%s" %(id)
    return ["db_platform_info.db",table,"id,ddr_info,pci_info,cpu_info,time"]
def db_device_history(id):
    table = "devices_%s" %(id)
    return ["db_devices_history.db",table,args.db_element_devices]
def db_platform_devices():
    return [args.db_platform_devices,args.db_table_platform_devices,args.db_element_platform_devices]
def db_user():
    return [args.db_user,args.db_user_table,args.db_user_element]
def db_test_cfg(id):
    table = "test_cfg_%s" %(id)
    return ["test_cfg.db",table,"id,bmc_fw,scp_fw,atfbios_fw,test_cfg,nvparm,cmd,nvparm_board_setting,user_cfg1,user_cfg2"]
def db_element(db):
    return db[2].split(",")
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
if args.web_ip =="":
    args.web_ip = get_ip()
def find_in( s, first="", last="" ,A=0,B=0):
    try:
        start = s.index( first ) + len( first ) 
        if last == "":
            end = len(s)
        else:
            end = s.index( last, start ) 
        return s[start-A:end+B]
    except ValueError:return ""
def id_by_time():
    return str(datetime.datetime.today().strftime('%y%m%d%H%M%S%f'))
def count_days(id_time):
    date0 = datetime.datetime.strptime(id_time, '%y%m%d%H%M%S%f')
    date1 = datetime.datetime.strptime(id_by_time(), '%y%m%d%H%M%S%f')
    re = find_in(str(date1 - date0),""," days")
    if re == "":
        re = "0"
    return int(re)
def now():
    return str(datetime.datetime.today().strftime('%y%m%d_%H%M%S'))
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
def is_valid_user(user,request):
    if user == "" or user == "FREE" or user == None:
        return True
    for u in user.split(","):
        if u in get_user(request):
            return True
    return False
def open_file(filename):
    try:
        f = open(filename, "r")
        text = f.read()
        f.close()
        return text;
    except:
        return ""
def cfg_file(pwd,_user=""):
    re = []
    exec_cmd("mkdir -p %s" %(pwd))
    for root, dirs, files in os.walk(pwd):
        re = ["%s%s" % (pwd, f) for f in files]
        break
    if _user != "":
        exec_cmd("mkdir -p %s/%s" %(pwd,_user)) 
        for root, dirs, files in os.walk("%s/%s" %(pwd,_user)):
            re = re + ["%s%s/%s" % (pwd,_user, f) for f in files]
            break
    return sorted(re)
def backup_db(db_file,dir="backup/"):
    if args.backup_db != 0:
        exec_cmd("mkdir -p %s" %(dir))
        exec_cmd("cp -rf %s %s/%s-%s" %(db_file,dir,db_file,now()))
def db_unpark(db):
    return db[0],db[1],db[2]
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
            print traceback.print_exc()
            pass
        con.close()         
def href(name,pwd):
    if args.web_ip =="":
        args.web_ip = get_ip()
    return "<a href='http://%s:%s%s'> %s </a>" %(args.web_ip,str(args.port),pwd,name)
def get_db_index(element,db):
    db_element = db[2]
    index = -1
    for e in db_element.split(","):
        index = index + 1
        if e == element:
            return index
    return -1

def wrlog(msg,file_name=""):
    exec_cmd("mkdir -p %s " %(os.path.dirname(file_name)))
    try:
        f=open(file_name, "a+")
        f.write("%s" %(msg))
        f.close()
    except:
        print "ERR wrlog %s " %(file_name)
def exec_cmd(e):
    if e.find("mkdir") != 0:
        print e
    re = commands.getstatusoutput(e)
    return re

def _replace(e,r={"\n":"","\r":""}):
    for rr in r:
        e = e.replace(rr,r[rr])
    return e
def get_cpu_serial_number(log):
    re = ""
    for e in log.split("\n"):
        v = find_in(e,"0000000000000000","")
        if v != "" and e.find("Serial Number") != -1:
            re = "%s%s<br>" %(re,v)
    return re
def get_lspci_info(log):
    re = ""
    v = find_in(log,"lspci;rc","_rc_")
    if v == "":
        v = find_in(log,"# lspci","#") 
    for e in v.split("\n"):
        if e.find("Ampere Computing") == -1:
            re = "%s%s<br>" %(re,e)
    return re
def get_cpu_info(log):
    err_authenticate_pm = find_in(log,"ERR: Authenticate PM","")
    if err_authenticate_pm != "":
        return "ES1/ES2 non-TMM"
    bl1_load = find_in(log,"ERR: BL1 load","")
    if bl1_load !="":
        return "ES1/ES2 TMM"
    authenticated_pmpro = find_in(log,"Authenticated PM","")
    bl1_authenticated = find_in(log,"BL1 auth","")
    cli = find_in(log,"-cli","")
    if authenticated_pmpro != "" and bl1_authenticated != "":
        if cli !="":
            return "ES3 TMM"
        else:
            return "EPR/PR TMM"
    return ""
def get_pci_info(log):
    info = []
    for e in log.split("\n"):
        pci_device_raw = find_in(e," pci "," type ")
        pci_device = find_in(pci_device_raw,"[","]")
        if pci_device == "" or pci_device.find("1def") == 0:
            continue
        print pci_device
        re = commands.getstatusoutput("grep %s -R pci.ids.grep" %(pci_device.replace("[", "")))
        if re[0] == 0:
            info.append(re[1])
        else:
            info.append(pci_device)
    return info
def get_ddr_info(log):
    re = OrderedDict()
    re['ddr_ver'] = _replace(find_in(log,"DRAM FW version ","\n"))
    re['ddr_speed'] = _replace(find_in(log,"DRAM: ","\n"),{" DDR4 ":"_"," ":"_","\r":""})
    re['cpu_core'] = find_in(log,"SMP: Total of ","processors activated")
    re['soc_value'] = find_in(log,"Soc voltage      : ","\r\n")
    dimm_list=find_in(log,"DRAM populated DIMMs:","CP")
    if dimm_list.find("SK1") != -1:
        re['socket'] = "2P"
    elif dimm_list.find("SK0") != -1:
        re['socket'] = "1P"
    else:
        re['socket'] = "NA"
    if dimm_list.find(" S1: ")!= -1:
        re['DPC']  = "2DPC"
    elif dimm_list.find(" S0: ")!= -1:
        re['DPC']  = "1DPC"
    else:
        re['DPC']  = "NA"
    re['number_dimm']=str(dimm_list.count("MC"))
    dimm_type=""
    if dimm_list!="":
        dimm_type =""
        _dimm_type_old =""
        _dimm_size =""
        for e in dimm_list.split('\n'):
            for e1 in e.split(" "):
                if e1.find("GB") != -1:
                    _dimm_size = e1
                if len(e1) > 12 and  e1 != _dimm_type_old:
                    _dimm_type_old = e1
                    dimm_type = "%s%dxDIMM_%s_%s_" %(dimm_type ,dimm_list.count(e1),_dimm_size,e1)
        if len(dimm_type) > 1:
            dimm_type = dimm_type[0:len(dimm_type)-1]
    else:
        dimm_type=""
    re['dimm_type'] = dimm_type
    return re
def ascii(text):
    try:
        return ''.join([x for x in text if x in string.printable])
    except:
        return text
def send_email_th(to,subject,body,attachment_location=""):
    os.system("./send_mail --email_list '%s' --subject '%s' --body '%s' --attachment_location '%s' &" %(to,ascii(subject),ascii(body),attachment_location))

def to_email_list(email):
    email_list = args.email_list + "," + email
    email_list_all = ""
    for e in email_list.split(","):
        if e == "" : 
            continue
        if e.find("@") == -1:
            e = e + "@amperecomputing.com"
        email_list_all = email_list_all + e +","
    email_list_all = email_list_all[0:len(email_list_all) -1]
    return email_list_all
def email_type(request,type,db,device,attachment_location):
    email =device[get_db_index("email",db)]
    email_list_all = to_email_list(email)
    part_number =device[get_db_index("Part_number",db)]
    number =device[get_db_index("number",db)]
    id = device[get_db_index("id",db)]
    if type == "REQUEST":
        html_link = "/page_request_submit/" + str(id)
    if type == "APPROVED":
        html_link = "/page_shared_submit/"  + str(id)
    if type == "MOVE TO":
        html_link = "/page_shared_submit/"  + str(id)
    if type == "RETURN" :
        html_link = "/page_history_submit/" + str(id)
    if type == "DENIED" :
        html_link = "/page_denied_submit/" + str(id)
   
    title = "%sRequest device %s x %s  by %s" %(args.db_group,number,part_number,email) 
    body = "Hi %s!\n" %(email.split("@")[0])
    body = "%sYour device <strong>%s %s</strong>!\n" %(body,href(part_number,html_link),type)
    body = "%s SUBMIT_ID:   %s \n" %(body,device[get_db_index("id",db)])
    body = "%s ID:          %s \n" %(body,device[get_db_index("device_id",db)])
    body = "%s EMAIL:       %s \n" %(body,email_list_all)
    body = "%s PART:        <b>%s</b> \n" %(body,part_number)
    body = "%s NUMBER:      <b>%s</b> \n" %(body,device[get_db_index("number",db)])
    body = "%s NOTE:        <b>%s</b> \n" %(body,device[get_db_index("note",db)])
    body = "%s BOARD SERIAL:        %s \n"%(body,get_db_platform_devices(id))
    body = "%s INFO:        %s \n" %(body,device[get_db_index("info",db)])
    body = "%s %s \n" %(body,href("DRAM Handling Guide","/static/DRAM_Handling_Guide.pdf"))
    body = "%s %s \n" %(body,href("ESD Control Selection Guide","/static/ESD.pdf"))
    body = "%s CLIENT_INFO: %s \n" %(body,device[get_db_index("client_info",db)])
    body = "%s TIME:        %s \n"%(body,device[get_db_index("time",db)])
    body = "%s USER %s IP %s ADMIN %s" %(body,','.join(get_user(request)),request.remote_addr,is_admin(request))
    
    body = body.replace("\n", "<br>\n")
    send_email_th(email_list_all,title,body,attachment_location)
def email_noti(db,device,email,body):
    body = "%s\n USER %s IP %s ADMIN %s" %(body,','.join(get_user(request)),request.remote_addr,is_admin(request))
    body = body.replace("\n","<br>\n")
    email_list_all = to_email_list(email)
    part_number = device[get_db_index("Part_number",db)]
    number = device[get_db_index("number",db)]
    title = "%sRequest device %s x %s  by %s" %(args.db_group,number,part_number,email)
    send_email_th(email_list_all,title,body)
def email_request(request,db,device,attachment_location):
    email_type(request,"REQUEST",db,device,attachment_location)
def email_approved(request,db,device,attachment_location): 
    email_type(request,"APPROVED",db,device,attachment_location)
def email_move_to(request,db,device,attachment_location): 
    email_type(request,"MOVE TO",db,device,attachment_location)
def email_denied(request,db,device,attachment_location): 
    email_type(request,"DENIED",db,device,attachment_location)
def email_return(request,db,device,attachment_location): 
    email_type(request,"RETURN",db,device,attachment_location)
# /home --> /page_shared  --> page_shared_submit -->page_shared_return
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
def get_devices(db,id=None,search="",is_map=False):
    devices = sql_db(db,id=id)
    if id == None:
        devices =  device_search(db,devices,search,is_map)
    else:
        if devices == None or len(devices) == 0:
            return None
        return devices[0]
    return devices
def color(test="",color="red"):
    return "<p style='color:%s'>%s</p>" %(color,test)
def devices_add_days(devices):
    re = []
    for device in devices:
        try:
            e = [ee for ee in device]
            days =  count_days(str(e[0]))
            if days > 30:
                e[1] = color("%s(%s days)" %(e[1],count_days(str(e[0]))),"red")
            else:
                e[1] = "%s(%s days)" %(e[1],count_days(str(e[0])))
            re.append(e)
        except:
            continue
    return re
def count_week(db):
    shared_week = OrderedDict()
    devices = get_devices(db,id=None,search="")
    devices = to_dicts(db, devices)
    for device in devices:
        if device['id'] == "":
            continue
        week =  count_days(str(device['id']))/7
        if week in shared_week:
            shared_week[week] = shared_week[week] + 1
        else:
            shared_week[week] = 1
    return shared_week
@app.route("/equipment_report", methods=['POST', 'GET'])
def fa():
    search = get_search(request)
    devices = get_devices(db_devices(),id=None,search=search)
    devices = to_dicts(db_devices(), devices)
    part = 0
    for device in devices:
        try:
            part = part + int(device['Count'])
        except:
            pass
    shared = count_week(db_shared())
    history = count_week(db_history())
    labels = ["Week %s" %(v) for v in shared]
    msg = "Equipment weekly report total:%s devices %s parts" %(len(devices),part)
    datasets=""
    datasets="%s{label: '%s',data: %s,backgroundColor:'red',borderColor:'red',fill: false}," %(datasets,"shared",str([shared[v] for v in shared]))
    datasets="%s{label: '%s',data: %s,backgroundColor:'blue',borderColor:'blue',fill: false}," %(datasets,"return",str([history[v] for v in history]))    
    return render_template('chartjs.html',labels=labels,datasets=datasets,char_id="shared",msg=msg,action="/fa",search=search)
@app.route("/page_shared", methods=['POST', 'GET'])
def page_shared():
    search = get_search(request)       
    devices = get_devices(db_shared(),id=None,search=search)
    msg = welcome("page_shared",request,search,devices)
    msg = msg + "<a href='/to_excel/shared?search=%s'> export to excel</a>" %(search)
    devices = devices_add_days(devices)
    devices = to_dicts(db_shared(), devices)
    title_link = "id/device_id/email/Part_number/number/note"
    titles=[]
    for title in get_titles(title_link):
        href = "" 
        if title["name"] == "email":
            href = "/send_noti"
        if title["name"] == "Part_number":
            href = "/page_shared_submit"
        titles.append({"name":title["name"],"class":title["class"],"href":href})
        
    return render_template('home.html',titles=titles,devices=devices,msg=msg,action="/page_shared",search=search)
@app.route("/page_shared_submit/<path:id>", methods=['POST', 'GET'])
def page_shared_submit(id):
    search = get_search(request)
    msg = welcome("page_shared_submit",request,search)
    device = get_devices(db_shared(),id=id)
    if device == None:
        return render_template('error.html',msg="INVALID ID")
    board_serial = get_db_platform_devices(id)
    board_serials = get_board_serials("")
    h_attached = attached(id)
    return render_template('return_page.html',msg=msg,len=len(device),device=device,board_serial=board_serial,board_serials=board_serials,element=db_element(db_shared()),h_attached=h_attached) 
@app.route("/fix", methods=['POST', 'GET'])
def fix():
    re = ""
    devices=to_dicts(db_devices(),get_devices(db_devices(),search=""))
    for device in devices:
        print device["Part_number"]
        re = "%s %s %s<br>" %(re,device["id"],device["Part_number"])
        s = "%s%s" %(args.upload_dir,device["Part_number"])
        d = "%s/devices/%s" %(args.upload_dir,device["id"])
        s = ascii(s)
        d = ascii(d)
        print "cp -rf '%s' '%s'" %(s,d)
        os.system("cp -rf '%s' '%s'" %(s,d))
    return re
def save_files(request,pwd,fname=""):
    pwd = "%s%s" %(args.upload_dir,pwd)
    print "save_files pwd=%s" %(pwd)
    os.system("mkdir -p %s" %(pwd))
    user = '_'.join(get_user(request))
    files = request.files.getlist('file')
    f_pwd = ""
    i = 0
    for f in files:
        if f:
            i = i + 1
            file_name, file_extension = os.path.splitext(f.filename)
            if fname == "":
                file_name = "%s_%s_%s%s" %(file_name,i,user,file_extension)
            else:
                file_name = "%s_%s_%s%s" %(fname,i,user,file_extension)
            print "save_files %s"  %(file_name)
            f.save(os.path.join(pwd, file_name))
            f_pwd =  f_pwd +  os.path.join(pwd, file_name) +","
    return f_pwd
@app.route("/page_shared_return/<path:id>", methods=['POST', 'GET'])
def return_device(id):
    msg = "Welcome to return_device id=%s" %(id)
    device = get_devices(db_shared(),id=id)
    if device == None:
        return render_template('error.html',msg="INVALID ID") 
    #key=device[get_db_index("client_info",db_shared())]
    
    device_id=device[get_db_index("device_id",db_shared())]
    number=device[get_db_index("number",db_shared())]
    return_number = 0
    if  is_admin(request) == False:
        return render_template('error.html',msg="Your is not admin")
    f_pwd = save_files(request,pwd = "devices/%s" %(device_id),fname = "return_%s" %(id))
#copy shared_device to history_device
    value = [e for e in device]
    try:
        note = request.form["return_note"]
        return_number = int(request.form["return_number"])
        number = int(number)
    except:
        return render_template('error.html',msg="INVALID Number")
    if note != "":
        note = "RETURN %s: %s x%s" %(now(),note,return_number) 
        value[get_db_index("note",db_history())] = value[get_db_index("note",db_history())] +"\n" + note
    value[get_db_index("number",db_history())] =  return_number
    
    sql_db(db_history(),value=value)
    email_value = value

#Update 
    
    device_main = sql_db(db_devices(),id=device_id)[0] 
    value = [e for e in device_main] 

    db_Stock = device_main[get_db_index("Stock",db_devices())]
    if db_Stock == None:
        db_Stock = 0
    db_Share = value[get_db_index("Share",db_devices())]
    if db_Share == None:
        db_Share = 0
    value[get_db_index("Stock",db_devices())] = int(db_Stock) + return_number
    value[get_db_index("Share",db_devices())] = int(db_Share) - return_number
    sql_db(db_devices(),value=value,id=device_id)

#Remote shared_device form db or Update if number
    device = sql_db(db_shared(),id=id)[0]
    value = [e for e in device]
    sql_db(db_shared(),id=id,rm=True)
    if return_number != number :
        value[get_db_index("number",db_shared())] = int(value[get_db_index("number",db_shared())]) - return_number
        value[get_db_index("note",db_shared())] = value[get_db_index("note",db_shared())] + "\nRETURN %s: %s [number=x%d]" %(now(),note,return_number)
        sql_db(db_shared(),value=value,id=id)
#Remote platform_device
    sql_db(db_platform_devices(),id=id,rm=True)
    
    msg = msg + " Return device approved!"
    value[get_db_index("number",db_shared())] = return_number
    if True == False:
        for db_type in ["shared","devices"]:
            re = save_xlsx(request,db_type)
            if re[0] == True:
                f_pwd = "%s,%s" %(f_pwd,re[1])
    email_return(request,db_shared(),email_value,f_pwd)
    return render_template('approve.html',msg=msg,len=len(device),device=device,element=db_element(db_shared()))

@app.route("/move_to/<path:id>", methods=['POST', 'GET'])
def move_to(id):
    move_to_user = request.form["move_to_user"]
    move_to_board_serial = request.form["board_serial"].split(":")[0]
    msg = "Welcome to move_to id=%s" %(id)
    #db_file,db_table,db_element = get_shared_db()
    
    device = get_devices(db_shared(),id=id)
    if device == None:
        return render_template('error.html',msg="INVALID ID") 
    
    device_id=device[get_db_index("device_id",db_shared())]
    number=device[get_db_index("number",db_shared())]
    email = device[get_db_index("email",db_shared())]
    
    value = [e for e in device]
    try:
        move_to_note = request.form["move_to_note"]
        move_to_number = int(request.form["move_to_number"])
        number = int(number)
    except:
        return render_template('error.html',msg="INVALID Number")
    
    if  (is_admin(request) == False):
        if email.lower() != move_to_user.lower():
            return render_template('error.html',msg="Your is not admin")    
#copy shared_device to shared_device new_user    
    f_pwd = save_files(request,pwd = "devices/%s" %(device_id),fname = "move_to_%s" %(id))
    if move_to_note != "":
        note = "MOVETO %s: %s x%s board_serial %s" %(now(),move_to_note,move_to_number,request.form["board_serial"]) 
        email = value[get_db_index("email",db_shared())]
        value[get_db_index("note",db_shared())] = "%s\n%s[%s-->%s]" %(value[get_db_index("note",db_shared())],note,email,move_to_user)
    value[get_db_index("number",db_shared())] =  move_to_number
    value[get_db_index("email",db_shared())] = move_to_user
    value[get_db_index("id",db_shared())] = id_by_time()

    sql_db(db_platform_devices(),[value[get_db_index("id",db_shared())],move_to_board_serial])
    
    sql_db(db_shared(),value=value)
    
    email_move_to(request,db_shared(),value,f_pwd)
#Remove shared_device form db or Update if number
    device = sql_db(db_shared(),id=id)[0]
    value = [e for e in device]
    sql_db(db_shared(),id=id,rm=True)
    value[get_db_index("number",db_shared())] = int(value[get_db_index("number",db_shared())]) - move_to_number
    value[get_db_index("note",db_shared())] = "%sMOVE TO %s:Your device is move to %s x%s %s\n" %(value[get_db_index("note",db_shared())],now(),move_to_user,move_to_number,move_to_note)
    if  value[get_db_index("number",db_shared())] != 0:   
        sql_db(db_shared(),value=value,id=id)
    else:
        sql_db(db_history(),value=value,id=id)
    
    msg = msg + " move to device approved!"
    
    value[get_db_index("number",db_shared())] = move_to_number
    email_return(request,db_shared(),value,f_pwd)
    return render_template('approve.html',msg=msg,len=len(device),device=device,element=db_element(db_shared()))


@app.route("/attached/<path:id>", methods=['POST', 'GET'])
def attached(id):
    id = id.replace(" ","")
    pwd = args.upload_dir + "/devices/" + id
    try:
        files = os.listdir(pwd)
    except:
        files = []
    return render_template('attached.html',msg=pwd,pwd=pwd,files=files)
@app.route("/attached_id/<path:id>", methods=['POST', 'GET'])
def attached_id(id):
    id = id.replace(" ","")
    pwd = args.upload_dir + "/" + id
    try:
        files = os.listdir(pwd)
    except:
        files = []
    return render_template('attached.html',msg="",pwd=pwd,files=files)

@app.route("/device_history/<path:id>", methods=['POST', 'GET'])
def device_history(id):
    db = db_device_history(id)
    search = get_search(request)
    history_devices = get_devices(db,search=search)
    device = sql_db(db_devices(),id=id)[0]
    history_devices.append(device)
    dbs=to_dicts(db,history_devices)
    msg = welcome("device_history",request,search,dbs)
    title_link = '/'.join(db_element(db))
    titles=[]
    for title in get_titles(title_link):
        href = "" 
        titles.append({"name":title["name"],"class":title["class"],"href":href})
    return render_template('home.html',titles=titles,devices=dbs,msg=msg,action="/",search=search)

def noti_device_edit(request,device,device_edit,id):
    title = "%snoti_device_edit" %(args.db_group)
    body = ""

    device = to_dict(db_devices(), device)
    device_edit = to_dict(db_devices(), device_edit)
    for e in device:
        if str(device[e]) == str(device_edit[e]):
            body = "%s%s: %s --> %s <br>" %(body,e,device[e],device_edit[e])
        else:
            body = "%s%s: %s --> %s <br>" %(body,e,device[e],color(device_edit[e]))
    body = body + "\nUSER %s IP %s ADMIN %s" %(','.join(get_user(request)),request.remote_addr,is_admin(request))
    body = body.replace("\n", "<br>")
    email_list_all = to_email_list(args.email_list)
    send_email_th(email_list_all,title,body,attachment_location="")
    
def save_device_history(request,device_edit,id):
    try:
        device = sql_db(db_devices(),id=id)[0]
        device = [e for e in device]
        if device == None:
            return False
        for i in range(0,len(device)):
            if str(device[i]) != str(device_edit[i]):
                noti_device_edit(request,device,device_edit,id)
                db = db_device_history(device[0])
                device[0] = id_by_time()
                sql_db(db,device)
                return True
    except:
        return False
    return False
# /home --> /edit/id
@app.route("/edit/<path:id>", methods=['POST', 'GET'])
def edit(id):
    id = id.replace(" ","")
    msg = "EDIT %s " %(id)
    #db_file,db_table,db_element = get_devices_db()
    device = ["" for e in db_element(db_devices())]
    is_wr = False
    for e in request.form:
        if e.find("file") == 0:
            continue
        device[get_db_index(e,db_devices())] = ascii(request.form[e])
        is_wr = True
    if is_wr and is_admin(request):
        Part_number = device[get_db_index("Part_number",db_devices())]
        if Part_number == "  " or Part_number == "":
            msg = msg + "!!!ERROR: Part_number is INVALID "
        try:
            Count=int(device[get_db_index("Count",db_devices())])
            Stock=int(device[get_db_index("Stock",db_devices())])
            Fail=int(device[get_db_index("Fail",db_devices())])
            Share=int(device[get_db_index("Share",db_devices())])
            if Count != (Stock + Fail + Share):
                msg = msg + "!!!ERROR: Count != Stock + Fail + Share !!! "
            save_files(request,pwd = "devices/%s" %(id))
        except:
            #print traceback.print_exc()
            msg = msg + "!!!ERROR: Count/Stock/Fail/Share is INVALID "
        value = [e for e in device]
        value[get_db_index("id",db_devices())] = id
        save_device_history(request,device,id)
        sql_db(db_devices(),id=id,value=value)
        msg = msg + "Updated"
    else:
        if  is_admin(request) == False:
            msg = msg + " !!!You NOT is admin!!! "
    try:
        device=sql_db(db_devices(),id=id)[0]
    except:
        device = ["" for e in db_element(db_devices())]
        device[get_db_index("id",db_devices())] = id
        device[get_db_index("Share",db_devices())] = 0
        device[get_db_index("Fail",db_devices())] = 0
        device[get_db_index("Stock",db_devices())] = 0
        device[get_db_index("Count",db_devices())] = 0
        device[get_db_index("Owner",db_devices())] = "admin"
        device[get_db_index("Remark",db_devices())] = now()
        device[get_db_index("Chip",db_devices())] = "Altra"
    device = to_dict(db_devices(), device)
    devices = to_dicts(db_devices(),get_devices(db_devices()))
    datalist = get_datalist(db_devices(),devices)
    action = "/edit/" +  id
    h_attached = attached(id)
    return render_template('edit.html',len=len(device),id=id,device=device,msg=msg,datalist=datalist,action=action,h_attached=h_attached)
@app.route("/page_add", methods=['POST', 'GET'])
def page_add():
    try:
        id = sql_db(db_devices(),select_max="id")
        if id == None:
            index = 1
        else:
            index = int(id) +  1
        return redirect("/edit/%d" %(index))
    except:
        return render_template('error.html',msg="INVALID ID") 
# /home --> /page_history
@app.route("/page_history", methods=['POST', 'GET'])
def page_history():
    search = get_search(request)
    devices = get_devices(db_history(),id=None,search=search)
    msg = welcome("page_history",request,search,devices)
    devices=to_dicts(db_history(), devices)
    title_link = "id/device_id/email/Part_number/number/note"
    titles=[]
    for title in get_titles(title_link):
        href = "" 
        titles.append({"name":title["name"],"class":title["class"],"href":href})
    return render_template('home.html',titles=titles,devices=devices,msg=msg,action="/page_history",search=search)
@app.route("/page_history_submit/<path:id>", methods=['POST', 'GET'])
def page_history_submit(id):
    return redirect(url_for("page_history"))
#/home --> /page_denied -->/page_denied_submit
@app.route("/page_denied", methods=['POST', 'GET'])
def page_denied():
    search = get_search(request) 
    devices = get_devices(db_denied(),id=None,search=search)
    msg = welcome("page_denied",request,search,devices)
    devices=to_dicts(db_denied(), devices)
    title_link = "id/device_id/email/Part_number/number/note"
    titles=[]
    for title in get_titles(title_link):
        href = "" 
        titles.append({"name":title["name"],"class":title["class"],"href":href})
    return render_template('home.html',titles=titles,devices=devices,msg=msg,action="/page_denied",search=search)
# /home --> /page_request --> /page_request_submmit -->approved |denied
@app.route("/page_request", methods=['POST', 'GET'])
def page_request():
    search = get_search(request) 
    devices = get_devices(db_request(),id=None,search=search)
    msg = welcome("page_request",request,search,devices)
    devices=to_dicts(db_request(), devices)
    title_link = "id/device_id/email/Part_number/number/note"
    titles=[]
    for title in get_titles(title_link):
        href = "" 
        if title["name"] == "Part_number":
            href = "/page_request_submit"
        titles.append({"name":title["name"],"class":title["class"],"href":href})        
    return render_template('home.html',titles=titles,devices=devices,msg=msg,action="/page_request",search=search)

@app.route("/page_request_submit/<path:id>", methods=['POST', 'GET'])
def approve_page(id):
    msg = "approve_page "
    device = get_devices(db_request(),id=id)
    if device == None:
        return render_template('error.html',msg="INVALID ID") 
    h_attached = attached(id)
    return render_template('approve_page.html',msg=msg,len=len(device),device=device,element=db_element(db_request()),h_attached=h_attached) 

@app.route("/approved/<path:id>", methods=['POST', 'GET'])
def approved(id):
    msg = "page_approved"
    #db_file,db_table,db_element = get_request_db()
    
    device_request = get_devices(db_request(),id=id)
    if device_request == None:
        return render_template('error.html',msg="INVALID ID") 
    device_id=device_request[get_db_index("device_id",db_request())]
    number = request.form["number"]
    #number=device_request[get_db_index("number",db_request())]
    if  is_admin(request) == False:
        return render_template('error.html',msg="Your is not admin")
    
    f_pwd = save_files(request,pwd = "devices/%s" %(device_id),fname = "approved_%s" %(id))
    #copy device to shared_db
    value = [e for e in device_request]
    note = request.form["note"]
    note = "APPROVE %s: %s x%s\n" %(now(),note,number) 
    value[get_db_index("note",db_shared())] = value[get_db_index("note",db_shared())] +"\n" + note
    
    value[get_db_index("number",db_shared())] = number
    sql_db(db_shared(),value=value)
    
    value_request = value    
    #update number of devices_db
    device_main = sql_db(db_devices(),id=device_id)
    value = [e for e in device_main[0]] 
    
    db_Stock = value[get_db_index("Stock",db_devices())]
    if db_Stock == None:
        db_Stock = 0
    db_Share = value[get_db_index("Share",db_devices())]
    if db_Share == None:
        db_Share = 0
        
    value[get_db_index("Stock",db_devices())] = int(db_Stock) - int(number)
    value[get_db_index("Share",db_devices())] = str2int(db_Share) + int(number)
    sql_db(db_devices(),value=value,id=device_id)
    
    #remove device form request_db
    sql_db(db_request(),id=id,rm=True)
    if True == False:
        for db_type in ["shared","devices"]:
            re = save_xlsx(request,db_type)
            if re[0] == True:
                f_pwd = "%s,%s" %(f_pwd,re[1])

    email_approved(request,db_request(),value_request,f_pwd)
    return render_template('approve.html',msg=msg,len=len(device_request),device=device_request,element=db_element(db_request()))
@app.route("/denied/<path:id>", methods=['POST', 'GET'])
def denied(id):
    msg = "page_denied"
    device = get_devices(db_request(),id=id)
    if device == None:
        return render_template('error.html',msg="INVALID ID")
    key=device[get_db_index("client_info",db_request())]
    if  is_admin(request) == False and key != request.remote_addr:
        return render_template('error.html',msg="Your is not admin")
    
    #copy request_device to denied_device
    value = [e for e in device]
    number = value[get_db_index("number",db_devices())]
    note = request.form["note"]
    if note != "":
        note = "DENIED %s: %s x%s" %(now(),note,number) 
        value[get_db_index("note",db_request())] = value[get_db_index("note",db_request())] +"\n" + note
    sql_db(db_denied(),value=value)
    
    msg = msg + " Your device denied. Please check email"
    #rm request_device
    sql_db(db_request(),id=id,rm=True)
    email_denied(request,db_request(),value,"")
    return render_template('denied.html',msg=msg,len=len(device),device=device,element=db_element(db_request()))
# /home --> /share --> /request_submit --> /submit_info
def str2int(str):
    try:
        return int(str)
    except:
        return 0
def format_devices_main(db,devices):
    _devices=[]
    for e in devices:
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
        _devices.append([Index,Count,Stock,Fail,Share,Part_number,Other])
    return _devices

def get_devices_main(db,id=None,search=""):
    devices = sql_db(db,id=id)
    if id == None:
        devices = device_search(db,devices,search=search)
    devices = format_devices_main(db,devices)
    if id != None:
        return devices[0]
    return devices
@app.route("/qr_code/<search>", methods=['POST', 'GET'])
def qr_code_search(search):
    devices = get_devices(db_devices(),None,search=search)
    return render_template('qr_page.html',devices=devices)
@app.route("/qr_code", methods=['POST', 'GET'])
def qr_code():
    devices = get_devices(db_devices(),None)
    return render_template('qr_page.html',devices=devices)
def get_search(request):
    f = ""
    if request.args.get("search")!=None:
        f = request.args.get("search")
    for e in request.form:
        if e == "search" and request.form[e] !="":
            f = request.form[e]
    return f
def welcome(msg,request,search,devices=""):
    msg="[%s %s] user=[%s] ip=[%s] filter=[%s] is_admin=%s len=%s" %(args.db_group,msg,','.join(get_user(request)),request.remote_addr,search,is_admin(request),len(devices))
    return msg
@app.route("/<path:title_link>", methods=['POST', 'GET'])
def home_title(title_link):
    return home(title_link)
@app.route("/", methods=['POST', 'GET'])
def hello():
    return home()
def get_other_title(db,titles):
    other = []
    element = db_element(db)
    for e in element:
        if (e in [title["name"] for title in titles]) == False:
            other.append(e)
    return other
def home(title_link=""):
    global args
    search = get_search(request)
    devices=to_dicts(db_devices(),get_devices(db_devices(),search=search))
    msg = welcome("home",request,search,devices)
    msg = msg + "<a href='/to_excel/devices?search=%s'> export to excel</a> or <a href='/page_add'> add device</a> " %(search)
    if title_link == "":
        title_link = "id/Count/Stock/Fail/Share/Interface/Part_number/Other"
    titles=[]
    for title in get_titles(title_link):
        href = "" 
        if title["name"] == "id":
            href = "/edit"
        if title["name"] == "Count":
            href = "/attached"
        if title["name"] == "Part_number":
            href = "/share"
        if title["name"] == "Stock":
            href = "/device_history"
        titles.append({"name":title["name"],"class":title["class"],"href":href})
    other_title = get_other_title(db_devices(),titles)
    return render_template('home.html',titles=titles,devices=devices,msg=msg,action="/",search=search,other_title=other_title) 
def get_board_serials(email):
    platforms = to_dicts(db_platform(),get_devices(db_platform(),search=email))
    board_serials = [ "%s:%s" %(e['id'],e['Serial_Number']) for e in platforms]
    return board_serials
@app.route("/share/<path:id>", methods=['POST', 'GET'])
def share(id):
    msg="share id = %s" %(id)
    device=get_devices_main(db_devices(),id=int(id))
    if device == None:
        return render_template('error.html',msg="INVALID ID") 
    element = "Index,Count,Stock,Fail,Share,Part_number,Info".split(",")
    email = ','.join(get_user(request))
    board_serials = get_board_serials("")
    h_attached = attached(id)
    return render_template('share.html',email=email,board_serials=board_serials,msg=msg,len=len(device),device=device,element=element,h_attached=h_attached)

def check_ip_alive(ip):
    if ip == "" :
        return False
    try:
        socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        ret = socket_obj.connect_ex(("%s" %(ip),22))
        socket_obj.close()
        if ret == 0 :
            return True
    except:
        pass
    return False
@app.route('/check_platform_alive/<path:ip>')
def check_platform_alive(ip):
    return str(check_ip_alive(ip))
@app.route("/test_panel", methods=['POST', 'GET'])
def test_panel():
    return render_template('test_panel.html',msg="test_panel",ws_ip=args.ws_ip)
@app.route("/add_platform", methods=['POST', 'GET'])
def add_platform():
    try:
        id = sql_db(db_platform(),select_max="id")
        if id == None:
            id = 0
        index = int(id) +  1
        return redirect("/add_platform_id/%d" %(index))
    except:
        return render_template('error.html',msg="INVALID ID") 
def get_datalist(db,platforms):
    datalist = OrderedDict()
    for e in db_element(db):
        _datalist = []
        for platform in platforms:
            if (platform[e] in _datalist) == False:
                _datalist.append(platform[e])
        datalist[e] = _datalist
    return datalist

def set_platform(platform_dict):
    if platform_dict == None:
        return False
    try:
        value = [platform_dict[e] for e in platform_dict]
        sql_db(db_platform(),value=value,id=platform_dict['id'])
        return True
    except:
        return False
def get_platform_id(id):
    try:
        platform = sql_db(db_platform(),id=id)[0]
        return platform
    except:
        return None
def save_platform_history(request,platform_edit,id):
    platform = get_platform_id(id)
    if platform == None:
        return False
    platform = [e for e in platform]
    for i in range(0,len(platform)):
        if str(platform[i]) != str(platform_edit[i]):
            noti_platform_edit(request,platform,platform_edit,id)
            db = db_platform_history(platform[0])
            platform[0] = id_by_time()
            sql_db(db,platform)
            return True
    return False

def noti_platform_edit(request,platform,platform_edit,id):
    title = "%snoti_platform_edit" %(args.db_group)
    body = ""
    platform = to_dict(db_platform(), platform)
    platform_edit = to_dict(db_platform(), platform_edit)
    for e in platform:
        if str(platform[e]) == str(platform_edit[e]):
            body = "%s%s: %s --> %s <br>" %(body,e,platform[e],platform_edit[e])
        else:
            body = "%s%s: %s --> %s <br>" %(body,e,platform[e],color(platform_edit[e]))
    body = body + "\n USER %s IP %s ADMIN %s" %(','.join(get_user(request)),request.remote_addr,is_admin(request))
    body = body.replace("\n", "<br>")
    email_list_all = to_email_list("%s,%s" %(platform['email'],platform_edit['email']))
    send_email_th(email_list_all,title,body,attachment_location="")
    
@app.route("/platform_history/<path:id>", methods=['POST', 'GET'])
def platform_history(id):
    db = db_platform_history(id)
    search = get_search(request)
    platform_history = get_devices(db,search=search)
    platform = sql_db(db_platform(),id=id)[0]
    platform_history.append(platform)
    dbs=to_dicts(db,platform_history)
    msg = welcome("platform_history",request,search,dbs)
    title_link = '/'.join(db_element(db))
    titles=[]
    for title in get_titles(title_link):
        href = "" 
        titles.append({"name":title["name"],"class":title["class"],"href":href})
    return render_template('home.html',titles=titles,devices=dbs,msg=msg,action="/",search=search)
def get_log_titles(titles="id:/logs,info,ddr_info,pci_info,cpu_info"):
    _titles=[]
    for e in titles.split(","):
        if e.find(":") == -1:
            name = e
            href = ""
        else:
            name = e.split(":")[0]
            href = e.split(":")[1]
        _titles.append({"name":name,"href":href})
    return _titles
def grep(_str,pwd,O="-h"):
    c = "grep %s '%s' -R '%s'" %(O,_str,pwd)
    re = commands.getstatusoutput(c)
    return re
def update_platform_info(platform_id,ddr_info,pci_info,cpu_info):
    try:
        platform_infos = sql_db(db_platform_info(platform_id),where="limit 1")
        if len(platform_infos) != 0:
            platform_info = platform_infos[0]
            print "read platform_info %s" %(str(platform_info))
            if ddr_info == "":
                ddr_info = str(platform_info[1])
            if pci_info == "":
                pci_info = str(platform_info[2])
            if cpu_info == "\n":
                cpu_info = str(platform_info[3])
            if ddr_info != str(platform_info[1]) or pci_info != str(platform_info[2]) or cpu_info != str(platform_info[3]):
                print "write platform_info %s" %([platform_id,ddr_info,pci_info,cpu_info,now()])
                sql_db(db_platform_info(platform_id), [platform_id,ddr_info,pci_info,cpu_info,now()], id=platform_id)
        else:
            print "write platform_info %s" %([platform_id,ddr_info,pci_info,cpu_info,now()])
            sql_db(db_platform_info(platform_id), [platform_id,ddr_info,pci_info,cpu_info,now()], id=platform_id)
    except:
        traceback.print_exc()
    pass
def logfa(pwd,is_wr_db):
    re = OrderedDict()
    re["id"] = pwd.replace("logs/","")
    if os.path.getsize(pwd) < 1024*1024:
        v =  grep("__start__",pwd,"-h")[1]
        cli_argv = find_in(v, "__start__CLI ARGV", "__end__")
        ddr_info = find_in(v, "__start__DDR_INFO", "__end__").replace("_", " ")
        pci_info = find_in(v, "__start__PCI_INFO", "__end__")
        cpu_info = find_in(v, "__start__CPU_INFO", "__end__") +"\n"+ find_in(v, "__start__CPU_TYPE", "__end__")
        
        status_summary = find_in(v, "__start__STATUS SUMMARY", "__end__")
        if status_summary == "":
            status_summary = "UNKNOW"
        status = "UNKNOW"
        fail_count = v.count("FAIL")
        pass_count = v.count("PASS")
        if pass_count != 0:
            status = color("PASS %s" %(pass_count),"blue")
        if fail_count != 0:
            status = color("FAIL %s" %(fail_count),"red")
        re["info"] = "cli_argv %s <br>status %s <br>status_summary %s" %(cli_argv,status,status_summary)
        re["ddr_info"] = ddr_info
        re["pci_info"] = pci_info
        re["cpu_info"] = cpu_info
        
        if is_wr_db:
            platform_id = int(re["id"].split("/")[0])
            update_platform_info(platform_id,ddr_info,pci_info,cpu_info)
    else:
        re["info"] = "skip big file"
        re["ddr_info"] = ""
        re["pci_info"] = ""
        re["cpu_info"] = ""
    return re
def logfas(pwd):
    logs = []
    listdirs = os.listdir(pwd)
    is_wr_db = True
    for i,listdir in enumerate(reversed(listdirs)):
            listdir = "%s/%s" %(pwd,listdir)
            if os.path.isdir(listdir) or i > 20:
                continue
            logs.append(logfa(listdir,is_wr_db))
            is_wr_db = False
    return logs
@app.route("/add_platform_id/<path:id>", methods=['POST', 'GET'])
def add_platform_id(id):
    msg="add_platform id = %s len %s" %(id,len(request.form))
    if len(request.form) != 0:
        platform_request = [ascii(request.form[e]) for e in db_element(db_platform())]
        platform = to_dict(db_platform(),get_devices(db_platform(),id=id))
            
        save_files(request,id)
        if (platform != None) and (is_admin(request) == False):
            for e in ["Board_Rev","email","Team","Name","Location","Serial_Number","Chassis_SN","System_Type","Board_Rev"]:
                if platform != None and platform[e] != request.form[e]:
                    return render_template('error.html',msg="INVALID %s. Your is not admin!" %(e))
        save_platform_history(request,platform_request, id)
        sql_db(db_platform(),platform_request, id)
        
    platform = to_dict(db_platform(),get_devices(db_platform(),id=id))
    if platform == None:
        platform = to_dict(db_platform(),["" for e in db_element(db_platform())])
        platform["id"] = id
        platform["client_info"] = request.remote_addr
        platform["time"] = now()


    platforms = to_dicts(db_platform(),get_devices(db_platform()))
    datalist = get_datalist(db_platform(),platforms)

    try:
        _user = get_user(request)[0]
    except:
        _user =""
            
    board_cfg = OrderedDict()
    board_cfg['bmc_fw'] = cfg_file("cfg/bmc_fw/",_user)
    board_cfg['atfbios_fw'] = cfg_file("cfg/atfbios_fw/",_user)
    board_cfg['scp_fw'] = cfg_file("cfg/scp_fw/",_user)
    
    board_cfg['nvparm_board_setting'] = cfg_file("cfg/nvparm_board_setting/",_user)
    board_cfg['user_cfg1'] = cfg_file("cfg/user_cfg1/" ,_user)
    board_cfg['user_cfg2'] = cfg_file("cfg/user_cfg2/" ,_user)
    
    board_cfg['test_cfg'] = cfg_file("cfg/test_cfg/",_user)
    board_cfg['nvparm'] = cfg_file("cfg/test_nvparm/",_user)
    board_cfg['cmd'] = [open_file(e) for e in cfg_file("cfg/cmd/",_user)]

    
    log_titles=get_log_titles()
    log_pwd = "logs/%s" %(platform['id'])
    try:
        log_elements = logfas(log_pwd)
    except:
        log_elements = []
    
    try:
        test_cfg = to_dict(db_test_cfg(id),sql_db(db_test_cfg(id),id=1)[0])
    except:
        test_cfg = OrderedDict()
    return render_template('add_platform.html',id=id,msg=msg,platform=platform,datalist=datalist,board_cfg=board_cfg,log_pwd=log_pwd,log_elements=log_elements,log_titles=log_titles,ws_ip=args.ws_ip,test_cfg=test_cfg) 
def get_id_shared(platforms):
    id_shared = {}
    for platform in platforms:
        i = 1
        _id_shared = "<br>"
        platform_devices = sql_db(db_platform_devices(),where="WHERE platform_id='%s'" %(platform['id']))
        #print platform_devices
        if platform_devices != None:
            for e in platform_devices:
                devices_shared = sql_db(db_shared(),id=e[0])
                for device_shared in devices_shared:
                    number=device_shared[get_db_index("number",db_shared())]
                    part_number = device_shared[get_db_index("Part_number",db_shared())]
                    email = device_shared[get_db_index("email",db_shared())]
                    _id_shared = "%s %s - %s<br>" %(_id_shared,i,href("x%s %s %s" %(number,part_number,email),"/page_shared_submit/%s" %(e[0])))
                    i = i + 1
                    #print _id_shared
        id_shared.update({platform['id']:_id_shared})
    return  id_shared
def get_db_platform_devices(id):
    try:
        platform_device = sql_db(db_platform_devices(),id=id)
        platform_device = to_dict(db_platform_devices(),platform_device[0])
        return platform_device["device_id"]
    except:
        return ""

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
@app.route("/download/<path:f>", methods=['POST', 'GET'])
def download(f):
    print "download %s ..." %(f)
    return send_file(f, as_attachment=True,cache_timeout=0)

def save_xlsx(request,type=""):
    import xlsxwriter
    f = "static/xls/%s_%s.xlsx" %(type,now())
    workbook = xlsxwriter.Workbook(f)
    worksheet = workbook.add_worksheet()
    search = get_search(request)
    if type == "platforms":
        dbs = to_dicts(db_platform(),get_devices(db_platform(),search=search,is_map=True))
    elif type == "devices":
        dbs = to_dicts(db_devices(),get_devices(db_devices(),search=search))
    elif type == "shared":
        dbs = to_dicts(db_shared(),get_devices(db_shared(),search=search))
    else:
        return False,"type %s unsupported" %(type)
    if dbs == None:
        return False,"type %s database is None" %(type)
    i = 0
    for col_num,data in enumerate(["filter",search]):
        worksheet.write(i, col_num,data)
    for db in dbs:
        i = i + 1
        if i == 1:
            for col_num,data in enumerate([e for e in db]):
                worksheet.write(i, col_num,data)
            i = i + 1
        for col_num, data in enumerate([db[e] for e in db]):
            worksheet.write(i, col_num, data)
            worksheet.set_column(i, col_num, 25)
    workbook.close()
    return True,f
@app.route("/to_excel/<type>", methods=['POST', 'GET'])
def to_excel(type):
    re = save_xlsx(request,type)
    if re[0] == False:
        return re[1]
    else:
        return send_file(re[1], as_attachment=True,cache_timeout=0)
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


def get_import_log_href(id,request):
    f_pwd = ""
    if "html_link" in request.form:
        href_link = request.form["html_link"]   
        if href_link != "":
            f_pwd = "%s/%s/%s" %(args.upload_dir,id,os.path.basename(href_link))
            exec_cmd("mkdir -p %s " %(os.path.dirname(f_pwd)))
            print exec_cmd("wget %s -O %s" %(href_link,f_pwd))
    return f_pwd

@app.route("/platforms", methods=['POST', 'GET'])
def platform_def():
    return platforms("id/Team/Serial_Number/System_Type/Board_Rev/email/Task/Note/Board_Status")
@app.route("/platforms/<path:link>", methods=['POST', 'GET'])
def _platforms(link):
    return platforms(link)
@app.route("/platforms_map", methods=['POST', 'GET'])
def platforms_map():
    return platforms("id/Team/Serial_Number/System_Type/Board_Rev/email/Task/Note/Board_Status",is_map=True,action="/platforms_map")
@app.route("/platforms_map/<path:link>", methods=['POST', 'GET'])
def _platforms_map(link):
    return platforms(link,is_map=True,action="/platforms_map")
def platforms(link,is_map=False,action="/platforms"):
    search = get_search(request)
    is_check_alive = False
    if search.find("alive")!=-1:
        search = search.replace("alive", "")
        is_check_alive = True
    platforms = to_dicts(db_platform(),get_devices(db_platform(),search=search,is_map=is_map))
    msg = welcome("platforms",request,search,platforms)
    msg = msg + "<a href='/to_excel/platforms?search=%s'> export to excel</a> or <a href='/add_platform'> add new platforms</a>" %(search)
    
    titles=[]
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
        titles.append({"name":title["name"],"class":title["class"],"href":href})

    return render_template('platforms.html',platforms=platforms,msg=msg,action="%s/%s" %(action,link),search=search,titles=titles,is_check_alive=is_check_alive) 

def chart_data(value,dicts):
    re = OrderedDict()
    for e in dicts:
        if e[value] in re:
            re[e[value]] = re[e[value]] + 1
        else:
            re[e[value]] = 1        
    return re

@app.route("/platforms_chart/<path:chart_titles>", methods=['POST', 'GET'])
def platforms_chart(chart_titles):
    search = get_search(request)
    platforms = to_dicts(db_platform(),get_devices(db_platform(),search=search))  
    msg = welcome("platforms_chart",request,search,platforms)
    charts_data = OrderedDict()
    for chart_title in chart_titles.split("/"):
        if chart_title == "":
            continue
        charts_data["%s" %(chart_title)] = chart_data(chart_title,platforms)
    return render_template('chart.html',charts_data=charts_data,msg=msg,action="/platforms_chart/%s" %(chart_titles),search=search,titles="platforms_chart") 
@app.route("/device_chart/<path:chart_titles>", methods=['POST', 'GET'])
def device_chart(chart_titles):
    search = get_search(request)
    devices = to_dicts(db_devices(),get_devices(db_devices(),search=search))
    msg = welcome("platforms_chart",request,search,devices)
    charts_data = OrderedDict()
    for chart_title in chart_titles.split("/"):
        if chart_title == "":
            continue
        charts_data["%s" %(chart_title)] = chart_data(chart_title,devices)
    return render_template('chart.html',charts_data=charts_data,msg=msg,action="/device_chart/%s" %(chart_titles),search=search,titles="device_chart") 
@app.route("/share_chart/<path:chart_titles>", methods=['POST', 'GET'])
def share_chart(chart_titles):
    search = get_search(request)
    devices = to_dicts(db_shared(),get_devices(db_shared(),search=search))
    msg = welcome("platforms_chart",request,search,devices)
    charts_data = OrderedDict()
    for chart_title in chart_titles.split("/"):
        if chart_title == "":
            continue
        charts_data["%s" %(chart_title)] = chart_data(chart_title,devices)
    return render_template('chart.html',charts_data=charts_data,msg=msg,action="/share_chart/%s" %(chart_titles),search=search,titles="device_chart") 

def gen_qr():
    try:
        import qrcode
        devices = sql_db(db_devices())
        exec_cmd("mkdir -p static/qr")
        for e in devices:
            try:
                part_number = e[get_db_index("Part_number",db_devices())]
                if os.path.exists("static/qr/%s.png" %(part_number)) == False:
                    print "gen qr %s" %(part_number)
                    os.system("mkdir -p static/qr/%s" %(os.path.dirname(part_number)))
                    qrcode.make(part_number).save("static/qr/%s.png" %(part_number))
            except:
                print traceback.print_exc()
                continue
    except:
        pass
@app.route("/request_submit/<path:id>", methods=['POST', 'GET'])
def request_submit(id):
    msg="Welcome to request_submit id = %s" %(id)
    submit_id =  id_by_time() 
    email = request.form["email"].replace("@amperecomputing.com","")
    number = request.form["number"]
    board_id = request.form["board_serial"].split(":")[0]
    if board_id != "":
        platform = to_dict(db_platform(),get_platform_id(board_id))
        #if platform == None or platform['email'] != email:
        if platform == None:
            return render_template('error.html',msg="INVALID board_serial/email %s" %(board_id))  
    note = request.form["note"]
    if note!="":
        note = "REQUEST %s: %s x%s board_serial %s\n" %(now(),note,number,request.form["board_serial"]) 
    
    device=get_devices_main(db_devices(),id=int(id))
    if device == None:
        return render_template('error.html',msg="INVALID ID") 
    
    if email == "" or number == "" or (number.isnumeric() == False) or note =="":
        msg = msg + " Error miss info <br> email='%s' number='%s' note='%s'" %(email,number,note)
        element = "Index,Count,Stock,Fail,Share,Part_number,Info".split(",")
        return render_template('share.html',msg=msg,len=len(device),device=device,element=element) 
    part_number = device[5]
    info = device[6]
    client_info = request.remote_addr
    time = now()
    value = [submit_id,id,email,part_number,number,note,info,client_info,time]
    sql_db(db_request(),value=value)
    
    if board_id != "":
        sql_db(db_platform_devices(),[submit_id,board_id])

    f_pwd = save_files(request,pwd = "devices/%s" %(id),fname = "request_%s" %(submit_id))
    email_request(request,db_request(),value,f_pwd)

    return redirect("/submit_info/%s" %(id))
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
@app.route("/send_noti/<path:id>", methods=['POST', 'GET'])
def send_noti(id):
    msg = "send_noti"
    if  is_admin(request) == False:
        return render_template('error.html',msg="Your is not admin")
    device = get_devices(db_shared(),id=id)
    if device == None:
        return render_template('error.html',msg="INVALID ID") 
    return render_template('send_noti.html',msg=msg,device=device,count_days=count_days(str(device[0])))
@app.route("/send_noti_action/<path:id>", methods=['POST', 'GET'])
def send_noti_action(id):
    if  is_admin(request) == False:
        return render_template('error.html',msg="Your is not admin")
    device = get_devices(db_shared(),id=id)
    if device == None:
        return render_template('error.html',msg="INVALID ID")
    email_noti(db_shared(),device,request.form['email'],request.form['email_body'])  
    return redirect("/page_shared")
def send_email_register(email,passw):
    title = "%sRegister board manager page" %(args.db_group)
    body = "Hi %s!\n" %(email)
    body = "%sYour key is %s!\n" %(body,href(passw,"/login/" + email +"/"+ passw))
    if email.find("@") == -1:
        email = email + "@amperecomputing.com"
    send_email_th(email,title,body)
@app.route("/login/<email>/<passw>", methods=['POST', 'GET'])
def login(email,passw):  
    db = db_user()
    user = sql_db(db,where="WHERE email='%s'" %(email))[0]
    if user[get_db_index("passw",db)] == passw:
        value = [e for e in user]
        value[get_db_index("ip",db)] = value[get_db_index("ip",db)] +"," + request.remote_addr
        sql_db(db, value=value, where="WHERE email='%s'" %(email))
        login_user(user=User(email), remember=True)
        return redirect("/")
    else:
        return render_template('error.html',msg="INVALID KEY") 
@app.route("/register", methods=['POST', 'GET'])
def register():
    email = ""
    for e in request.form:
        if e == "email" and request.form[e] !="":
            email = request.form[e]
            email = email.split("@")[0]
    if email != "":
        passw = id_by_time()
        value = [email,passw,""]
        sql_db(db_user(),value,where="WHERE email='%s'" %(email))
        send_email_register(email,passw)
        msg = "Your key is send ... %s" %(email)
        return render_template('register.html',msg=msg)
    else:
        msg = "Welcome page register for your key!"
        return render_template('register.html',msg=msg)
def div_s(ext_class=""):
    h = "<div class='w3-container %s'>" %(ext_class)
    return h
def div_e():
    return "</div>"
def html(p,ext_class="",style=""):
    return "%s<span style='%s'>%s</span>%s" %(div_s(ext_class),style,p,div_e())
def log_fa(log,key="\n"):
    msg = ""
    for e in log.split(key):
        if e.find("<") == 0:
            msg = msg + e
        else:
            msg = msg + html(e,ext_class="raw_log")
    return msg
@app.route('/logs',methods=['POST', 'GET'])
def logs():
    return _open_sys_log("",request)
@app.route('/logs/<path:logfile>', methods=['POST', 'GET'])
def open_sys_log(logfile):
    return _open_sys_log(logfile,request)
@app.route('/logs//<path:logfile>', methods=['POST', 'GET'])
def open_sys_log2(logfile):
    return _open_sys_log(logfile,request)
def dir_filter(pwd,dirs,search):
    if search == "" or search == None:
        return dirs
    dirs_filter = []
    for d in dirs:
        append = True
        for s in search.split(","):
            re = commands.getstatusoutput("grep %s -R %s/%s" %(s,pwd,d))
            if re[0] != 0:
                append = False
                break
        if append:
            dirs_filter.append(d)
    return dirs_filter
def _open_sys_log(logfile,request):
    search = get_search(request)
    pwd = "logs/" + logfile
    if os.path.isdir(pwd):
        dirs=reversed(os.listdir(pwd))
        return render_template('dir.html',dirs=dir_filter(pwd,dirs,search),pwd=pwd,filter=search)
    logtext = ascii(open_file("%s" %(pwd)))
    logtext = logtext.replace("<DEL", "[DEL").replace("<ESC", "[ESC")
    
    return render_template('logs.html',logfile=pwd,logtext=log_fa(logtext))
def get_nvparam_define(f = "nvparam_define.h"):
    NVPARAM=OrderedDict()
    offset = 0;
    for e in open_file(f).split("\n"):
        try:
            nv_ = find_in(e,"NV_",",",A=3,B=1)
            if nv_ != "":
                name = find_in(nv_,"NV_","\t")
                if name == "":
                    name = find_in(nv_,"NV_"," ")
                value_str = find_in(nv_,"(",")")
                value = 1
                if value_str =="":
                    value_str = find_in(nv_,"= ",",")
                if value_str != "":
                    v = value_str.split("*")
                    for i in v:
                        value = int(i,0)*value
                if name == "PREBOOT_PARAM_START":
                    offset = value | 0x110000
                    continue
                elif name == "MANU_PARAM_START":
                    offset = value | 0x110000
                    continue
                elif name == "USER_PARAM_START":
                    offset = value | 0x110000
                    continue
                elif name == "BOARD_PARAM_START":
                    offset = (value | 0x5F0000) -(0xC000)
                    continue
                value = value + offset
                if name !="" and value != 1:
                    NVPARAM[name] = value
        except:
            #traceback.print_exc()
            pass
    return NVPARAM

@app.route("/action_nvparam", methods=['GET'])
def action_nvparam():
    nv=get_nvparam_define()
    bmcip =""
    nvparm_cmd = ""
    for args in request.args:
        if args == "bmcip" and request.args[args] !="":
            bmcip = request.args[args]
        elif args == "nvparm_configs" and request.args[args] !="":
            nvparm_configs = open_file(request.args[args])
            for e in nvparm_configs.split("\n"):
                if e == "":
                    continue
                ee = e.split(" ")
                name = ee[0]
                if len(ee) == 2:
                    value = ee[1]
                    nvparm_cmd = nvparm_cmd + "echo %s && nvparm -s %s -o 0x%x &&" %(name,value,nv[name])
                else:
                    nvparm_cmd = nvparm_cmd + "%s" %(e)
        elif request.args[args] != "":
            nvparm_cmd = nvparm_cmd + "echo %s && nvparm -s %s -o 0x%x &&" %(args,request.args[args],nv[args])

    if bmcip =="":
        msg = "Need BMCIP"
    elif nvparm_cmd =="":
        msg = "Need NVPARM value"
    else:
        for board in g_boards:
            ssh_pass = "sshpass -p %s ssh -o StrictHostKeyChecking=no -t %s@%s '%s&&%s&&%s'" %(board['bmc_pass'],board['bmc_user'],bmcip,board['cmd_before'],nvparm_cmd,board['bmc_after'])
            if os.path.exists("./sshpass"):
                ssh_pass = "./" + ssh_pass
            re = exec_cmd(ssh_pass)
            if re[0] == 0:
                msg = ssh_pass
                break
            else:
                msg = ssh_pass + " " + re[1]
    email = ','.join(get_user(request))
    platforms = to_dicts(db_platform(),get_devices(db_platform(),search=email))
    bmc_list = [e['bmcip'] for e in platforms]
    return render_template('nvparm.html',\
                           bmc_list=bmc_list,\
                           nvparm_configs=cfg_file("cfg/nvparm/"),\
                           nv=get_nvparam_define(),msg=msg)
@app.route("/nvparm")
def nvparm():
    msg="Welcome to nvparm tools"
    email = ','.join(get_user(request))
    platforms = to_dicts(db_platform(),get_devices(db_platform(),search=email))
    bmc_list = [e['bmcip'] for e in platforms]
    return render_template('nvparm.html',\
                           bmc_list=bmc_list,\
                           nvparm_configs=cfg_file("cfg/nvparm/"),\
                           nv=get_nvparam_define(),msg=msg)
def encode_cfg(e):
    re = e.replace("6.^","/").replace("^.^"," ").replace("^.6","\n")
    if re == "None":
        return ""
    else:
        return re
def load_cfg(e):
    e = encode_cfg(e)
    #if os.path.exists(e) and os.path.getsize(e) < 8*1024:
    #    e = open_file(e)
    return e
def test_args(f,arg):
    c = f
    for e in arg:
        if arg[e] =="" or arg[e] =="None":
            continue
        else:
            c = "%s --%s %s" %(c ,e,arg[e])
    print c
    return c
def platforms_map_ttyid(ttyids):
    re = ""
    platforms = to_dicts(db_platform(),get_devices(db_platform()))
    for ttyid in ttyids.split(","):
        re = "%s%s" %(re,ttyid)
        for platform in platforms:
            e = [platform[e] for e in platform]
            if ttyid in e:
                re = "%s[%s-%s]" %(re,platform['id'],platform['Serial_Number'])
        re = "%s," %(re)
    return re
def format_log_xconsole(e):
    if e.find("' ") != -1:
        return e.split("' ")[1]
    return e.replace("\r","")
def get_host_user(logs,keys=["hostuser ","hostpass "," tty"]):
    data = {}
    for log in logs.split("\n"):
        for key in keys:
            re = find_in(log,key,"")
            key = key.replace(" ","")
            if re != "":
                if (key in data) == True:
                    data[key] = "%s,%s" %(data[key] , format_log_xconsole(re))
                else:
                    data[key] = (format_log_xconsole(re))
    if "tty" in data:
        data['tty'] = platforms_map_ttyid( data['tty'] )
    return data
def format_json(arg):
    j = "{"
    for e in arg:
        if arg[e] !="":
            j = "%s\"%s\":\"%s\"," %(j,e,arg[e])
    if len(j) > 1:
        j = j[0:len(j) -1]
    j = "%s}" %(j)
    return j 
def ssh_pass(P="None",U=None,H=None,C=""):
    C = C.replace("./ipmitool","ipmitool")
    c = "sshpass -p %s ssh -o StrictHostKeyChecking=no -t %s@%s '%s'" %(P,U,H,C)
    if os.path.exists("./sshpass"):
        c = "./" + c
    return c
@app.route("/scanip", methods=['POST', 'GET'])    
def scanip():
    search = get_search(request)
    msg = "scanip %s" %(search)
    pwd = "logs/scanip"
    dirs=os.listdir(pwd)
    try:
        scanip = request.form['scanip']
        if scanip != "":
            log = "scanip_%s_%s.log" %(scanip,now())
            c = test_args("./xconsole.py --scanip %s >> %s/%s" %(scanip,pwd,log),{})
            os.system("%s &" %(c))
            msg = msg + href(log, "/%s/%s" %(pwd,log))
    except:
        pass
    return render_template('scanip.html',msg=msg,action="/scanip",search="",titles="scanip",dirs=dir_filter(pwd,dirs,search))
def cKermit(N="Atf",H="127.0.0.1",U="root",P="root",T="ttyUSB0"):
    if T.find("tty") == -1:
        x="\"com.amperecomputing.console.enhanceconsole.%sEnhanceConsole\": { \n\
            \t\"JsonTestSetting\": {},\n\
            \t\"Properties\": {\n\
            \t\"Ckermit host\": \"%s\",\n\
            \t\"Ckermit user\": \"%s\",\n\
            \t\"Ckermit password\": \"%s\",\n\
            \t\"Ckermit ttyUSB\": \"/dev/ttyUSB6969\",\n\
            \t\"Ckermit ttyUSB ID\": \"%s\",\n\
            \t\"Console class\": \"com.amperecomputing.console.CkermitConsole\",\n\
            \t\"Ckermit force to use ttyUSB\": \"true\",}}," %(N,H,U,P,T)
    else:
        x="\"com.amperecomputing.console.enhanceconsole.%sEnhanceConsole\": { \n\
            \t\"JsonTestSetting\": {},\n\
            \t\"Properties\": {\n\
            \t\"Ckermit host\": \"%s\",\n\
            \t\"Ckermit user\": \"%s\",\n\
            \t\"Ckermit password\": \"%s\",\n\
            \t\"Ckermit ttyUSB\": \"/dev/%s\",\n\
            \t\"Console class\": \"com.amperecomputing.console.CkermitConsole\",\n\
            \t\"Ckermit force to use ttyUSB\": \"true\",}}," %(N,H,U,P,T)
    return x
def SSH(N="Cli",H="127.0.0.1",U="root",P="root"):
    x="\"com.amperecomputing.console.enhanceconsole.%sEnhanceConsole\": { \n\
        \t\"JsonTestSetting\": {},\n\
        \t\"Properties\": {\n\
        \t\"SSH host\": \"%s\",\n\
        \t\"SSH user\": \"%s\",\n\
        \t\"SSH password\": \"%s\",\n\
        \t\"Console class\": \"com.amperecomputing.console.SshConsole\",\n\
        }}," %(N,H,U,P)
    return x
def SOL(N="Bmc",H="127.0.0.1",U="ADMIN",P="ADMIN",I="0"):
    x="\"com.amperecomputing.console.enhanceconsole.%sEnhanceConsole\": { \n\
        \t\"JsonTestSetting\": {},\n\
        \t\"Properties\": {\n\
        \t\"SOL host\": \"%s\",\n \
        \t\"SOL user\": \"%s\",\n \
        \t\"SOL password\": \"%s\",\n \
        \t\"SOL instance\": \"%s\",\n \
        \t\"Console class\": \"com.amperecomputing.console.SolConsole\",\n\
        }}," %(N,H,U,P,I)
    return x

def platform_console(board,hostip,hostuser,hostpass,bmcip,tty_uefi,tty_atf,tty_s0cli,tty_s1cli,tty_bmc):
    g_boards = []
    g_boards.append({"board":"jade","bmc_user":"root","bmc_pass":"root","U":"ADMIN","P":"ADMIN"})
    g_boards.append({"board":"snow","bmc_user":"sysadmin","bmc_pass":"superuser","U":"admin","P":"password"})
    g_boards.append({"board":"collins","bmc_user":"sysadmin","bmc_pass":"superuser","U":"admin","P":"admin"})
    U="ADMIN"
    P="ADMIN"
    bmc_user="root"
    bmc_pass="root"
    for g_board in g_boards:
        if board.lower().find(g_board['board']) != -1:
            U=g_board["U"]
            P=g_board["P"]
            bmc_user=g_board["bmc_user"]
            bmc_pass=g_board["bmc_pass"]
    sol_uefi = "1"
    sol_s0cli = "2"
    sol_atf = '3'
    sol_s1cli = '4'
    js = ""
    js +="{"
    if hostip != "" and (tty_atf != None) and (len(tty_atf) > 4):
        js += cKermit("Atf",hostip,hostuser,hostpass,"%s" %(tty_atf))
    else:
        js += SOL("Atf",bmcip,U,P,sol_atf)
    if hostip != "" and (tty_s0cli != None) and len(tty_s0cli) > 4:
        js += cKermit("Cli",hostip,hostuser,hostpass,"%s" %(tty_s0cli))
    else:
        js += SOL("Cli",bmcip,U,P,sol_s0cli)
        
    if hostip != "" and (tty_s1cli != None) and len(tty_s1cli) > 4:
        js += cKermit("S1Cli",hostip,hostuser,hostpass,"%s" %(tty_s1cli))
    else:
        js += SOL("S1Cli",bmcip,U,P,sol_s1cli)   
               
    if hostip != "" and (tty_bmc != None) and len(tty_bmc) > 4:
        js += cKermit("Bmc",hostip,hostuser,hostpass,"%s" %(tty_bmc))
    else:
        js += SSH("Bmc",bmcip,bmc_user,bmc_pass)

    if hostip != "" and (tty_uefi != None) and len(tty_uefi) > 4:
        js += cKermit("Linux",hostip,hostuser,hostpass,"%s" %(tty_uefi))
    else:
        js += SOL("Linux",bmcip,U,P,sol_uefi)
    js +="}"
    return js
def get_cfg_file(request):
    try:
        _user = get_user(request)[0]
    except:
        _user =""
    configs = []    
    configs.extend(cfg_file("cfg/test_cfg/",_user)) 
    configs.extend(cfg_file("cfg/test_nvparm/",_user))
    configs.extend(cfg_file("cfg/cmd/",_user))
    configs.extend(cfg_file("cfg/test_script/",_user))
    configs.extend(cfg_file("cfg/user_cfg1/" ,_user))
    configs.extend(cfg_file("cfg/user_cfg2/" ,_user))
    return  configs 
@app.route('/get_file/<path:subpath>')
def get_file(subpath):
    return open_file(subpath)
@app.route("/cfg_edit", methods=['GET'])
def cfg_edit():
    msg = "welcome cfg edit"
    if "configs" in request.args and (request.args["configs"]) != "":
        if "args" in request.args:
            os.system("rm -rf " + (request.args["configs"]))
            if (request.args["args"]) != "":
                wrlog((request.args["args"]), (request.args["configs"]))
            msg = "configs " + (request.args["configs"]) + " " + (request.args["args"])
    return render_template('cfg_edit.html',msg=msg,configs=get_cfg_file(request),action="/cfg_edit")
@app.route("/console/<path:id>", methods=['POST', 'GET'])    
def console(id):
    p = to_dict(db_platform(),get_devices(db_platform(),id=id))
    return platform_console(p['System_Type'],p['hostip'],p['hostuser'],p['hostpass'],p['bmcip'],p['tty_uefi'],p['tty_atf'],p['tty_s0cli'],p['tty_s1cli'],p['tty_bmc'])
@app.route('/kill/<path:pid>')
def kill(pid):
    #os.system("kill -9 %s" %(pid))
    c = "kill -9 %s" %(pid)
    c = ssh_pass(H="10.38.13.102",U="amcclab",P="amcc1234",C=c)
    os.system("%s &" %(c))
    return "killed"
def save_test_cfg(ajax):
    db = db_test_cfg(ajax['id'])
    value = []
    for e in db_element(db):
        if e == "id":
            value.append(1)
        else:
            value.append(ajax[e])
    sql_db(db=db, value=value,id=1)
@app.route("/ajax_request/<path:paths>", methods=['POST', 'GET'])    
def ajax_request(paths):
    ajax = OrderedDict()
    keys = ["req","id","hostip","hostuser","hostpass","hostport","bmc_fw","scp_fw","atfbios_fw","test_cfg","nvparm","cmd","nvparm_board_setting","user_cfg1","user_cfg2"]
    for i in range(0,len(keys)):
        ajax[keys[i]] = load_cfg(paths.split("/")[i])
    platform_args = OrderedDict()
    try:
        platform = to_dict(db_platform(),get_devices(db_platform(),id=ajax['id']))
        #if is_valid_user(platform['email'],request) == False:
        #    json = {"request":"%s" %(ajax["req"]),"msg":"is_valid_user %s != %s" %(platform['email'],str(get_user(request)))}
        #    return format_json(json).replace("\r", "").replace("\n", "<br>")
        platform_args['hostip'] = platform['hostip']
        platform_args['hostuser'] = platform['hostuser']
        platform_args['hostpass'] = platform['hostpass']
        platform_args['bmcip'] = platform['bmcip']
        platform_args['tty_bmc'] = platform['tty_bmc']
        platform_args['tty_uefi'] = platform['tty_uefi']
        platform_args['tty_atf'] = platform['tty_atf']
        platform_args['tty_s0cli'] = platform['tty_s0cli']
        platform_args['tty_s1cli'] = platform['tty_s1cli']
        platform_args['board_type'] = platform['System_Type']
        platform_args['board'] = "%s_%s" %(platform['System_Type'],platform['id'])
    except:
        pass
    platform_args['hostip'] = ajax['hostip']
    platform_args['hostuser'] = ajax['hostuser']
    platform_args['hostpass'] = ajax['hostpass']
    
    save_test_cfg(ajax)
    
    if ajax["req"] == "get_host_tty":
        platform_args['list'] ='1'
        c = test_args("./xconsole.py",platform_args)
        re = exec_cmd(c)
        if re[0] == 0:
            data = get_host_user(re[1])
            data['request'] = "%s" %(ajax['req'])
            return format_json(data)
        else:
            return '{"request":"%s","msg":"error: %s"}' %(ajax['req'],c)
    elif ajax["req"] == "get_info":
        platform_args['cmd'] ='fru'
        platform_args['list'] ='0'
        c = test_args("./xconsole.py",platform_args)
        re = exec_cmd(c)
        if re[0] != 0:
            return '{"request":"%s","error":"%s"}' %(request,re[1])  
        json = {"request":"%s" %(ajax["req"]),"msg":re[1]}
        return format_json(json).replace("\r", "").replace("\n", "<br>")
    elif ajax["req"] == "get_board_serial":
        platform_args['cmd'] ='fru'
        platform_args['list'] ='0'
        c = test_args("./xconsole.py",platform_args)
        re = exec_cmd(c)
        if re[0] != 0:
            return '{"request":"%s","error":"%s"}' %(request,re[1])   
        wrlog(re[1],"static/upload/%s/FRU.txt" %(ajax['id']))
        board_serial = find_in(re[1],"Board Serial","\n").replace(" ", "").replace("\n", "").replace(":", "")
        json = {"request":"%s" %(ajax["req"]),"Serial_Number":board_serial}
        return format_json(json).replace("\r", "")
    elif ajax["req"] == "detect_console":
        platform_args['detect_tty'] ="%s,%s,%s,%s,%s" %(platform_args['tty_bmc'],platform_args['tty_uefi'],platform_args['tty_atf'],platform_args['tty_s0cli'],platform_args['tty_s1cli'])
        c = test_args("./xconsole.py",platform_args)
        re = exec_cmd(c)
        if re[0] != 0:
            return '{"request":"%s","error":"%s"}' %(request,re[1])
        bmcip = find_in(re[1],"detect_tty bmcip "," ")
        tty_bmc = find_in(re[1],"detect_tty tty_bmc "," ")
        tty_atf = find_in(re[1],"detect_tty tty_atf "," ")
        tty_uefi = find_in(re[1],"detect_tty tty_uefi "," ")
        tty_s0cli = find_in(re[1],"detect_tty tty_s0cli "," ")
        tty_s1cli = find_in(re[1],"detect_tty tty_s1cli "," ")
        board_serial = find_in(re[1],"Board Serial","\n").replace(" ", "").replace(":", "")
        json = {"request":"%s" %(ajax['req']),"bmcip":bmcip,"tty_bmc":tty_bmc,"tty_atf":tty_atf,"tty_uefi":tty_uefi,"tty_s0cli":tty_s0cli,"tty_s1cli":tty_s1cli,"board_serial":board_serial,"msg":c}
        print format_json(json).replace("\r", "")
        return  format_json(json).replace("\r", "")    
    elif ajax["req"] == "power_reset":
        platform_args['cmd']= 'reset'
        c = test_args("./xconsole.py",platform_args)
        os.system("%s &" %(c))
        return '{"request":"%s","msg":"%s"}' %(ajax['req'],c)
    elif ajax["req"] == "mc_reset":
        platform_args['cmd']= 'mc_reset'
        c = test_args("./xconsole.py",platform_args)
        os.system("%s &" %(c))
        return '{"request":"%s","msg":"%s"}' %(ajax['req'],c)
    elif ajax["req"] == "clean_nvparm":
        platform_args['cmd'] = "cleannv"
        c = test_args("./xconsole.py",platform_args)
        os.system("%s &" %(c))
        return '{"request":"%s","msg":"%s"}' %(ajax['req'],c)
    elif ajax["req"] == "start_test":
        platform_args['bmc_fw'] = ajax['bmc_fw']
        platform_args['scp_fw'] = ajax['scp_fw']
        platform_args['atfbios_fw'] = ajax['atfbios_fw']
        platform_args['nvparm_board_setting'] = ajax['nvparm_board_setting']
        platform_args['test_cfg'] = os.path.basename(ajax['test_cfg'])
        
        test_cmd = "cd %s && ./test_cfg.py" %(os.getcwd())        
        if os.path.exists(ajax['test_cfg']) and os.path.getsize(ajax['test_cfg']) < 8*1024:
            test_cmd = "%s --cfg_file %s " %(test_cmd,ajax['test_cfg'])
        else:
            test_cmd = "%s %s " %(test_cmd,ajax['test_cfg']) 

        for _cfg in ['nvparm','cmd','user_cfg1','user_cfg2']:
            if ajax[_cfg] == "":
                continue
            if os.path.exists(ajax[_cfg]) and os.path.getsize(ajax[_cfg]) < 8*1024:
                test_cmd = "%s %s " %(test_cmd,open_file(ajax[_cfg]))
            else:
                test_cmd = "%s %s " %(test_cmd,ajax[_cfg]) 
                
        test_cmd = test_cmd.replace("\n", " ").replace("\r", "")
        platform_args['wait'] = "0"
        sys_log = "logs/%s/%s_%s.log" %(platform['id'],platform_args['board'],now())
        platform_args['sys_log'] = sys_log
        c = test_cmd + test_args(" ",platform_args) 
        c = ssh_pass(H="10.38.13.102",U="amcclab",P="amcc1234",C=c)
        os.system("%s &" %(c))
        return '{"request":"%s","msg":"%s"}' %(ajax['req'],c)
    elif ajax["req"] == "share_screen":
        platform_args['screen'] = "%s_%s" %(platform['System_Type'],platform['id'])
        c = test_args("./xconsole.py",platform_args)
        c = ssh_pass(H="10.38.13.102",U="amcclab",P="amcc1234",C=c)
        os.system("%s &" %(c))
        msg = ssh_pass(H="10.38.13.102",U="amcclab",P="amcc1234",C="screen -xr %s" %(platform_args['screen']))
        return '{"request":"%s","msg":"%s"}' %(ajax['req'],msg.replace("./", ""))
    else:
        return '{"request":"%s","msg":"%s"}' %(request,"error")
class User():
    def __init__(self, email):
        self.email = email
    authenticated = True
    def is_active(self):
        return True
    def get_id(self):
        return self.email
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
@login_manager.user_loader
def load_user(user_id):
    return user_id
gen_qr()
exec_cmd("mkdir -p static/upload")
exec_cmd("mkdir -p static/qr")
if __name__ == "__main__":
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host= '0.0.0.0',port=args.port)    