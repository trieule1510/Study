from flask import Flask,render_template,request
import argparse
import os
import datetime
import commands
import string

app = Flask(__name__)
parser = argparse.ArgumentParser(description='utilities')
parser.add_argument('--port', dest='port',default=2020,type=int,help='port')

args=parser.parse_args()

def now():
    return str(datetime.datetime.today().strftime('%y%m%d%H%M%S%f'))

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

def get_search(request):
    f = ""
    if request.args.get("search")!=None:
        f = request.args.get("search")
    for e in request.form:
        if e == "search" and request.form[e] !="":
            f = request.form[e]
    return f

def ascii(text):
    try:
        return ''.join([x for x in text if x in string.printable])
    except:
        return text

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

def _open_sys_log(logfile, request):
    search = get_search(request)
    pwd = "logs/" + logfile
    if os.path.isdir(pwd):
        dirs = reversed(os.listdir(pwd))
        return render_template('dir.html', dirs=dir_filter(pwd, dirs, search), pwd=pwd, filter=search)
    logtext = ascii(open_file("%s" % (pwd)))
    logtext = logtext.replace("<DEL", "[DEL").replace("<ESC", "[ESC")

    return render_template('logs.html', logfile=pwd, logtext=log_fa(logtext))

def open_file(filename):
    try:
        f = open(filename, "r")
        text = f.read()
        f.close()
        return text;
    except:
        return ""

@app.route('/logs',methods=['POST', 'GET'])
def logs():
    return _open_sys_log("",request)
@app.route('/logs/<path:logfile>', methods=['POST', 'GET'])
def open_sys_log(logfile):
    return _open_sys_log(logfile,request)
@app.route('/logs//<path:logfile>', methods=['POST', 'GET'])
def open_sys_log2(logfile):
    return _open_sys_log(logfile,request)

@app.route("/scan", methods=['POST',])
def scan():
    search = get_search(request)
    pwd = "logs"
    dirs = os.listdir(pwd)
    try:
        scan=request.form['scan']
        print scan
        if scan != "":
            log = "scan_device_%s_%s.log" %(scan,now())
            #c = "./xconsole.py --scan %s >> %s/%s" %(scan,pwd,log)
            c= "./scan_all_info.sh %s >> %s/%s" %(scan,pwd,log)
            os.system("%s " %(c))
    except:
        pass
    return render_template('scan.html',action='/scan', titles='scan', dirs=dir_filter(pwd,dirs,search) )

if __name__== "__main__":
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='0.0.0.0',port=args.port)
