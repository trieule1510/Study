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
parser.add_argument('--tty', dest='tty', default="", help='Open /dev/$tty')
parser.add_argument('--log', dest='log', default="", help='Save log file')
parser.add_argument('--list', dest='list', default=1, type=int, help='list all Name/ID of ttyUSB')
parser.add_argument('--h', dest='h', default="", help='Remote Host IP address')
parser.add_argument('--hostip', dest='hostip', default="", help='Remote Host IP address')
parser.add_argument('--hostuser', dest='hostuser', default="", help='Remote Host user')
parser.add_argument('--hostpass', dest='hostpass', default="", help='Remote Host pass')
parser.add_argument('--hostprom', dest='hostprom', default="~", help='Remote Host prom')
parser.add_argument('--hostport', dest='hostport', default="", help='cielo port')
parser.add_argument('--bmcip', dest='bmcip', default="", help='bmcip')
parser.add_argument('--sol', dest='sol', default="", help='SOL number: 1=UEFI 2=S0-CLI 3=ATF 4=S1-CLI')
parser.add_argument('--cmd', dest='cmd', default="", help='exec cmd')
parser.add_argument('--hpm', dest='hpm', default="", help='program hpm')
parser.add_argument('--force', dest='force', default=1, type=int, help='force open UART')
parser.add_argument('--debug', dest='debug', default=0, type=int, help='debug')
parser.add_argument('--file', dest='file', default="", help='Upload cielo file')
parser.add_argument('--fru', dest='fru', default="", help='print fru')
parser.add_argument('--board_type', dest='board_type', default="", help='board type')

parser.add_argument('--detect_tty', dest='detect_tty', default="", help='detect_tty')
parser.add_argument('--tty_bmc', dest='tty_bmc', default="", help='tty_bmc')
parser.add_argument('--tty_uefi', dest='tty_uefi', default="", help='tty_uefi')
parser.add_argument('--tty_atf', dest='tty_atf', default="", help='tty_atf')
parser.add_argument('--tty_s0cli', dest='tty_s0cli', default="", help='tty_s0cli')
parser.add_argument('--tty_s1cli', dest='tty_s1cli', default="", help='tty_s0cli')
parser.add_argument('--nps', dest='nps', default="", help='nps')
parser.add_argument('--enable_root', dest='enable_root', default="", help='enable_root')
parser.add_argument('--screen', dest='screen', default="", help='screen')
parser.add_argument('--screen_log', dest='screen_log', default="", help='screen_log')

parser.add_argument('--bmc_user', dest='bmc_user', default="root", help='bmc_user')
parser.add_argument('--bmc_pass', dest='bmc_pass', default="root", help='bmc_pass')
parser.add_argument('--U', dest='U', default="ADMIN", help='')
parser.add_argument('--P', dest='P', default="ADMIN", help='')
parser.add_argument('--note', dest='note', default="", help='')
parser.add_argument('--scanip', dest='scanip', default="", help='scanip')

g_passw_list = [["amcclab", "amcc1234"], ["amplab", "Ampere@4655"], ["amplab", "amp1234"], ["root", "root"]]
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


def _replace(e, r={"\n": "", "\r": ""}):
    for rr in r:
        e = e.replace(rr, r[rr])
    return e


if len(args.tty) == 1:
    args.sol = args.tty
    args.tty = ""


def now():
    return str(datetime.datetime.today().strftime('%y%m%d_%H%M%S'))


def find_in(s, first, last, A=0, B=0):
    try:
        start = s.index(first) + len(first)
        if last == "":
            end = len(s)
        else:
            end = s.index(last, start)
        return s[start - A:end + B]
    except ValueError:
        return ""


def ipmitool(ip=""):
    search_board_type()
    ipmitool = "ipmitool "
    if args.hostport == "":
        ipmitool = ipmitool + "-H " + ip + " -U %s -P %s" % (args.U, args.P)
    ipmitool = ipmitool + " -I lanplus -z 0x7fff "
    if os.path.exists("./ipmitool"):
        ipmitool = "./" + ipmitool
    return ipmitool


