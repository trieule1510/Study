#!/usr/bin/python
import pexpect
import sys
import os
import datetime
import argparse
import commands
parser = argparse.ArgumentParser(description='bmc_fw script!')

parser.add_argument('--tty', dest='tty',default="",help='tty')
parser.add_argument('--hostip', dest='hostip',default="",help='hostip')
parser.add_argument('--bmc_user', dest='bmc_user',default="root",help='bmc_user')
parser.add_argument('--bmc_pass', dest='bmc_pass',default="root",help='bmc_pass')
parser.add_argument('--hostuser', dest='hostuser',default="",help='hostuser')
parser.add_argument('--hostpass', dest='hostpass',default="",help='hostpass')
parser.add_argument('--ima_file', dest='ima_file',default="jade_bmc_1.05.210423.ima",help='ima_file')
parser.add_argument('--cmd_type', dest='cmd_type',default="cp",help='cmd_type:cp or sf')

parser.add_argument('--tftp_ip', dest='tftp_ip',default="10.38.13.103",help='tftp_ip')
parser.add_argument('--tftp_pwd', dest='tftp_pwd',default="/tftpboot",help='tftp_pwd')
parser.add_argument('--tftp_user', dest='tftp_user',default="amcclab",help='tftp_user')
parser.add_argument('--tftp_pass', dest='tftp_pass',default="amcc1234",help='tftp_pass')

parser.add_argument('--ethact', dest='ethact',default="ast_eth1",help='ethact')
parser.add_argument('--debug', dest='debug',default=1,type=int,help='debug')
parser.add_argument('--timeout', dest='timeout',default=30*60,type=int,help='debug')
parser.add_argument('--uboot_prom', dest='uboot_prom',default="AST2500EVB>",help='uboot_prom')
parser.add_argument('--bmc_prom', dest='bmc_prom',default="~",help='bmc_prom')
parser.add_argument('--mac_tmp', dest='mac_tmp',default="00:00:ca:fe:ca:fe",help='mac_tmp')
parser.add_argument('--interact', dest='interact',default=0,type=int,help='interact')



args = parser.parse_args()
tty=None
def now():
    return str(datetime.datetime.today().strftime('%y%m%d_%H%M%S'))
def find_in( s, first, last="",A=0,B=0):
    try:
        start = s.index( first ) + len( first ) 
        if last == "":
            end = len(s)
        else:
            end = s.index( last, start ) 
        return s[start-A:end + B]
    except ValueError:return ""
def _replace(e,r={"\n":"","\r":""}):
    for rr in r:
        e = e.replace(rr,r[rr])
    return e
def exec_cmd(e):
    re = commands.getstatusoutput(e)
    return re
def ssh_pass(P,U,H,C=""):
    return "sshpass -p %s ssh -o StrictHostKeyChecking=no -t %s@%s '%s'" %(P,U,H,C)
def scp_file(F,U,H,P,D="/var/tmp"):
    sshpass = "sshpass -p " + P + " scp  -o StrictHostKeyChecking=no  " + F +" "+ U + "@" + H +":" + D
    return exec_cmd(sshpass)
def xconsole_args(arg):
    arg.update({ "hostip":args.hostip,
                 "hostuser":args.hostuser,
                 "hostpass":args.hostpass})
    c = "./xconsole.py"
    for e in arg:
        if arg[e] =="" or arg[e] =="None":
            pass
        else:
            c = "%s --%s %s" %(c ,e,arg[e])
    print c
    return c
def xconsole(tty="",note=""):
    tty = pexpect.spawn(xconsole_args({"tty":tty,"note":note}),timeout=300000)
    if args.debug >= 1:
        tty.logfile_read = sys.stdout
    return tty
def do_print(msg):
    #print now(),
    print "==>%s" %(msg)
def do_exit(tty,msg,exit_code=-1):
    #print now(),
    print " ERROR: ",
    print msg
    if tty != None:
        tty.logfile_read = None
        if args.interact != 0:
            tty.interact()
    sys.exit(exit_code)
def _expect(tty,pattern,timeout):
    re = tty.expect(pattern,timeout=timeout)
    return re
