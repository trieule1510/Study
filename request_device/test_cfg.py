#!/usr/bin/python
import sys
import os
sys_argv=' '.join([str(e) for e in sys.argv])

def find_in( s, first, last,A=0,B=0):
    try:
        start = s.index( first ) + len( first ) 
        if last == "":
            end = len(s)
        else:
            end = s.index( last, start ) 
        return s[start-A:end + B]
    except ValueError:return ""
def open_file(filename):
    try:
        f = open(filename, "r")
        text=f.read()
        f.close()
        return text;
    except:return ""
def format_cmd(cmd):
    re = ""
    for e in cmd.split(" --"):
        if e == "":
            continue
        if re == "":
            re = e
        elif e.count(" ") == 1:
            re = "%s --%s" %(re,e)
        else:
            _e = e.split(" ")
            re = "%s --%s '%s'" %(re,_e[0],e.replace(_e[0],""))
    print cmd
    print re
    return re
if sys_argv.find("--cfg_file") != -1:
    cfg_file_argv = find_in(sys_argv,"--cfg_file "," ")
    if cfg_file_argv == "":
        cfg_file_argv = find_in(sys_argv,"--cfg_file ","")
        
    cfg_files = cfg_file_argv.split(",")
    for e in open_file(cfg_files[0]).split("\n"):
        e = e.replace("\r", "")
        if e == "" or e[0] == "#":
            continue
        ext_args = sys_argv.replace(cfg_file_argv, "").replace("./test_cfg.py", "").replace(" --cfg_file ", "")
        for i in range(1,len(cfg_files)):
            ext_args = ext_args + " --cfg_file "+ cfg_files[i]
        cmd = "%s %s --test_cfg %s " %(e,ext_args,os.path.basename(cfg_file_argv.replace(",", "_")))
        os.system(format_cmd(cmd))