def ssh_pass(P="None", U=None, H=None, C=""):
    C = C.replace("./ipmitool", "ipmitool")
    return "sshpass -p %s ssh -o StrictHostKeyChecking=no -t %s@%s '%s'" % (P, U, H, C)


def ipmitool_exec(cmd, debug=True, retry=3):
    print cmd
    for i in range(0, retry):
        if args.hostip != "":
            re = exec_cmd(ssh_pass(P=args.hostpass, U=args.hostuser, H=args.hostip, C=cmd), debug, 3)
        else:
            re = exec_cmd(cmd, debug, 3)
        if re[0] == 0:
            return re[1]
    return ""


def exec_cmd(e, debug=True, retry=3):
    for i in range(0, retry):
        if debug == True: print e
        re = commands.getstatusoutput(e)
        if re[0] == 0: return re
    return -1, "ERROR:exec_cmd %s retry %s" % (e, retry)


def fru_print(bmcip):
    print ipmitool_exec(ipmitool(bmcip) + "fru print", False, 1)
    print ipmitool_exec(ipmitool(bmcip) + "mc info", False, 1)


def enable_root():
    print ipmitool_exec(ipmitool(args.bmcip) + "raw 0x32 0x91 1")


def BMCoff(bmcip):
    print ("CHASSIS POWER OFF[%s]" % (now()))
    return ipmitool_exec(ipmitool(bmcip) + "chassis power off")


def BMCon(bmcip):
    print ("CHASSIS POWER ON[%s]" % (now()))
    return ipmitool_exec(ipmitool(bmcip) + "chassis power on")


def BMCReset(ip):
    if args.nps != "":
        exec_cmd(args.nps)
    elif ip != "":
        BMCoff(ip)
        time.sleep(5)
        BMCon(ip)
    else:
        print "ERROR:BMCReset need BMCIP or NPS"


def cielo_upload(fname):
    import json
    import requests
    request_data = {"Action": "UploadFile",
                    "UserId": args.hostuser,
                    "Password": args.hostpass}

    server_address = "http://" + args.hostip + ":8080"
    files = {'data': ['data', json.dumps(request_data), 'application/json'],
             'file': [os.path.basename(fname), open(fname, 'rb'), 'application/octet']
             }
    resp = requests.post(server_address, files=files)
    resp_data = json.loads(resp.text)
    errno = resp_data['Error']
    data = resp_data['Data']
    msg = resp_data['Message']
    return errno


def tty2id(tty_serials, ttyUSB):
    if ttyUSB.find('tty') != -1:
        for tty_serial in tty_serials:
            if tty_serial.find(ttyUSB) != -1:
                re = find_in(tty_serial, "ID_SERIAL_SHORT='", "'")
                if re != "": return re
    return ttyUSB


def id2tty(tty_serials, ttyUSB):
    if ttyUSB.find('tty') == -1:
        for tty_serial in tty_serials:
            if tty_serial.find(ttyUSB + "'") != -1:
                re = find_in(tty_serial, "/dev/", "'")
                if re != "": return re
    return ttyUSB


def list_ttyusb(tty_serials, tty_dmesgs):
    ttyUSBID = []
    re = []
    for tty_dmesg in reversed(tty_dmesgs):
        ttyUSB = find_in(tty_dmesg, " to ", "") + "'"
        if (ttyUSB != "") and (ttyUSB.find('tty') != -1) and ((ttyUSB in ttyUSBID) == False):
            id = tty2id(tty_serials, ttyUSB)
            if id != ttyUSB:
                ttyUSBID.append(ttyUSB)
                re.append("[%s] %s %s" % (find_in(tty_dmesg, "[", "]"), ttyUSB, id))
    return re


