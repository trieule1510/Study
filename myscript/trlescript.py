#!/usr/bin/python
import pexpect
import sys
import os
import argparse
import time
import commands
import datetime
import threading
from threading import Thread
import socket

parser = argparse.ArgumentParser(
    description='Open tty kermit/ipmitool/ssh/cielo | program image hpm | on/off board | send file via UART script!')
parser.add_argument('--scanip', dest='scanip', default="", help='scanip')
parser.add_argument('--h', dest='h', default="", help='Remote Host IP address')
parser.add_argument('--hostip', dest='hostip', default="", help='Remote Host IP address')


global g_boards
g_boards = []
g_boards.append({"board": "jade", "bmc_user": "root", "bmc_pass": "root", "U": "ADMIN", "P": "ADMIN"})
g_boards.append({"board": "snow", "bmc_user": "sysadmin", "bmc_pass": "superuser", "U": "admin", "P": "password"})
g_boards.append({"board": "collins", "bmc_user": "sysadmin", "bmc_pass": "superuser", "U": "admin", "P": "admin"})

sys_argv = ' '.join([str(e) for e in sys.argv])
if sys_argv.find("--") == -1:
    args = parser.parse_args("")
    if len(sys.argv) >= 2: args.tty = sys.argv[1]
    if len(sys.argv) >= 3: args.log = sys.argv[2]
else:
    args = parser.parse_args()
if args.h != "":
    args.hostip = args.h
if args.hostip.find("@") != -1:
    x = args.hostip.split("@")
    args.hostip = x[1]
    args.hostuser = x[0]

def search_board_type():
    if args.scanip != "":
        return
    if args.board_type == "":
        for board in g_boards:
            args.bmc_user = board['bmc_user']
            args.bmc_pass = board['bmc_pass']
            args.U = board['U']
            args.P = board['P']
            args.board_type = board['board']
            re = exec_cmd(ipmitool(args.bmcip) + "bmc info", False, retry=1)
            if re[0] == 0:
                print "Search board %s" % (board)
                break
    else:
        for board in g_boards:
            if args.board_type == board['board']:
                args.bmc_user = board['bmc_user']
                args.bmc_pass = board['bmc_pass']
                args.U = board['U']
                args.P = board['P']

def ipmitool(ip=""):
    search_board_type()
    ipmitool = "ipmitool "
    if args.hostport == "":
        ipmitool = ipmitool + "-H " + ip + " -U %s -P %s" % (args.U, args.P)
    ipmitool = ipmitool + " -I lanplus -z 0x7fff "
    if os.path.exists("./ipmitool"):
        ipmitool = "./" + ipmitool
    return ipmitool

def exec_cmd(e, debug=True, retry=3):
    for i in range(0, retry):
        if debug == True: print e
        re = commands.getstatusoutput(e)
        if re[0] == 0: return re
    return -1, "ERROR:exec_cmd %s retry %s" % (e, retry)

def ssh_pass(P="None", U=None, H=None, C=""):
    C = C.replace("./ipmitool", "ipmitool")
    return "sshpass -p %s ssh -o StrictHostKeyChecking=no -t %s@%s '%s'" % (P, U, H, C)

def search_host_pass():
    if args.hostip != "" and (args.hostuser == "" or args.hostpass == ""):
        for e in g_passw_list:
            re = exec_cmd(ssh_pass(P=e[1], U=e[0], H=args.hostip, C="ls"), debug=False, retry=1)
            if re[0] == 0:
                args.hostuser = e[0]
                args.hostpass = e[1]
                print "hostuser %s" % (args.hostuser)
                print "hostpass %s" % (args.hostpass)

def is_port_open(ip, port):
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)
    ret = socket_obj.connect_ex((ip, port))
    socket_obj.close()
    return ret

def get_line_info(logs, greps=[""], skips=["********"], r={"  ": "", "\r": "", "\t": ""}):
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

def scanip_fru_print(h):
    # print h
    for board in g_boards:
        args.U = board['U']
        args.P = board['P']
        # print ipmitool(ip=h) + "fru print"
        re = exec_cmd(ipmitool(h) + "fru print", False, retry=1)
        if re[0] == 0:
            return get_line_info(logs=re[1], greps=["Board Product", "Board Serial", "Product Version"])
    return None

def get_centos_info(h):
    re = exec_cmd(ssh_pass(H=h, U='root', P='root', C="ipmitool lan print && dmidecode"), False, retry=1)
    print re
    if re[0] == 0:
        return get_line_info(logs=re[1], greps=["IP Address", "Part Number:", "Vendor:"],
                             skips=[" Array ", "Address Source"])
    return None

def scanip(ip, port):
    ip = ip.split(".")
    ipstart = int(ip[3])
    bmcip = "%s.%s.%s." % (ip[0], ip[1], ip[2])
    print "Start scan IP %s%d to %s%d" % (bmcip, ipstart, bmcip, 255)
    for i in range(ipstart, 255):
        try:
            h = "%s%d" % (bmcip, i)
            print scanip_fru_print(h)
            print get_centos_info(h)
        except KeyboardInterrupt:
            sys.exit(-1)
        except:
            pass

if args.scanip != "":
    for ip in args.scanip.split(","):
        scanip(ip, 22)
    print "DONE"
    sys.exit()
search_host_pass()

