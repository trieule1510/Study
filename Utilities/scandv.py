#!/usr/bin/python

import pexpect
import sys
import os
import argparse
import time
import datetime
import socket
import commands
from sys import *
import threading
from threading import Thread


parser = argparse.ArgumentParser(description='')
parser.add_argument('--ssh', dest='ssh',default="",help='ssh to system')
parser.add_argument('--u', dest='u',default="ADMIN",help='')
parser.add_argument('--p', dest='p',default="ADMIN",help='')
parser.add_argument('--scandv', dest="scandv",default="",help="ip of system")


args = parser.parse_args()

global g_boards
g_boards = []

g_boards.append({"board":"jade",
                 "bmc_user":"root",
                 "bmc_pass":"root",
                 "U":"ADMIN",
                 "P":"ADMIN",})
g_boards.append({"board":"snow",
                 "bmc_user":"sysadmin",
                 "bmc_pass":"superuser",
                 "U":"admin",
                 "P":"password",
                 "bmc_cmd_start":"gpiotool --set-dir-output 139 && gpiotool --set-data-low 139",
                 "bmc_cmd_end":"gpiotool --set-dir-output 139 && gpiotool --set-data-high 139"})
g_boards.append({"board":"collins",
                 "bmc_user":"sysadmin",
                 "bmc_pass":"superuser",
                 "U":"admin",
                 "P":"admin",
                 "bmc_cmd_start":"echo ~",
                 "bmc_cmd_end":"echo ~",
                 "scp_fw_upgrade":"amp_smpmpro_fw_upgrade -p -f"})

def ipmitool(ip=""):
    print "ip1"
    ipmitool = "ipmitool "
    if args.hostport == "":
        ipmitool = ipmitool + "-H "+ ip +" -U %s -P %s" %(args.U,args.P)
    ipmitool = ipmitool + " -I lanplus -z 0x7fff "
    if os.path.exists("./ipmitool"):
        ipmitool =  "./" + ipmitool
    return ipmitool

def _replace(e,r={"\n":"","\r":""}):
    for rr in r:
        e = e.replace(rr,r[rr])
    return e
def get_line_info(logs,greps=[""],skips=["********"],r={"  ":"","\r":"","\t":""}):
    re = []
    for log in logs.split("\n"):
        is_append = False
        for grep in greps:
            if log.find(grep) != -1:
                is_append = True
        for skip in skips:
            if log.find(skip) != -1:
                is_append = False
        if is_append:
            re.append(_replace(log, r))
    return re

def exec_cmd(e,debug=True,retry = 1):
    print "exec_cmd"
    print "e1: %s" % (e)
    #if (args.debug != 0 and debug == True) or args.syscmd_print != 0:
        #print e
    print "e2: %s" %(e)
    for i in range(0,retry):
        print "e3: %s" % (e)
        re = commands.getstatusoutput(e)
        print "getstatusoutput: %s" %(re)
        if re[0] != 0:
            print re[1]
        if re[0] == 0 :
            return re
    return -1,"ERROR:exec_cmd %s retry %s" %(e,retry)

def printd(parameters):
    now = datetime.datetime.now()
    str = now.strftime("%Y-%m-%d %H:%M:%S") + " " + parameters

def ssh(ip,u,p):
    ssh = pexpect.spawn ("sshpass -p %a ssh -o StrictHostKeyChecking=no %s/%s" %(p,u,ip) ,timeout=5*60)

    #return ssh;

def ssh_pass(P=None,U=None,H=None,C=""):
    if U == None:
        U = args.bmc_user
    if P == None:
        P = args.bmc_pass
    if H == None:
        H = args.bmcip
    C = C.replace("./ipmitool","ipmitool")
    c = "sshpass -p %s ssh -o StrictHostKeyChecking=no -t %s@%s '%s'" %(P,U,H,C)
    if os.path.exists("./sshpass"):
        c = "./" + c
    return c

def scan_macaddr(h):
    for board in g_boards:
        re = exec_cmd(ssh_pass(H=h,U=board['bmc_user'],P=board['bmc_pass'],C="ifconfig | grep HWaddr"),False,retry=1)
        if re[0] == 0:
            return re[1] #_replace(re[1],{"\n":" ","\r":""})
    return ""

def get_centos_info(h):
    re = exec_cmd(ssh_pass(H=h,U='root',P='root',C="ipmitool lan print && dmidecode"),False,retry=1)
    return re[1]
    if re[0] == 0:
        return get_line_info(logs=re[1],greps=["IP Address","Part Number:","Vendor:"],skips=[" Array ","Address Source"])

def scanip_fru_print(h):
    #print h
    for board in g_boards:
        args.U = board['U']
        args.P = board['P']
        print "Thuc thi ipmitool"
        #re = exec_cmd(ipmitool(h) + "fru print",False,retry=1)
        re = commands.getstatusoutput("ifconfig")
        print "re: %s" %(re[1])
        if re[0] == 0:
            return re[1]#get_line_info(logs=re[1],greps=["Board Product","Board Serial","Product Version"])
    return None

def is_port_open(ip,port):
    socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    ret = socket_obj.connect_ex((ip,port))
    socket_obj.close()
    return ret

def scandv(ip,port):
    print "ip la: %s" %(ip)
    print "Start scan device with IP: %s" %(ip)
    try:
        print "is_port_open: %s" %(is_port_open(ip,port))
        if is_port_open(ip,port) == 0:
            re = scanip_fru_print(ip)
            print "re: %s" % (re)
            if re != None:
                print re
                print scan_macaddr(ip)
            else:
                print get_centos_info(ip)
    except KeyboardInterrupt:
        sys.exit(-1)
    except:
        pass

#Main loop:
def main():
    print "Hello"
    if args.scandv != "":
        print "scan"
        print args.scandv
        for ip in args.scandv.split(","):
            scandv(ip,22)
        print "DONE"
        sys.exit()

if __name__ == '__main__':
    try:
        main();
    except KeyboardInterrupt:
        pass
        # ignore exception as it is a valid way to exit the program
        # and skip to finally clause
    except Exception as e:
        printd("ERROR: %s" %e);