def get_ttydata():
    tty_serial = commands.getstatusoutput("for i in $(find /sys/bus/usb/devices/usb*/ -name dev | grep --color=never ttyUSB);\
         do udevadm info -q property --export -p `dirname $i` |\
         grep --color=never  'DEVNAME\|ID_SERIAL_SHORT';done")
    tty_dmesg = commands.getstatusoutput("dmesg | grep 'to ttyUSB'")
    return tty_serial[1].split("DEVNAME="), tty_dmesg[1].replace("\r", "").split("\n")


def get_ttydata_ssh(hostip="localhost", hostuser="root", hostpass="root", hostprom="~", timeout=1 * 60):
    tty = pexpect.spawn("ssh -o 'StrictHostKeyChecking no' %s@%s" % (hostuser, hostip), timeout=4 * timeout)
    if args.debug != 0:
        tty.logfile_read = sys.stdout
    if tty.expect(["password", pexpect.EOF, pexpect.TIMEOUT], timeout=timeout) != 0:
        return "", ""
    tty.sendline(hostpass)
    if tty.expect([hostprom, pexpect.EOF, pexpect.TIMEOUT, "Permission denied"], timeout=timeout) != 0:
        print "get_ttydata_ssh error"
        return "", "Permission denied"
    tty.sendline("bash")
    tty.sendline("for i in $(find /sys/bus/usb/devices/usb*/ -name dev | grep --color=never ttyUSB); \
            do udevadm info -q property --export -p `dirname $i` | \
            grep --color=never  'DEVNAME\|ID_SERIAL_SHORT';done;echo -n __DONE__;echo -n __DONE__")
    if tty.expect(["__DONE____DONE__"], timeout=timeout) != 0:
        return "", ""
    tty_serial = tty.before.split("DEVNAME=")
    tty.sendline("dmesg | grep --color=never 'to ttyUSB';echo -n __DONE__;echo -n __DONE__")
    if tty.expect(["__DONE____DONE__"], timeout=timeout) != 0:
        return "", ""
    tty_dmesg = tty.before.replace("\r", "").split("\n")
    return tty_serial, tty_dmesg


def ckermit_cfg(ttyUSB, speed=115200):
    msg = "'set line /dev/%s" % (ttyUSB)
    msg = msg + "\n" + "set speed %d" % (speed)
    msg = msg + "\n" + "set carrier-watch off"
    msg = msg + "\n" + "set handshake none"
    msg = msg + "\n" + "set flow-control none"
    msg = msg + "\n" + "robust"
    msg = msg + "\n" + "set file type bin"
    msg = msg + "\n" + "set file name lit"
    msg = msg + "\n" + "set rec pack 1000"
    msg = msg + "\n" + "set send pack 1000"
    msg = msg + "\n" + "set window 5'"
    return msg