def uboot_send(tty,msg,timeout=15,false_exit=True):
    do_print(msg)
    tty.sendline(msg)
    re = _expect(tty,[msg.split(' ')[0],pexpect.EOF, pexpect.TIMEOUT],timeout=10)
    if re != 0:
        do_exit(tty,"echo ==>%s<==" %(msg))
    if false_exit:
        re = _expect(tty,[args.uboot_prom,pexpect.EOF, pexpect.TIMEOUT],timeout=timeout)
    if false_exit and re != 0:
        tty.send('\003')
        do_exit(tty,msg)
    return re
def get_uboot_env(uboot_env):
    env = {}
    for e in uboot_env.split("\n"):
        e = _replace(e)
        ee = e.split("=")
        if len(ee) == 2:
            env.update({ee[0]:ee[1]})
    return env
def wait_uboot(tty):
    do_print("wait uboot_prom %s" %(args.uboot_prom))
    is_reboot = False 
    while True:
        try:
            re = _expect(tty,[args.uboot_prom,"login:","Password:","logout from",args.bmc_prom, pexpect.EOF, pexpect.TIMEOUT],timeout=0.5)
            if re == 0:
                break
            elif re == 1:
                tty.sendline(args.bmc_user)
                _expect(tty,["Password:"],timeout=3*60)
                tty.sendline(args.bmc_pass)
                continue
            elif re == 2:
                tty.sendline(args.bmc_pass)
                continue
            elif re == 3:
                #if is_reboot:
                #    do_exit(tty,"Request enable root!!!")
                continue
            elif re == 4:
                tty.sendline("reboot")
                is_reboot = True
            else:
                tty.sendline()
        except:
            do_exit(tty,"wait %s" %(args.uboot_prom))
if args.tty =="":
    do_exit(None,"Request tty")
if args.hostip =="":
    do_exit(None,"Request hostip")
do_print("__START__")
do_print("WAIT POWER AC BOARD")
re = exec_cmd(ssh_pass(H=args.tftp_ip, P=args.tftp_pass,U=args.tftp_user,C="ls %s/%s" %(args.tftp_pwd,os.path.basename(args.ima_file))))
if re[0] != 0:
    re = scp_file(F=args.ima_file, U=args.tftp_user, H=args.tftp_ip, P=args.tftp_pass, D=args.tftp_pwd)
    if re[0] != 0:
        print re[1]
        do_exit(None,"scp_file %s" %(args.ima_file))
tty = xconsole(tty=args.tty)

wait_uboot(tty)
uboot_send(tty,"version")
uboot_send(tty,"mw.l 0x1e78502c 0x92")
uboot_send(tty,"printenv")
uboot_env = get_uboot_env(tty.before)
for e in uboot_env:
    if uboot_env[e] == "00:00:00:00:00:00":
            uboot_send(tty,"setenv %s %s" %(e,args.mac_tmp))
uboot_send(tty,"setenv ethact %s" %(args.ethact))
uboot_send(tty,"dhcp")
uboot_send(tty,"setenv serverip %s" %(args.tftp_ip))
uboot_send(tty,"tftp 0x80000000 %s" %(os.path.basename(args.ima_file)),timeout=args.timeout)
if tty.before.find("Bytes transferred = %s" %(os.path.getsize(args.ima_file))) == -1:
    do_exit(tty,"!tftp file")
if args.cmd_type == "cp":
    uboot_send(tty,"protect off 0x20000000 +${filesize}",timeout=args.timeout)
    uboot_send(tty,"erase 0x20000000 +${filesize}",timeout=args.timeout)
    if tty.before.find("Erased ") == -1:
        do_exit(tty,"erase failed ! DO NOT REBOOT BOARD")
    uboot_send(tty,"cp.b 0x80000000 0x20000000 ${filesize}",timeout=args.timeout)
    if tty.before.find(" done") == -1:
        do_exit(tty,"cp.b failed ! DO NOT REBOOT BOARD")
    uboot_send(tty,"protect on all",timeout=args.timeout)
elif args.cmd_type == "sf":
    uboot_send(tty,"sf probe 0;sf update 80000000 0 ${filesize}",timeout=args.timeout,false_exit=True)
    if tty.before.find("written") == -1:
        do_exit(tty,"!sf written")
else:
    do_exit(tty,"cmd_type %s not support") %(args.cmd_type)
uboot_send(tty,"reset",timeout=args.timeout,false_exit=False)
sys.exit(0)