def ssh_tty(hostip="", hostuser="", hostpass="", hostprom="~", ttyUSB="", log="", speed=115200, timeout=1 * 60,
            retry=3):
    if ttyUSB == "" or hostip == "" or hostpass == "":
        return None, "ERROR: miss ttyUSB or hostip"
    if ttyUSB.find("tty") == -1:
        tty_serials, tty_dmesgs = get_ttydata_ssh(hostip, hostuser, hostpass)
        ttyUSB = id2tty(tty_serials, ttyUSB)
    lock_pid = ""
    for i in range(0, retry):
        tty = pexpect.spawn("ssh -o 'StrictHostKeyChecking no' %s@%s" % (hostuser, hostip), timeout=300000)
        if args.debug != 0:
            tty.logfile_read = sys.stdout
        if tty.expect(["password", pexpect.EOF, pexpect.TIMEOUT], timeout=timeout) != 0:
            return None, "ERROR: timeout ssh wait password"
        tty.sendline(hostpass)
        if tty.expect([hostprom, pexpect.EOF, pexpect.TIMEOUT], timeout=timeout) != 0:
            return None, "ERROR: timeout ssh wait hostprom"
        tty.sendline("sudo echo %s" % (ttyUSB))
        if tty.expect(["password", hostprom, pexpect.EOF, pexpect.TIMEOUT], timeout=timeout) > 1:
            return None, "ERROR: timeout ssh wait sudo password"
        tty.sendline(hostpass)
        if tty.expect([hostprom, pexpect.EOF, pexpect.TIMEOUT], timeout=timeout) != 0:
            return None, "ERROR: timeout ssh wait sudo hostprom"
        tty.sendline("sudo fuser -k /dev/%s" % (ttyUSB))
        if tty.expect([hostprom, pexpect.EOF, pexpect.TIMEOUT], timeout=timeout) != 0:
            return None, "ERROR: timeout ssh wait sudo hostprom"
        tty.sendline("sudo echo -e %s > /tmp/.kermit_%s" % (ckermit_cfg(ttyUSB, speed), ttyUSB))
        if lock_pid != "":
            print "Kild pid %s" % (lock_pid)
            tty.sendline("sudo kill -9 %s" % (lock_pid))

        tty.sendline("sudo kermit -c -y /tmp/.kermit_%s -f ; exit" % (ttyUSB))
        re = tty.expect(["--------", "has no effect without prior", pexpect.EOF, pexpect.TIMEOUT], timeout=timeout)
        if re == 1:
            if args.force != 0:
                lock_pid = find_in(tty.before, "Locked by process ", "\n")
                continue
            else:
                print tty.before
                return None, "Locked by process"
        if re == 2:
            return None, "ERROR:EOF"
        if re == 3:
            return None, "ERROR:TIMEOUT"
        if re == 0:
            return tty, "PASS"
    return None, "ERROR: Open Console"


def local_tty(ttyUSB="", log="", speed=115200, timeout=1 * 60, retry=3):
    if ttyUSB == "":
        return None, "ERROR:Need ttyUSB"
    if ttyUSB.find("tty") == -1:
        tty_serials, tty_dmesgs = get_ttydata()
        ttyUSB = id2tty(tty_serials, ttyUSB)
    os.system("sudo echo -e %s > /tmp/.kermit_%s" % (ckermit_cfg(ttyUSB, speed), ttyUSB))
    for i in range(0, retry):
        tty = pexpect.spawn("sudo kermit -c -y /tmp/.kermit_%s -f" % (ttyUSB), timeout=300000)
        if args.debug != 0:
            tty.logfile_read = sys.stdout
        re = tty.expect(["--------", "has no effect without prior", pexpect.EOF, pexpect.TIMEOUT], timeout=timeout)
        if re == 1:
            if args.force != 0:
                pid = find_in(tty.before, "Locked by process ", "\r\n")
                print "Locked by process %s kill true" % (pid)
                os.system("sudo kill -9 %s" % (pid))
                time.sleep(1)
                continue
            else:
                print tty.before
                return None, "Locked by process"
        if re == 2:
            return None, "ERROR:EOF"
        if re == 3:
            return None, "ERROR:TIMEOUT"
        if re == 0:
            return tty, "PASS"
    return None, "ERROR: Open Console"


def sol_tty(bmcip="", sol="", log=""):
    if bmcip == "" or sol == "":
        return None, "ERROR: Need bmcip and sol"
    cmd_deactivate = ipmitool(bmcip) + " sol deactivate instance=%s" % (sol)
    cmd_activate = ipmitool(bmcip) + " sol activate=usesolkeepalive instance=%s" % (sol)
    if args.force != 0:
        print cmd_deactivate
        os.system(cmd_deactivate)
    print cmd_activate
    tty = pexpect.spawn(cmd_activate, timeout=300000)
    if args.debug != 0:
        tty.logfile_read = sys.stdout
    tty.expect("for help]", timeout=1 * 60)
    return tty, "PASS"


def cielo_tty(spawn, timeout=1 * 60):
    key = [["Username:", args.hostuser],
           ["Password:", args.hostpass],
           ["Cielo CS >", "return"],
           [pexpect.EOF, "EOF"],
           [pexpect.TIMEOUT, "TIMEOUT"]
           ]
    expect_str = [x[0] for x in key]
    send_str = [x[1] for x in key]

    tty = pexpect.spawn(spawn, timeout=300000)
    if args.debug != 0:
        tty.logfile_read = sys.stdout
    while True:
        print expect_str
        re = tty.expect(expect_str, timeout=timeout)
        if expect_str[re] == pexpect.EOF:
            return None, "EOF"
        if expect_str[re] == pexpect.TIMEOUT:
            return None, "TIMEOUT %d" % (timeout)
        if send_str[re] == "return":
            return tty, ""
        tty.sendline(send_str[re])


def xconsole(bmcip, sol, hostip, hostuser, hostpass, hostprom, hostport, ttyUSB):
    if hostip != "" and hostport != "" and sol != "":
        tty, re = cielo_tty("telnet %s %s" % (hostip, hostport))
        tty.sendline(ipmitool() + " sol deactivate instance=%s" % (sol))
        tty.sendline(ipmitool() + " sol activate instance=%s" % (sol))
    elif hostip != "" and hostport != "":
        tty, re = cielo_tty("telnet %s %s" % (hostip, hostport))
    elif hostip != "" and ttyUSB != "":
        tty, re = ssh_tty(hostip, hostuser, hostpass, hostprom, ttyUSB)
    elif hostip == "" and ttyUSB != "":
        tty, re = local_tty(ttyUSB)
    elif sol != "":
        tty, re = sol_tty(bmcip, sol)
    else:
        return None, "ERR"
    return tty, re


def _expect(tty, list, timeout=5 * 60, debug=False):
    start_time = time.time()
    if debug:
        print "__expect ",
        print  (list),
        print "[%d]" % (timeout)
    try:
        re = tty.expect(list, timeout)
        if debug:
            elapsed_time = time.time() - start_time
            x = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            print ("[expected=%s %s]" % (list[re].replace("\n", "[n]"), x))
        if re >= len(list):
            return -3
        else:
            return re
    except KeyboardInterrupt:
        return -2
    except:
        # print traceback.print_exc()
        return -1


def get_detect_tty(i):
    e = args.detect_tty.split(",")
    try:
        return e[i]
    except:
        return ""


def uart_th(arg, timeout=60):
    pattern = ["SMpro Rom Firmware", "DRAM FW version", "Welcome to AEROe", "Booting Trusted Firmware", "login:",
               "U-Boot", "Password:", "~ #", "~]#", "\n"]
    tty_name = get_detect_tty(arg)
    if (tty_name == "") or (tty_name == "None") or (len(tty_name) < 2):
        return
    t = threading.currentThread()
    tty, re = xconsole(args.bmcip, args.sol, args.hostip, args.hostuser, args.hostpass, args.hostprom, args.hostport,
                       tty_name)
    tty.sendline("")
    tty.sendline("")
    tty.sendline("")

    while getattr(t, "do_run", True):
        re = _expect(tty, pattern, timeout=timeout, debug=False)
        if re < 0:
            break
        if pattern[re] == "\n":
            continue
        if pattern[re] == "SMpro Rom Firmware":
            args.tty_s0cli = tty_name
            print "detect_tty %s %s " % ("tty_s0cli", tty_name)
        if pattern[re] == "DRAM FW version" or pattern[re] == "Welcome to AEROe":
            args.tty_uefi = tty_name
            print "detect_tty %s %s " % ("tty_uefi", tty_name)
        if pattern[re] == "Booting Trusted Firmware":
            args.tty_atf = tty_name
            print "detect_tty %s %s " % ("tty_atf", tty_name)
        if pattern[re] == "U-Boot":
            args.tty_bmc = tty_name
            print "detect_tty %s %s " % ("tty_bmc", tty_name)
        if pattern[re] == "login:":
            tty.sendline("root")
            continue
        if pattern[re] == "Password:":
            tty.sendline("root")
            continue
        if pattern[re] == "~]#" or pattern[re] == "~ #":
            tty.sendline("ifconfig")
            _expect(tty, ["ifconfig"], timeout=10)
            _expect(tty, ["~]#", "~ #"], timeout=10)
            bmcip = find_in(tty.before, "inet addr:", " ")
            print "detect_tty %s %s " % ("bmcip", bmcip)
            print "detect_tty %s %s " % ("tty_bmc", tty_name)
            BMCReset(bmcip)
            fru_print(bmcip)
        break


def __bg_start(th, arg):
    bg = Thread(target=th, args=(arg,))
    bg.do_run = True
    bg.start()
    return bg


def __bg_stop(bg):
    if bg != None:
        bg.join()


def detect_tty():
    uart_0_bg = __bg_start(uart_th, 0)
    uart_1_bg = __bg_start(uart_th, 1)
    uart_2_bg = __bg_start(uart_th, 2)
    uart_3_bg = __bg_start(uart_th, 3)
    uart_4_bg = __bg_start(uart_th, 4)
    if args.bmcip != "" or args.nps != "":
        BMCReset(args.bmcip)
    __bg_stop(uart_0_bg)
    __bg_stop(uart_1_bg)
    __bg_stop(uart_2_bg)
    __bg_stop(uart_3_bg)
    __bg_stop(uart_4_bg)
    sys.exit()


def xconsole_args(arg):
    c = "./xconsole.py"
    for e in arg:
        if arg[e] != "":
            c = "%s --%s %s" % (c, e, arg[e])
    print c
    return c


def xconsole_args2(tty="", sol="", cmd="", log="", hpm=""):
    c = "./xconsole.py"
    if args.bmcip != "": c = "%s --bmcip '%s'" % (c, args.bmcip)
    if args.hostip != "": c = "%s --hostip '%s'" % (c, args.hostip)
    if args.hostuser != "amcclab": c = "%s --hostuser '%s'" % (c, args.hostuser)
    if args.hostpass != "amcc1234": c = "%s --hostpass '%s'" % (c, args.hostpass)
    if args.hostprom != "~": c = "%s --hostprom '%s'" % (c, args.hostprom)
    if args.hostport != "": c = "%s --hostport '%s'" % (c, args.hostport)
    if args.board_type != "":
        c = "%s --board '%s'" % (c, args.board_type)
    if tty != "": c = "%s --tty '%s'" % (c, tty)
    if sol != "": c = "%s --sol '%s'" % (c, sol)
    if cmd != "": c = "%s --cmd '%s'" % (c, cmd)
    if log != "": c = "%s --log '%s'" % (c, log)
    if hpm != "": c = "%s --hpm '%s'" % (c, hpm)
    print c
    return c


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def _screen_tty(name, id, tty, cmd, note):
    time.sleep(0.5)
    tee_cmd = ""
    if args.screen_log != "":
        tee_cmd = " | tee -a %s-%s-%s" % (args.screen_log, note, now())
    if tty != "":
        x_args = {"tty": tty, "bmcip": args.bmcip, "hostip": args.hostip, "hostuser": args.hostuser,
                  "hostpass": args.hostpass, "hostport": args.hostport, "board_type": args.board_type}
        os.system("screen -S %s -p%d -X stuff '%s%s'\r\n" \
                  % (name, id, xconsole_args(x_args), tee_cmd))
    else:
        os.system("screen -S %s -p%d -X stuff '%s%s'\r\n" % (name, id, cmd, tee_cmd))
    time.sleep(1)


def screen_share(name):
    cmd = ssh_pass(H=get_ip(), U="amcclab", P="amcc1234", C="screen -xr %s" % (name))
    print cmd
    exec_cmd("for i in `screen -ls | grep %s | cut -d. -f1 | awk '{print $1}'`; do echo $i;kill -9 $i; done" % (name),
             debug=False, retry=1)
    exec_cmd("screen -wipe > /dev/null", debug=False, retry=1)
    exec_cmd("screen -AdmS %s -t BMC" % (name), debug=False, retry=1)
    for e in ["PMPR", "ATF", "UEFI", "PMPR_S1", "NPS"]:
        exec_cmd("screen -S %s -X screen -t %s" % (name, e), debug=False, retry=1)
    if args.tty_bmc != "":
        _screen_tty(name, 0, args.tty_bmc, "", "bmc")
    else:
        search_board_type()
        _screen_tty(name, 0, "", ssh_pass(H=args.bmcip, P=args.bmc_pass, U=args.bmc_user, C="bash"), "bmc")

    if args.tty_uefi == "" or args.tty_uefi == "None":
        args.tty_uefi = "1"
    if args.tty_s0cli == "" or args.tty_s0cli == "None":
        args.tty_s0cli = "2"
    if args.tty_atf == "" or args.tty_atf == "None":
        args.tty_atf = "3"
    if args.tty_s1cli == "" or args.tty_s1cli == "None":
        args.tty_s1cli = "4"
    _screen_tty(name, 1, args.tty_s0cli, "", "s0cli")
    _screen_tty(name, 2, args.tty_atf, "", "atf")
    _screen_tty(name, 3, args.tty_uefi, "", "uefi")
    _screen_tty(name, 4, args.tty_s1cli, "", "s1cli")
    x_args = {"cmd": "reset", "bmcip": args.bmcip, "hostip": args.hostip, "hostpass": args.hostpass,
              "hostport": args.hostport, "board_type": args.board_type, "list": "0"}
    _screen_tty(name, 5, "", "echo " + xconsole_args(x_args), "reset")
    if args.hostip != "":
        exec_cmd("screen -S %s -X screen -t HOST" % (name))
        _screen_tty(name, 6, "", ssh_pass(H=args.hostip, U=args.hostuser, P=args.hostpass, C="bash"), "bash")


def search_host_pass():
    if args.hostip != "" and (args.hostuser == "" or args.hostpass == ""):
        for e in g_passw_list:
            re = exec_cmd(ssh_pass(P=e[1], U=e[0], H=args.hostip, C="ls"), debug=False, retry=1)
            if re[0] == 0:
                args.hostuser = e[0]
                args.hostpass = e[1]
                print "hostuser %s" % (args.hostuser)
                print "hostpass %s" % (args.hostpass)
                break


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


def get_centos_info(h):
    re = exec_cmd(ssh_pass(H=h, U='root', P='root', C="ipmitool lan print && dmidecode"), False, retry=1)
    if re[0] == 0:
        return get_line_info(logs=re[1], greps=["IP Address", "Part Number:", "Vendor:"],
                             skips=[" Array ", "Address Source"])
    return None


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

def is_port_open(ip, port):
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)
    ret = socket_obj.connect_ex((ip, port))
    socket_obj.close()
    return ret


def scanip(ip, port):
    ip = ip.split(".")
    ipstart = int(ip[3])
    bmcip = "%s.%s.%s." % (ip[0], ip[1], ip[2])
    print "Start scan IP %s%d to %s%d" % (bmcip, ipstart, bmcip, 255)
    for i in range(ipstart, 255):
        try:
            h = "%s%d" % (bmcip, i)
            if is_port_open(h, port) == 0:
                print h
                re = scanip_fru_print(h)
                if re != None:
                    print re
                else:
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
if args.detect_tty != "":
    detect_tty()
if args.cmd == "reset" and args.bmcip != "":
    BMCReset(args.bmcip)
    sys.exit()
if args.cmd == "mc_reset" and args.bmcip != "":
    ipmitool_exec(ipmitool(args.bmcip) + "mc reset cold")
    sys.exit()
if args.cmd == "on" and args.bmcip != "":
    BMCon(args.bmcip)
    sys.exit()
if args.cmd == "off" and args.bmcip != "":
    BMCoff(args.bmcip)
    sys.exit()
if args.file != "":
    re = cielo_upload(args.file)
    sys.exit(re)
if args.screen != "":
    if args.tty != "":
        e = args.tty.split(",")
        try:
            args.tty_bmc = e[0]
            args.tty_atf = e[1]
            args.tty_s0cli = e[2]
            args.tty_s1cli = e[3]
            args.tty_uefi = e[4]
        except:
            pass
    screen_share(args.screen)
    args.tty = ""
    sys.exit(0)
if args.fru != "":
    if args.bmcip == "" and len(args.fru) > 8:
        args.bmcip = args.fru
    fru_print(args.bmcip)
if args.enable_root != "":
    if args.bmcip == "" and len(args.enable_root) > 8:
        args.bmcip = args.enable_root
    enable_root()
if args.hpm != "" and args.hostport != "":
    re = cielo_upload(args.hpm)
    if re != 0:
        print "cielo_upload %s failed" % (args.file)
if args.list != 0 and args.hostport == "" and args.sol == "":
    if args.hostip != "":
        tty_serials, tty_dmesgs = get_ttydata_ssh(args.hostip, args.hostuser, args.hostpass, args.hostprom)
    else:
        tty_serials, tty_dmesgs = get_ttydata()
    for ttyUSB in list_ttyusb(tty_serials, tty_dmesgs):
        print ttyUSB
if args.hpm != "" and args.bmcip != "" and args.hostport == "":
    cmd = "echo y |" + ipmitool(args.bmcip) + "hpm upgrade " + args.hpm + " force"
    if args.debug:
        print cmd
    print os.system(cmd)
    sys.exit()
if args.tty != "" or args.sol != "" or args.hostport != "":
    tty, re = xconsole(args.bmcip, args.sol, args.hostip, args.hostuser, args.hostpass, args.hostprom, args.hostport,
                       args.tty)
    if args.log != "":
        print args.log
        if os.path.dirname(args.log) != "":
            os.system("mkdir -p %s" % (os.path.dirname(args.log)))
        tty.logfile_read = open(args.log, 'a+')
    if args.hpm != "":
        tty.logfile_read = sys.stdout
        tty.sendline("")
        tty.expect([args.hostport, ">", "Goodbye"], timeout=60)
        tty.sendline("ipmitool -I lanplus -z 0x7fff hpm upgrade " + os.path.basename(args.hpm) + " force")
        re = tty.expect(["y/n", "Continue?"], timeout=10 * 60)
        tty.sendline("yes")
        re = tty.expect(["successful"], timeout=1 * 60 * 60)
        tty.sendline("exit")
        tty.expect([args.hostport, ">", "Goodbye"], timeout=60)
        sys.exit(re)
    if args.cmd != "":
        tty.logfile_read = sys.stdout
        if args.cmd == "reset" and args.hostport != "":
            tty.sendline("ipmitool -I lanplus -z 0x7fff chassis power reset")
        elif args.cmd == "mc_reset" and args.hostport != "":
            tty.sendline("ipmitool -I lanplus -z 0x7fff mc reset cold")
        elif args.cmd == "on" and args.hostport != "":
            tty.sendline("ipmitool -I lanplus -z 0x7fff chassis power on")
        elif args.cmd == "off" and args.hostport != "":
            tty.sendline("ipmitool -I lanplus -z 0x7fff chassis power off")
        else:
            tty.sendline(args.cmd)
        tty.expect([args.hostport, ">"], timeout=1 * 60 * 60)
        tty.sendline("exit")
        tty.expect([args.hostport, ">", "Goodbye"], timeout=60)
        sys.exit()
    if tty != None:
        if args.debug != 0 and args.log == "":
            tty.logfile_read = None
        tty.interact()
        sys.exit()
    else:
        print "ERROR !!!Open console error!!! %s" % (re)
