#!/usr/bin/python
import pexpect
import sys
import os
import datetime
import time
import threading
import argparse
import socket 
from threading import Thread
import traceback
import string
from collections import OrderedDict
import commands

parser = argparse.ArgumentParser(description='cli platform script')

parser.add_argument('--cfg_file', dest='cfg_file',default="",help='load argument via file')

parser.add_argument('--bmcip', dest='bmcip',default="",help='bmcip address')
parser.add_argument('--nps_off', dest='nps_off',default="",help='nps_off')
parser.add_argument('--nps_on', dest='nps_on',default="",help='nps_on')
parser.add_argument('--powertime', dest='powertime',default=15,type=int,help='delay time power OFF/ON')

parser.add_argument('--debug', dest='debug',default=0,type=int,help='print debug out to console')
parser.add_argument('--syscmd_print', dest='syscmd_print',default=1,type=int,help='dump syscmd')
parser.add_argument('--expect_print', dest='expect_print',default=1,type=int,help='dump expect_print')
parser.add_argument('--send_print', dest='send_print',default=2,type=int,help='print send_print')
parser.add_argument('--wrlog_print', dest='wrlog_print',default=0,type=int,help='print wrlog_print')
parser.add_argument('--html_print', dest='html_print',default=1,type=int,help='dump html_print')

parser.add_argument('--time', dest='time',default=15*60*60,type=int,help='Linux test time')
parser.add_argument('--t_expect', dest='t_expect',default=1*60,type=int,help='Linux expect timeout')
parser.add_argument('--ddr_init_timeout', dest='ddr_init_timeout',default=10*60,type=int,help='ddr_init_timeout')
parser.add_argument('--linux_boot_timeout', dest='linux_boot_timeout',default=10*60,type=int,help='linux_boot_timeout')
parser.add_argument('--loop', dest='loop',default=1,type=int,help='number loop of test')
parser.add_argument('--sub_loop', dest='sub_loop',default=1,type=int,help='loop when test pass')

parser.add_argument('--hostip', dest='hostip',default="",help='Host IP address')
parser.add_argument('--hostuser', dest='hostuser',default="",help='Host user')
parser.add_argument('--hostpass', dest='hostpass',default="",help='Host pass')
parser.add_argument('--hostprom', dest='hostprom',default="~",help='Host prom')
parser.add_argument('--hostport', dest='hostport',default="",help='cieal port')

parser.add_argument('--tty_atf', dest='tty_atf',default="",help='tty_s1pcli console')
parser.add_argument('--tty_s0cli', dest='tty_s0cli',default="",help='tty_s1pcli console')
parser.add_argument('--tty_s1cli', dest='tty_s1cli',default="",help='tty_s1cli console')
parser.add_argument('--tty_uefi', dest='tty_uefi',default="",help='tty_uefi console')
parser.add_argument('--tty_bmc', dest='tty_bmc',default="",help='tty_bmc console')
parser.add_argument('--sensor_bg', dest='sensor_bg',default=0,type=int,help='dump sensor')
parser.add_argument('--sensor_interval', dest='sensor_interval',default=30,type=int,help='sensor_interval')

parser.add_argument('--sol', dest='sol',default=0,type=int,help='force to use SOL')
parser.add_argument('--sol_uefi', dest='sol_uefi',default="1",help='sol_uefi')
parser.add_argument('--sol_s0cli', dest='sol_s0cli',default="2",help='sol_s0cli')
parser.add_argument('--sol_atf', dest='sol_atf',default="3",help='sol_atf')
parser.add_argument('--sol_s1cli', dest='sol_s1cli',default="4",help='sol_s1cli')
parser.add_argument('--nvparam_102', dest='nvparam_102',default="",help='nvparam_102')
parser.add_argument('--nvparm_board_setting', dest='nvparm_board_setting',default="",help='nvparm_board_setting')
parser.add_argument('--sel_list', dest='sel_list',default=0,type=int,help='sel_list')
parser.add_argument('--cli_startup', dest='cli_startup',default="mdw -l 0x50002d14,mdw -l 0x50002d18",help='cli_startup')
parser.add_argument('--startup_cmd', dest='startup_cmd',default="lspci,lsscsi,dmidecode,dhclient -v",help='startup_cmd')
parser.add_argument('--cli_err_break', dest='cli_err_break',default=100,type=int,help='cli_err_break')

parser.add_argument('--board', dest='board',default="",help='name of board')
parser.add_argument('--note', dest='note',default="",help='note')

parser.add_argument('--linux_script', dest='linux_script',default="",help='linux_script')
parser.add_argument('--linux_pwd', dest='linux_pwd',default="/var/tmp",help='linux_pwd')
parser.add_argument('--wget_href', dest='wget_href',default="http://10.38.19.97:2021/download",help='wget_href')

parser.add_argument('--sendfile', dest='sendfile',default="",help='send file to Linux via UART/SOL')

parser.add_argument('--wait', dest='wait',default=1,type=int,help='check bmcip before start')

parser.add_argument('--flash_fw', dest='flash_fw',default=1,type=int,help='enable flash_fw file')
parser.add_argument('--bios_fw', dest='bios_fw',default="",help='hpm file')
parser.add_argument('--scp_fw', dest='scp_fw',default="",help='scp_fw file')
parser.add_argument('--bmc_fw', dest='bmc_fw',default="",help='bmc_fw file')
parser.add_argument('--enable_root', dest='enable_root',default=0,type=int,help='enable_root file')
parser.add_argument('--atfbios_fw', dest='atfbios_fw',default="",help='atfbios_fw file')
parser.add_argument('--hpm_to_img', dest='hpm_to_img',default="",help='hpm_to_img')

parser.add_argument('--cmd', dest='cmd',default="",help='exec xconsole cmd')
parser.add_argument('--start_test', dest='start_test',default=0,type=int,help='Enable start_test')

parser.add_argument('--sys_log', dest='sys_log',default="",help='www')

parser.add_argument('--cleannv', dest='cleannv',default=0,type=int,help='clean all nv')

parser.add_argument('--board_type', dest='board_type',default="",help='import board to platformtools')


parser.add_argument('--nv', dest='nv',default="",help='nvparam name')
parser.add_argument('--nv_def', dest='nv_def',default=1,type=int,help='nvparam def')
parser.add_argument('--nv_scan', dest='nv_scan',default="",help='nvparam nv_scan')
parser.add_argument('--retry', dest='retry',default=2,type=int,help='retry ssh cmd')

parser.add_argument('--web_link', dest='web_link',default="",help='web link')
parser.add_argument('--port', dest='port',default=1234,type=int,help='port')

parser.add_argument('--log_cycle', dest='log_cycle',default="",help='TEST code')
parser.add_argument('--time_power_cycle', dest='time_power_cycle',default="",help='time_power_cycle')
parser.add_argument('--time_start_test', dest='time_start_test',default="",help='time_start_test')

parser.add_argument('--board_cfg', dest='board_cfg',default="",help='board_cfg')
parser.add_argument('--test_cfg', dest='test_cfg',default="",help='test_cfg')

parser.add_argument('--test_case', dest='test_case',default="",help='test_case')
parser.add_argument('--exit_on_fail', dest='exit_on_fail',default="",help='exit_on_fail')
parser.add_argument('--break_on_fail', dest='break_on_fail',default=0,type=int,help='break_on_fail')

parser.add_argument('--eye_type', dest='eye_type',default="",help='eye_type wrdq,rdfall,rdrise for DMTe2')
parser.add_argument('--eye_type_e2', dest='eye_type_e2',default="wrdq,rdfall,rdrise",help='eye_type_e2 wrdq,rdfall,rdrise for DMTe2')
parser.add_argument('--eye_x', dest='eye_x',default="",help='eye_x ENV_DDR_DRAM_VREF_ADJ DMTe2')
parser.add_argument('--eye_x_value', dest='eye_x_value',default="-80:80:4",help='eye_x_value [-80:-80:4] DMTe2' )
parser.add_argument('--eye_y', dest='eye_y',default="",help='eye_y ENV_DDR_PHY_VREF_ADJ DMTe2')
parser.add_argument('--eye_y_value', dest='eye_y_value',default="-24:24:2",help='eye_y_value [-24:24:2] DMTe2')
parser.add_argument('--sk', dest='sk',default="",help='sk')
parser.add_argument('--mcu_mask', dest='mcu_mask',default="",help='mcu_mask')
parser.add_argument('--rank_mask', dest='rank_mask',default="",help='rank_mask')
parser.add_argument('--slice_mask', dest='slice_mask',default="",help='slice_mask')
parser.add_argument('--dmt_addr', dest='dmt_addr',default="",help='dmt_addr')
parser.add_argument('--dmt_size', dest='dmt_size',default=1,type=int,help='dmt_size')

parser.add_argument('--fan', dest='fan',default="",help='fan')

parser.add_argument('--fail_signal', dest='fail_signal',default="cfg/test_cfg/fail_signal.cfg",help='fail_signal')
parser.add_argument('--known_issues', dest='known_issues',default="cfg/test_cfg/known_issues.cfg",help='known_issues')
parser.add_argument('--expect_signal', dest='expect_signal',default="",help='expect_signal')

parser.add_argument('--scp_fw_upgrade', dest='scp_fw_upgrade',default="amp_hostfw_update -c  2 -b 12 -s 50 -t 4 -f,amp_hostfw_update -c  2 -b 12 -s 50 -t 4 -f",help='scp_fw_upgrade')
parser.add_argument('--bios_fw_upgrade', dest='bios_fw_upgrade',default="amp_hostfw_update -c  1 -f ",help='amp_hostfw_update')
parser.add_argument('--tty_send_interval', dest='tty_send_interval',default=0,type=int,help='tty_send_interval')

global args
def get_eye_size(value):
    values =  value.replace("[","").replace("]","").split(":")
    return int(values[0],0),int(values[1],0),int(values[2],0)
def is_enable_sk(log,sk=1):
    if log.find("CP: %d"  %(sk)) != -1:
        return True
    return False
def get_mcu_mask(log,sk):
    dimm_mask = 0
    for mcu in range(0,9):
        if log.find("CP: %d%d"  %(sk,mcu)) != -1:
            dimm_mask = dimm_mask | (1<< mcu)
    return "0x%08x" %(dimm_mask)
def get_rank_mask(log,sk):
    rank_mask = 0
    for mcu in range(0,9):
        for rank in range(0,9):
            if log.find("CP: %d%d%d" %(sk,mcu, rank))!= -1:
                rank_mask = rank_mask | (1<< rank)
    return "0x%08x" %(rank_mask)
def get_add_map(log,sk,region=2):    
    return find_in(log,"Node[%d] Region[%d]: " %(sk,region)," - ")
def aeroe2_dmt():
    global uefi,g_uefi_log 
    re = None,None
    for e in ["ddrinit","ecc_dis","mkddrcache"]:
        _send(uefi,e)
        re = _expect(uefi,[e],timeout=args.time)
        if re != 0:
            return "ERROR",e
        re = _expect(uefi,["AEROe2>"],timeout=args.time)
        if re != 0:
            return "ERROR",e
    if args.sk =="":
        if is_enable_sk(g_uefi_log,sk=1): 
            args.sk = "0,1"
        else: 
            args.sk = "0" 
    for eye_type in args.eye_type_e2.split(","):
        for sk in args.sk.split(","):
            if args.mcu_mask =="":
                args.mcu_mask = get_mcu_mask(g_uefi_log, int(sk))
            if args.rank_mask =="":
                args.rank_mask = get_rank_mask(g_uefi_log, int(sk))
            if args.slice_mask == "":
                args.slice_mask = "0x1ff"
            if args.dmt_addr == "":
                for region in [5,4,3,2,1]:    
                    args.dmt_addr = get_add_map(g_uefi_log, int(sk), region=region) 
                    if args.dmt_addr != "":
                        break
            for mcu_mask in args.mcu_mask.split(","):
                for rank_mask in args.rank_mask.split(","):
                    for slice_mask in args.slice_mask.split(","):
                        for dmt_addr in args.dmt_addr.split(","):
                            re = AEROe2(uefi,eye_type,sk,mcu_mask,rank_mask,slice_mask,dmt_addr)
    return re
def AEROe2(tty,eye_type,sk,mcu_mask,rank_mask,slice_mask,dmt_addr):
    if eye_type == "wrdq":
        eye_y = "dimm"
    else:
        eye_y = "phy"
    eye_x_start,eye_x_end,eye_x_step = get_eye_size(args.eye_x_value)
    eye_y_start,eye_y_end,eye_y_step = get_eye_size(args.eye_y_value)
    dmte2_cmd = "eye -p %s -x %s -y %s" %(sk,eye_type,eye_y)
    dmte2_cmd = "%s -l %d -r %d -s %d" %(dmte2_cmd,eye_x_start,eye_x_end,eye_x_step)
    dmte2_cmd = "%s -b %d -t %d -f %d" %(dmte2_cmd,eye_y_start,eye_y_end,eye_y_step)
    dmte2_cmd = "%s -M %s -R %s -N %s -B 0xff" %(dmte2_cmd,mcu_mask,rank_mask,slice_mask)
    dmte2_cmd = "%s -T 24 -a %s -S 0x%x" %(dmte2_cmd,dmt_addr,(args.dmt_size<<30))
    _send(tty,dmte2_cmd)
    if _expect(tty,[dmte2_cmd],timeout=args.time,debug=1) != 0:
        return "ERROR:send %s" %(dmte2_cmd),None
    
    re = _expect(tty,["VREF/Level"],timeout=args.time)
    if re < 0:
        return "ERROR: expect VREF/Level",None
    if args.debug == 0:
        tty.logfile_read = sys.stdout
    re = _expect(tty,["AEROe2>"],timeout=args.time)
    if re < 0:
        return "ERROR: expect AEROe2",None
    if args.debug == 0:
        tty.logfile_read = None
    if re >= 0 :
        eye = find_in(tty.before,"","2D ")
        if eye != "":
            return dmt_2deye_html(eye,eye_type,eye_type)
        return "ERROR:Can't find eye %d" %(args.time),None
    else:
        return "ERROR:Timeout %d" %(args.time),None
def dmt_2deye_nv_cfg(eye_type):
    nv = {"SI_PLT_EN":1}
    if eye_type == "rdrise":
        nv.update({"SI_PLT_X_PARAM":1})
        nv.update({"SI_PLT_Y_PARAM":1})
    elif eye_type == "rdfall":
        nv.update({"SI_PLT_X_PARAM":2})
        nv.update({"SI_PLT_Y_PARAM":1})
    elif eye_type == "wrdq":
        nv.update({"SI_PLT_X_PARAM":3})
        nv.update({"SI_PLT_Y_PARAM":2})
    elif eye_type == "adcmd":
        nv.update({"SI_PLT_X_PARAM":6})
        nv.update({"SI_PLT_Y_PARAM":1})
    if args.eye_x !="":
        nv.update({"SI_PLT_X_PARAM":args.eye_x})
    if args.eye_y !="":
        nv.update({"SI_PLT_Y_PARAM":args.eye_y})
    left,right,step = get_eye_size(args.eye_x_value)
    nv.update({"SI_PLT_X_LEFT":left})
    nv.update({"SI_PLT_X_RIGHT":right})
    nv.update({"SI_PLT_X_STEP":step})
    bottom,top,step = get_eye_size(args.eye_y_value)
    nv.update({"SI_PLT_Y_BOTTOM":bottom})
    nv.update({"SI_PLT_Y_TOP":top})
    nv.update({"SI_PLT_Y_STEP":step})
    nv.update({"SI_DDR_ECC_MODE":0})
    nv.update({"SI_RAS_BERT_ENABLED":1})
    nv.update({"SI_S1_PCP_ACTIVECPM_0_31":0xFFFFFFFF})
    nv.update({"SI_S1_PCP_ACTIVECPM_32_63":0xFFFFFFFF})
    nv.update({"SI_S0_PCP_ACTIVECPM_0_31":0xFFFFFFFF})
    nv.update({"SI_S0_PCP_ACTIVECPM_32_63":0xFFFFFFFF})
    nv.update({"SI_DDR_ZQCS_EN":0x0})
    nv.update({"SI_DDR_SCRUB_EN":0x0})
    nv.update({"SI_RO_BOARD_S1_DIMM_AVAIL":0xFFFF})
    nv.update({"SI_RO_BOARD_S0_DIMM_AVAIL":0xFFFF})
    print "SI_PLT_MCU_MASK %s" %(args.mcu_mask)
    if args.sk != "":
        nv.update({"SI_PLT_SOCKET":args.sk})
    if args.mcu_mask !="":
        nv.update({"SI_PLT_MCU_MASK":args.mcu_mask})
    if args.rank_mask !="":
        nv.update({"SI_PLT_RANK_MASK":args.rank_mask})
    if args.slice_mask !="":
        nv.update({"SI_PLT_BIT_MASK":args.slice_mask})
    c = ""
    for e in nv:
        c = c + set_nvparam_cmd(e,int(str(nv[e]),0))
    if c != "":
        re = set_nvparm(c)
        return re
    return set_exec_cmd_fail("dmt_2deye_nv_cfg")
def platform_mem_tool():
    global uefi,g_uefi_log
    re = _expect(uefi, ["saved leveling"], timeout=2*60)
    if re < 0:
        return "ERROR:_expect saved leveling",None
    try:
        x_param = find_in(g_uefi_log, "X-param:\t\t","\r\n") 
        y_param = find_in(g_uefi_log, "Y-param:\t\t", "\r\n")
        eye_name = "%s" %(cfg2id(g_configure,"loop"))
        msg = "%s/%s Level" %(y_param,x_param)
        re = _expect(uefi, [msg])
        if args.debug < g_loop_count:
            uefi.logfile_read = sys.stdout
        re = _expect(uefi, ["Waiting for reboot"],timeout=args.time)
        if args.debug < g_loop_count:
            uefi.logfile_read = None
        eye_2d_str = find_in(g_uefi_log, msg, "Waiting for reboot")
        #get_dly_param()
        return dmt_2deye_html(eye_2d_str,eye_name,x_param)
    except:
        print traceback.print_exc()
        return "ERROR:Can't detect eye param",None
def dmt_2deye_html(eye_2d_raw,eye_name,x_param):
    re = ""
    x_left,x_right,x_step = get_eye_size(args.eye_x_value)
    y_bottom,y_top,y_step = get_eye_size(args.eye_y_value)
    eye_2d = eye2d(eye_2d_raw)
    if (eye_name in g_eye2d) == False :
        g_eye2d[eye_name] = eye_2d
    else:
        g_eye2d[eye_name] = add(g_eye2d[eye_name],eye_2d)
    eye_x_value_list = [i for i in range(x_left,x_right + x_step,x_step)]
    eye_y_value_list = [i for i in range(y_bottom,y_top + y_step,y_step)]
    if x_param.lower().find("wrdq") == 0:
        eye_x_mask = 16/x_step
        eye_y_mask = 4/y_step
    else:
        eye_x_mask = 16/x_step
        eye_y_mask = 8/y_step
    eye_html = raw_eye_to_html(x_param,g_eye2d[eye_name],eye_x_value_list,eye_y_value_list,eye_x_mask,eye_y_mask)
    if eye_html.find("eye_fail_mask") != -1:
        re = "FAIL"
    elif eye_html.find("eye_pass_mask") != -1:
        re = "PASS"
    else:
        re = "FAIL"
    wr_report(html_dict({eye_name:eye_html},w3_border_en=True))
    wr_report(html_dict({"status":re},w3_border_en=True))
    return re,eye_html
def to_do(e):
    print "to_do %s" %(str(e))
def do_exit(msg="",err=0):
    if err != 0:
        print "__ERROR__: %s" %(msg)
    else:
        print "__DONE__: %s" %(msg)
    sys.exit(err)
def open_file(filename):
    try:
        f = open(filename, "r")
        text=f.read()
        f.close()
        return text;
    except:return ""
def ascii(text):
    try:
        return ''.join([x for x in text if x in string.printable])
    except:
        return text
def wrlog(msg,name="",_print = 1):
    try:
        os.system("mkdir -p %s" %(os.path.dirname(name)))
        filename = "%s" %(name)
        if args.wrlog_print != 0 and _print != 0:
            print "wrlog %s %s" %(msg,name) 
        f=open(filename, "a+")
        f.write("%s" %(msg))
        f.close()
    except:
        print "ERR wrlog %s " %(name)
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
def nv_args(sys_cmd,key="--nv_scan"):
    sys_cmd = sys_cmd +" "
    nv = ""
    args_split = sys_cmd.split(key)
    for i in range(1,len(args_split)):
        a = find_in(args_split[i]," "," ")
        sys_cmd = _replace(sys_cmd,{key + " " + a + " ":""})
        nv = "%s%s," %(nv,a)
    nv = nv[0:len(nv) - 1]
    if nv != "":
        sys_cmd = sys_cmd + key + " " + nv
    return sys_cmd
def get_loop_element(DATA,value,i):
    data_len = []
    count = []
    for e in reversed(DATA):
        data_len.append(len(DATA[e]))
        count.append(0)
    for j in range(0,len(data_len)):
        count[j] = int( i%(data_len[j]))
        i = int (i/data_len[j])
    j = -1
    for e in reversed(DATA):
        j = j + 1
        if e == value: return DATA[value][count[j]],count[j]
    return None,None

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
                    if args.nvparam_102 != "":
                        offset = value | 0xE30000
                    else:
                        offset = value | 0x110000
                    continue
                elif name == "MANU_PARAM_START":
                    if args.nvparam_102 != "":
                        offset = value | 0xE30000
                    else:
                        offset = value | 0x110000
                    continue
                elif name == "USER_PARAM_START":
                    if args.nvparam_102 != "":
                        offset = value | 0xE30000
                    else:
                        offset = value | 0x110000
                    continue
                elif name == "BOARD_PARAM_START":
                    if args.nvparam_102 != "":
                        offset =  0x1F0000
                    else:
                        offset = (value | 0x5F0000) -(0xC000)
                    continue
                value = value + offset
                if name !="" and value != 1:
                    NVPARAM[name] = value
        except:
            pass
    return NVPARAM
def set_exec_cmd_fail(msg="exec_cmd_fail"):
    return -1,msg
def get_exec_cmd_status(re):
    return re[0]
def get_exec_cmd_log(re):
    return re[1]
def exec_cmd(e,do_quit=True,do_print=True):
    global g_loop_count
    for i in range(0,args.retry):
        if do_print:
            if args.syscmd_print != 0 or args.debug > g_loop_count:
                print "exec_cmd %s" %(e)
            wrlog(e+"\n", "%s/%s" %(get_log_dir(),"test_exec.sh"))
        re = commands.getstatusoutput(e)
        if args.debug >= g_loop_count and e.find("ps") != 0:
            print re[1]
        if re[0] != 0:
            print re[1]
        if re[0] == 0 :
            return re
        if (i + 1) == args.retry:
            print "retry %s" %(args.retry)
    if re[0] != 0 and do_quit == True:
        do_exit("exec_cmd %s" %(e), 1)
    return re
def now():
    return str(datetime.datetime.today().strftime('%y%m%d_%H%M%S'))
def check_ip_alive(ip):
    if ip == "" :
        return True
    for i in range(0,args.retry):
        socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        ret = socket_obj.connect_ex(("%s" %(ip),22))
        socket_obj.close()
        if ret == 0 :
            return True
        if i == args.retry:
            pass
    return False
def get_pid(ps,i=1):
    j = 0
    for e in ps.split(" "):
        if e != "" :
            if i == j:
                return e
            j = j + 1
    return ""
def mkdir(pwd):
    exec_cmd("mkdir -p " + pwd,False,False)
    exec_cmd("chmod 777 " + pwd,False,False)
    return dir
def html_header(title,do_print=True):
    h = ""
    h = h + "<!DOCTYPE html>"
    h = h + "<html lang='en'><head><title>"+ title +"</title><link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'><script src='https://cdn.jsdelivr.net/npm/chart.js@2.8.0'></script>"
    h = h + "<style>.eye_main {width:100%;}.eye_element {width:25%;}.eye_table {width:80%;}.eye_fail {background-color: Purple;}.eye_fail_mask {background-color: DarkRed;}.eye_pass {background-color: YellowGreen;}.eye_pass_mask {background-color: ForestGreen;}.eye_title {background-color: whilte;}.eye_hw {background-color: aqua;}.eye_point{width:auto;}.overflowTest {padding: 15px;width: auto;height: 600px;overflow: scroll;border: 1px solid #ccc;}</style>"
    h = h + "</head><body><h1 align='center'><img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAABzZJREFUeNrsXc11IjkYlPuyV4eAN4Gxb3tbHMHYERgiwESAiQAcAUwEw0YAc9vbEMFCCFz35JV2PvzaGEmf/roluuo9nneNp7vpqq/0qVp0X729vQmgu7iCACAAnAUIAIAAAAgAgAAACACAAAAIAIAAAAgAgAAACACAAAAIAIAAAAgAgAAACACAAAAIAIAAAAgAgACAcqEEcPoCePj3j9978jUrmmsIIEgAC/l6k69+qQI4OwRcXV2BXUb1yx87+t/Nb3//c1+CAE5RgUpvLGr/3S/FBVhNIBzAWv2K7PXJr/fSBW7gAN3A5MzvVEM4gANcfvUPTuz/gwvI1510ggMcoFvV/+4C8vUMB7jc6lfk2ub9qvpvcnQBOEAY+deW6j+C+3dZAALg45nIZf0t5QQYAi6k+hWZO8d/tpTDwBBDwOU3fjoMSgiHIAB79d8qMg0N3zyycCCAzGDq+l/la0rz/3PIPiKGAMzVr8jrm6qfpntTTwFBAAVX//g415c/lwYXuM05IoYA9NWvSLvVvL0n0usYltgLQAB+pI1PfyEFsZE/Npq/VxeKXiCAcqpfkdXTvK0Wf6w075l6gRGliRBA5uQrkkaGP9GSTC6w1LyttvsMAZRh/bpKXRLJwkcgatu5RcQQwMfq71mqdGrbhhTI3uAC2TWEEACfnDmRy8GYcoJzGFC6CAFkVv19YY58p9xtUT7w6pkvQAAZVv+rxwKPucEFsomIIQBhjXz3wnzBx+QC49xdAAL4hYWp8fNd3lVCRFyh+v8nQTc1Oxf5umKc84yg6jj5tvV7wSt6KDXUZQc9WmgKAbSEZ2GOfDeR9mMLh64hgHaqf+RJmqsLKCHprh+0GhF32QFCI9+YvcCorYi46mj190Rg5OvhAmo2sDS4wAQCaA4zy7Rvn2i/toi4BwGkr/6+/PGgedu2yjfUBWwR8QICaGbs1+G1ge/0ZRURVx2rflX5uhOsQp+X1MfAWEU8gQBaGvubOggpAuUCe4MLDCCA+NWvTqquydpGiHxdkYULVB0h/9pS/eOmj4kEp8saGouIu+IApq92bxKEPlFcoImIuOpI9Y9yqv6aC2wMLtBIRNwFB5gJc+S7bfn4TFcck0fE1YVXvzp5gxw6f4MLqNnA0uACSRvCi7xDCIUpivwnw7x/ypn3H1fwpnQKEupPg1PdxIinz3JdugBojFcBzxcim7PkmnUnL9r2rkaMGq9/qGkjNY+HiJ/jxVDtK7mvRwjgY1Uq0r8yCf/U+FEYE0LKURB/EUH7CELeGVzgPnS2UrQAyCYfqKMPaYzY9/SV+9w57Eu5wrcQMVjuQxh8R/IiBUD5/ZPQX8Fz7ro5qZ/llrA2qNU/3wzfIvYV3aPPNosUABEwCax27ypyrH6t24hfl3+X3H7Bdi/ikDuSFyGARMQ7jaPUY8zoGGIcx3EdwJwjBLn/tWH2MvS9bpG1ACIQf6jNnaONodSc3RIhfxqIiSYEzfMInGYwxQiAPuzMs5vfHrtwOjHJ59K1Y/5KfUnPUwhT00zE4gJTn7ULWQmgdoVu4DGuKsJf64SqBzgZtpXstq00XDzRvq89Psvw3LBE2/0Z0wWyEQBNdyaOJ2xDpK80U8Sd4WTdJVzoeTqMPXkMEysSwuFke1FF3boAiKiF4wlaEvHbJu0ygiuMHN3t07DAuEm107DWqgBoPr9wqHpVFWPbB0zVMEUU/MRRCBtygz1t40VEiohbEYDHWL+hStgwt2+qflbk25AQZg5h1oFEsIoZETcuALLCheBfoBm7zHFThiaZzHjUuVALVp4NLsCe3jb6vACy/DXzw87Jql0DDqe7ebYNVanydSfM3xCqY0DncCUS3ZE8iQMwrqJZp0GB+8j+Ua5k7QvmsHCgofEhxO2SDwGO4/1ceN5+pYlLpw0KwbU51sEaEScVAJHCsfz3BieRw0RZPNGCG3wXYTHzXlgeWpmsB6ilVjbyt3SQIeT3Shv7Gb3BgYaskGPvCY9VxMEOQOSvGRYWJY5tK/JtOET6LvyvMWhzj+gO4ED+MBL5tgc4jUXhoMTzTui/L2CC8ypibwdgkq9IeYzVkOUW+TbgBjPh9+WQsxFxNAdgkr+P2Y1zHuAkLgzy3ClH83HOSTIHYJK/JfJjLps2NZnDFr7d26QT9KkvcJkqfiq+4Glgi+QPREGRb8LmcO0ggk9hWNAQ0Bb5DEsbiw6AmsN7OsccsCLiKiL5qxTkBzzACSJgLGu3DgGM2DXZ/PuSIt8E54V7oe29P3IeAmo7Mtp+wvCl6bt5luIEBwcnmIQMATaVHS0phcp7ouG7eV6oCIwPrawMBCw45CdcbhXrAU5dEIGNA+1DKytD4zVoi3xG5DsVgIsItLebOdsEAt0BBAABQAAQAAABABAAAAEAEAAAAQAQAAABABAAAAEAEAAAAQAQAAABABAAAAEAEAAAAQAQAAABABAAAAEA5eI/AQYANT2i2iNsRMcAAAAASUVORK5CYII=' scale='0'></h1>"
    h = h + "<p align='center'><font size='7' color='blue'><span>"+ title +"</span></font></p>"
    if do_print:
        print h
    return h
def w3_dropdown_hover(html,title="Hover over me!"):
    return "<div class='w3-dropdown-hover'>" + title + "<div class='w3-dropdown-content w3-green w3-padding'>" + html + "</div></div>"
def w3_border(msg):
    return "<div class='w3-panel w3-border-left w3-border-blue'>" + msg + "</div>"
def html_dict(_dict,href="",do_print=True,w3_border_en=False,w3_dropdown_hover_en=False):
    if args.html_print == 0:
        for e in _dict:
            print "%s %s" %(e,_dict[e])
    h =     "<div class='w3-container'> "
    for e in _dict:
        v_raw = "__start__%s %s__end__" %(e,_dict[e])
        h = h + "<div hidden>\n" + v_raw.replace("\n","<br>") + "\n</div>"
        if href !="":
            v = "<a href='%s'>%s</a>" %(href,_dict[e])
        else:
            v = str(_dict[e])
        v = v.replace("\n", "<br>")       
        h = h + "<div class='w3-light-blue'> <br> </div>"
        h = h + "<div class='w3-row '>"
        h = h + "    <a class='w3-col m3 show-white-space' style='white-space: pre-line' >%s</a>" %(e)
        if v.find("PASS") != -1:
            ext_class ="w3-text-blue"
        elif v.find("FAIL") != -1:
            ext_class ="w3-text-red"
        else:
            ext_class=""
        h = h + "    <a class='w3-col m9 show-white-space %s' style='white-space: pre-line' >%s</a>"  %(ext_class,v)  
        h = h + "</div>"
    h = h + "</div>"
    if w3_border_en:
        h = w3_border(h)
    if w3_dropdown_hover_en:
        h = w3_dropdown_hover(h)
    if do_print:
        print h
    return h
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def set_nvparam_cmd(n,v=None):
    c = ""
    if n in g_nvparm:
        if v == None:
            c = "%s[%s:%s:%s]" %(c,n,g_nvparm[n],"read")
        else:
            c = "%s[%s:%s:%s]" %(c,n,g_nvparm[n],tohex32(v))
            return c
    else:
        do_exit("set nvparam_cmd %s" %(n), 1)

def set_nvparm(nv_cmd):
    return exec_cmd(xconsole_args({"set_nvparm":nv_cmd}))

def xconsole_args(arg):
    arg.update({ "nps_on":args.nps_on,"nps_off":args.nps_off,
                 "nvparam_102":args.nvparam_102,"hpm_to_img":args.hpm_to_img,
                 "bmcip":args.bmcip,"hostip":args.hostip,
                 "hostuser":args.hostuser,"hostpass":args.hostpass,
                 "hostport":args.hostport,"board_type":args.board_type})
    c = "./xconsole.py"
    for e in arg:
        if arg[e] =="" or arg[e] =="None":
            pass
        else:
            c = "%s --%s %s" %(c ,e,arg[e])
    return c

def xconsole(tty="",note=""):
    global g_loop_count
    log = "%s/%s" %(get_log_dir(),get_log_name(note + ".log"))
    xconsole_cmd = xconsole_args({"tty":tty,"note":note,"log":log})
    if args.syscmd_print != 0:
        print xconsole_cmd   
    tty = pexpect.spawn(xconsole_cmd,timeout=300000)
    if args.debug >= g_loop_count:
        tty.logfile_read = sys.stdout
    return tty
        
def _expect(tty,pattern,timeout=5*60,debug=None,is_uefi=True):
    global g_uefi_log,g_cli_log
    if debug == None:
        debug = args.expect_print
    start_time = time.time()
    if args.debug !=0 and debug != 0:
        print "_expect ",
        print  (pattern),
        print "[%d]" %(timeout)
    try:
        re = tty.expect(pattern,timeout)
        if is_uefi:
            g_uefi_log="%s%s%s" %(g_uefi_log,tty.before,pattern[re])
        else:
            g_cli_log="%s%s%s" %(g_cli_log,tty.before,pattern[re])
        if args.log_cycle!="":
            wrlog(ascii("%s%s" %(tty.before,pattern[re])),args.log_cycle)
        if args.debug !=0 and debug != 0:
            elapsed_time = time.time() - start_time
            x=time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            print ("[expected=%s %s]" %(_replace(pattern[re]),x))
        return re
    except KeyboardInterrupt:
        return -2
    except:
        return -1
def _send(tty,msg):
    if args.debug !=0 or args.send_print != 0:
        print "|_send %s [%s]" %(msg,now())
    for e in msg:
        tty.send(e)
        if args.tty_send_interval != 0:
            time.sleep(args.tty_send_interval/1000)
    tty.sendline("")
def tohex32(v):
    return _replace(hex(v & (2**32-1)).upper(),{"X":"x"})
def bitMask(h, l):
    i = 0xFFFFFFFF;
    return ~(i << h << 1) & (i << l)
def name_format(name):
    name = _replace(name)
    name = _replace(name,{" ":"","/":""})
    name = _replace(name,{"[":"","]":""})
    return name
def ln_log_ddr_info(log_dir,ddr_info):
    mkdir("logs/ddr_info/%s" %(ddr_info))
    os.system("ln -sf %s/%s logs/ddr_info/%s" %(os.getcwd(),log_dir,ddr_info))    
def ln_log_test_cfg(log_dir):
    if args.test_cfg != "":
        mkdir("logs/%s" %(args.test_cfg))
        os.system("ln -sf %s/%s logs/%s" %(os.getcwd(),log_dir,args.test_cfg))    
def get_log_dir():
    if args.sys_log !="":
        log_dir = _replace(args.sys_log,{".log":""})
    else:
        log_dir = "logs/%s/%s/%s" %(args.board_type,args.board_cfg,args.test_cfg)
    mkdir(log_dir)
    return  log_dir
def get_log_name(ext=".txt"):
    global g_configure
    global g_loop_count
    log_name = args.board_cfg 
    if args.test_case != "":
        log_name ="%s_%s"  %(log_name,args.test_case)
    if args.test_cfg != "":
        log_name ="%s_%s"  %(log_name,args.test_cfg)
    if g_loop_count !="":
        log_name ="%s_at_%s"  %(log_name,g_loop_count)
    if args.time_power_cycle !="":
        log_name ="%s_%s"  %(log_name,args.time_power_cycle)
    log_name ="%s%s" %(log_name,ext)
    return log_name
def BMC_sel_list(i):
    global g_loop_count
    if args.sel_list != 0:
        re = exec_cmd(xconsole_args({"cmd":"sel_list"}))
        sel_list_log_cycle = "%s/sel_list-%s-%s.%s.log" %(get_log_dir(),args.test_case,g_loop_count,i)
        wrlog(get_exec_cmd_log(re),sel_list_log_cycle)
def BMCoff():
    args.time_power_cycle = now()
    print "CHASSIS POWER OFF"
    exec_cmd(xconsole_args({"cmd":"off"}))
    BMC_sel_list(0)
def BMCon():
    global g_loop_count
    args.log_cycle = "%s/%s" %(get_log_dir(),get_log_name())
    wr_report(html_dict({"CHASSIS POWER ON %s" %(g_loop_count):args.time_power_cycle},href="/%s" %(args.log_cycle),w3_border_en=True))
    exec_cmd(xconsole_args({"cmd":"on"}))

def nv_get_value(n):
    pass
def nv_value(n,e):
    highbit=31
    lowbit=0
    if e.find("][") != -1:
        highbit = int(find_in(e,"[","][").split(":")[0])
        lowbit = int(find_in(e,"[","][").split(":")[1])
        v = find_in(e,"][","]")
    elif e.find("[") != -1 and e.find("]") != -1:
        v = find_in(e,"[","]")
    else:
        v = e
    if v.find(".") != -1:
        v = [int(i,0) for i in v.split(".")]
    elif v.find(":") != -1:
        r = v.split(":")
        v = [i for i in range(int(r[0]),int(r[1]),int(r[2]))]
    else:
        v = [int(v,0)]
    if highbit == 31 and lowbit == 0:
        return v
    else:
        x = nv_get_value(n)
        v = [ (i<< lowbit)|(x & int(tohex32(~bitMask(highbit,lowbit)),0))  for i in v]
    return v
def nv_name(a):
    NV=OrderedDict()
    e_ = ""
    for e in reversed(a.split(",")):
        if e.find("[") != -1:
            e_ = e.split("[")[0]
            v = "["+find_in(e,"[","")
            NV[e_] = nv_value(e_,v)
        else:
            NV[e] = "-"
            e_ = e 
    return NV 
def __bg_start(th,msg=""):
    bg = Thread(target = th, args = (msg,))
    bg.do_run = True
    bg.start()
    return bg
def __bg_stop(bg):
    if bg == None:
        return
    try:
        bg.do_run = False
        bg.join()
    except:
        print "except stop th"
        
def cli_th(tty):
    PMPRO_EXPECT = ["SMpro ready","Runtime Firmware","-cli>","\n","Error: "]
    global g_cli_status,g_uefi_log
    t = threading.currentThread()
    g_cli_status = 0xffff
    re = 0
    if tty == None:
        return
    one_time = True
    while getattr(t, "do_run", True):
        re = _expect(tty,PMPRO_EXPECT,timeout=3,debug=0,is_uefi=False)        
        if re < 0 :
            continue
        if PMPRO_EXPECT[re] == "\n":
            continue
        if re == 0 or re == 1:
            g_cli_status = 0
        if PMPRO_EXPECT[re] == "-cli>":
            if one_time:
                one_time = False
                for e in args.cli_startup.split(","):
                    if e != "":
                        tty.send('\003')
                        time.sleep(1)
                        _send(tty,"%s" %(e))
                        tty.send("\r")
                        _expect(tty,["cli>"],timeout=3,is_uefi=False)
            continue
        if re > 3:
            g_cli_status = g_cli_status + 1
def sensor_list_th(arg):
    global g_loop_count
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        try:
            re = exec_cmd(xconsole_args({"cmd":"sensor"}), do_quit=False, do_print=False)
            if get_exec_cmd_status(re) == 0:
                sensor_log = "%s/sensor.log" %(get_log_dir())
                sensor_log_cycle = "%s/sensor-%s-%s.log" %(get_log_dir(),args.test_case,g_loop_count)
                wrlog(get_exec_cmd_log(re),sensor_log_cycle)
                wrlog(get_exec_cmd_log(re),sensor_log)
            time.sleep(args.sensor_interval)
        except :
            pass
def ddr_init(tty):
    global g_cli_status
    DDRINIT=["Checkpoint","Platform Mem Tool","DRAM: 0GB","mismatch errors","Synchronous","initialization failure","DDRFAILSAFE","ERROR:","AEROe2>"]
    for _timecount in range(0,args.ddr_init_timeout,60):
        re=_expect(tty,DDRINIT,timeout=60)
        if re == -1:
            continue
        if re == -2:
            return
        if g_cli_status >= args.cli_err_break:
            break
        if re >= 0:
            break
    if re == -2:
        return "INTERRUPT"
    elif re == -1:
        return "TIMEOUT DDRINIT"
    elif re == 0:
        return "PASS"
    return DDRINIT[re]
def linux_send_cmd(tty,cmd,timeout=3*60):
    _send(tty,"%s;rc" %(cmd))
    re = _expect(tty,["_exit_"],timeout)
    if re == -2:
        return "KEYBOARDINTERRUPT %s" %(cmd)
    elif re == -1:
        return "TIMEOUT ERROR %s" %(cmd)
    else:
        if tty.before.find("_rc_0") != -1:
            return "PASS"
        else:
            print tty.before
            return "FAIL %s" %(cmd)

def linux_wget_file(tty,sendfile):
    sendfile_basename = os.path.basename(sendfile)
    if args.wget_href != "":
        return linux_send_cmd(tty,"wget %s/%s -O %s && chmod 777 %s" %(args.wget_href,sendfile,sendfile_basename,sendfile_basename)) 
    else:
        return "--wget_href is not set"
def send_file_b64(tty,sendfile):
    global s0_cli,s1_cli,atf,uefi,bmc
    sendfile_basename = os.path.basename(sendfile)
    re = exec_cmd("cd %s && tar cvfj - '%s'  | base64" %(os.path.dirname(sendfile),sendfile_basename), do_quit=False, do_print=False)
    if re[0] == 0:
        i = 0
        texts = re[1].split("\n")
        print "send_file_b64 %s ... %s(%s)" %(sendfile_basename,now(),(len(texts)*5/60))
        if args.tty_bmc == "ssh":
            _send(bmc,"alias rc='echo -n _rc_$?_ex;echo -n it_'")
            _send(bmc,"cd %s" %(args.linux_pwd))
        for text in texts:
            if i == 0:
                linux_send_cmd(tty,"rm -rf f64")
            else:
                #_send(tty,"echo '%s'>>f64" %(text))
                #re = _expect(tty,["\n"],1*60)
                if 1==1:#len(args.tty_uefi) > 1:
                    print "send_file_b64 %s %s %s %s" %(text,i,len(texts),now())
                    args.tty_send_interval = 50
                    if linux_send_cmd(tty,"echo '%s'>>f64" %(text)) != "PASS":
                        return "SENDFILE %s %s" %(sendfile,text)
                if 1 == 0:
                    print "send_file_b64 %s %s %s %s" %(text,i,len(texts),now())
                    #args.tty_send_interval = 10
                    _send(bmc,"echo 'echo %s>>f64;rc' > /dev/ttyS0;rc" %(text))
                    re = _expect(tty,["_rc_0_exit_"],timeout=10)
                    time.sleep(0.5)
                    print "%s %s" %(tty.before,re)
                    if re != 0:
                        print "_ERROR_"
                        return "SENDFILE %s %s" %(sendfile,text)
            i = i + 1
        re = linux_send_cmd(tty,"cat f64 | base64 -di | tar xvfj -") 
        print "send_file_b64 %s ... %s" %(sendfile_basename,now())
        return re
    else:
        return "SENDFILE %s TAR ERROR" %(sendfile) 
def send_file(tty):    
    for sendfile in args.sendfile.split(","):
        if sendfile == "":
            continue
        re = exec_cmd("cksum %s" %(sendfile)) 
        cksum = re[1].split(" ")[0]
        re = linux_send_cmd(tty,"cksum %s" %(os.path.basename(sendfile)))
        cksum_remote = tty.before
        if cksum_remote.find(cksum) != -1:
            print "skip sendfile %s same cksum %s"  %(sendfile,cksum)
            continue
        else:
            print "start sendfile %s"  %(sendfile)
            if linux_wget_file(tty,sendfile) != "PASS":
                if send_file_b64(tty,sendfile) != "PASS":
                    return "sendfile %s error"  %(sendfile)
    return ""
  
def linux_boot(tty):
    global g_configure
    LINUXBOOT_EXPECT=["login:","Shell>","Synchronous Exception","crashdump kernel","Kernel panic","DRAM FW version","System reboot"]
    try:
        re=_expect(tty,LINUXBOOT_EXPECT,timeout=args.linux_boot_timeout)
        if re ==-1:
            return "LOGIN"
        elif re ==-2:
            return "INTERRUPT"
        elif LINUXBOOT_EXPECT[re] == "DRAM FW version":
            return "AUTO REBOOT"
        elif re > 0:
            return LINUXBOOT_EXPECT[re]
        time.sleep(3)
        _send(tty,"root")
        if _expect(tty,["Password:"]) < 0:
            return "LOGIN PASSWORD"
        _send(tty,"root")
        if _expect(tty,["#","~"]) < 0:
            return "LOGIN ROOT"
        _send(tty,"alias rc='echo -n _rc_$?_ex;echo -n it_'")
        if _expect(tty,["#","~"]) < 0:
            return "Map alias _rc__exit_"
        re = linux_send_cmd(tty,"cd %s" %(args.linux_pwd)) 
        if re != "PASS":
            return re
        for startup_cmd in args.startup_cmd.split(","):
            if startup_cmd == "":
                continue
            re = linux_send_cmd(tty,startup_cmd) 
            if re != "PASS":
                return re
        if args.sendfile != "":
            re = send_file(tty)
            #if re != "":
            #    return re 
        return ""
    except Exception:
        return "EXCEPTION LINUX BOOT %s" %(str(traceback.print_exc()))

def exec_linux_test(tty):
    LINUX_EXPECT = ["_exit_","crashdump kernel","Kernel panic","No such file or directory","DRAM FW version","System reboot"]
    global g_configure,g_cli_status
    if g_cli_status < args.cli_err_break:
        for script in args.linux_script.split(","):
            print "[%s]Start %s" %(now(),script)
            time_start=time.time()
            if script.find("./") != -1:
                _chmod = "chmod 777 %s;" %(script)
                _time = "%s" %(args.time)
            else:
                _chmod = ""
                _time = ""
            _send(tty,"echo -n _start;echo -n _test_;%s%s %s ;rc" %(_chmod,script,_time))
            if _expect(tty,["_start_test_"],timeout=30) <=-1:
                return  "_START_TEST_ %s" %(script)
            timeout = args.time + 10*60
            for _timecount in range(0,timeout,args.t_expect):
                re = _expect(tty,LINUX_EXPECT,timeout=args.t_expect)
                if re == -2:
                    print "KeyboardInterrupt"
                    break
                if re >= 0:
                    print "%s break re=[%s]" %(script,LINUX_EXPECT[re])
                    break
                if g_cli_status >= args.cli_err_break:
                    print "g_cli_status %s" %(g_cli_status)
                    break
                #if len(tty.before) == 0:
                #    re = -3
                #    break
                if re == -1:
                    print "wait[%s]" %(timeout - _timecount)
                    continue
                    #_send(tty, "")
                print ""    
            tdelay=int(time.time() - time_start)
            print "[%s]End %s in %d sec" %(now(),script,tdelay)
            if re == -3:
                return "TESTHANG ERROR"
            elif re == -2:
                return "KEYBOARDINTERRUPT ERROR"
            elif re == -1:
                return "TIMEOUT ERROR"
            elif LINUX_EXPECT[re] == "DRAM FW version":
                time.sleep(3*60) #Monitor sensor list
                return "AUTO REBOOT"
            elif LINUX_EXPECT[re] == "_exit_": 
                if tty.before.find("_rc_0") != -1:
                    return "PASS"
                else:
                    return "FAIL"
            else :
                return LINUX_EXPECT[re]
    else:
        return "CLI[%d]" %(g_cli_status)
def add(a,b):
    return [[a[i][j] + b[i][j] for j in range(0,len(a[i]))] for i in range(0,len(a))]
def eye2d(re):
    re = find_in(re,"\n","")
    re = find_in(re,"\n","")
    re = re[:len(re)-1]
    re = _replace(re,{"+":"0","*":"0",".":"1","%":"1","\r":""})
    eye=[]
    for e in re.split("\n"):
        if e.find("0x") == -1:
            continue
        eye.append([int(i,0) for i in e[6:]])
    return eye
def raw_eye_to_html(name,eye,eye_x,eye_y,eye_x_mask,eye_y_mask):
    h="<table class='eye_table'>"
    h=h+"<tr>"
    h=h+"<th class='eye_title eye_point' > %s </th>" %(name)
    for x in eye_x:
        if x >= 0:
            h=h+ "<th class='eye_title eye_point' >+%02d</th>" %(x)
        else:
            h=h+ "<th class='eye_title eye_point' >-%02d</th>" %(-x)
    h=h+"</tr>"
    for y in range(len(eye_y)):
        h=h+"<tr>"
        for x in range(len(eye_x)):
            if x == 0:
                table_class ="eye_title"
                table_value = eye_y[y]
                flag = ""
                if table_value > 0:
                    flag="+"
                h=h+ "<th class='%s eye_point' >%s%02d</th>" %(table_class,flag,table_value)
            table_value = eye[y][x]
            if eye_x[x] == 0 and eye_y[y] == 0:
                table_class ="eye_hw"
            elif (x-len(eye_x)/2 >= -eye_x_mask) and (x-len(eye_x)/2 <= eye_x_mask) \
             and (y-len(eye_y)/2 >= -eye_y_mask) and (y-len(eye_y)/2 <= eye_y_mask) \
             and eye[y][x] != 0:
                table_class ="eye_fail_mask"
            elif (x-len(eye_x)/2 >= -eye_x_mask) and (x-len(eye_x)/2 <= eye_x_mask) \
             and (y-len(eye_y)/2 >= -eye_y_mask) and (y-len(eye_y)/2 <= eye_y_mask) \
             and eye[y][x] == 0:
                table_class ="eye_pass_mask"
            elif eye[y][x] != 0:
                table_class ="eye_fail"
            else :
                table_class ="eye_pass"
            h=h+ "<th class='%s eye_point' >%d</th>" %(table_class,table_value)
        h=h+"</tr>"
    h=h+"</table>"
    return h
def cfg2id(cfg,split="loop"):
    cfg = _replace(cfg,{"SI_S1_PCP_ACTIVECPM_32_63 [0xFFFFFFFF]":""})
    cfg = _replace(cfg,{"SI_S1_PCP_ACTIVECPM_0_31 [0xFFFFFFFF]":""})
    cfg = _replace(cfg,{"SI_S0_PCP_ACTIVECPM_32_63 [0xFFFFFFFF]":""})
    cfg = _replace(cfg,{"SI_S0_PCP_ACTIVECPM_0_31 [0xFFFFFFFF]":""})
    cfg = _replace(cfg,{"SI_RO_BOARD_S1_DIMM_AVAIL [0xFFFF]":""})
    cfg = _replace(cfg,{"SI_RO_BOARD_S0_DIMM_AVAIL [0xFFFF]":""})
    cfg = _replace(cfg,{"SI_":""})
    cfg = _replace(cfg,{"RO_":""})
    cfg = _replace(cfg,{"BOARD_":""})
    cfg = _replace(cfg,{" ":"_"})
    cfg = _replace(cfg,{"[":""})
    cfg = _replace(cfg,{"]":""})
    while True:
        if cfg.find("__") != -1:
            cfg = _replace(cfg,{"__":"_"})
        else:
            break
    if split !="":
        cfg = cfg.split(split)[0]
    return cfg
def set_configure(name,value,is_hex=True):
    print "set_configure %s %s" %(name,value)
    global g_configure
    if name != "":
        if is_hex:
            try:
                g_configure = "%s %s[%s]" %(g_configure,name,tohex32(int(value,0)))
            except:
                g_configure = "%s %s[%s]" %(g_configure,name,tohex32(int(value)))
        else:
            g_configure = "%s %s[%s]" %(g_configure,name,value)
def set_str(s,ss,e=""):
    if s =="":
        return "%s%s" %(e,ss)
    if ss != "":
        return "%s_%s%s" %(s,e,ss)
    return s
def set_fan(speed):
    print "set_fan %s %s" %(args.bmcip,speed)
    exec_cmd(xconsole_args({"fan":speed}))
def dict_to_str(d):
    re = ""
    for e in d:
        if re == "":
            re="%s" %(d[e])
        elif d[e] != "":
            re="%s_%s" %(re,d[e])
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
def get_cpu_serial_number(log):
    re = ""
    for e in log.split("\n"):
        v = find_in(e,"0000000000000000","")
        if v != "" and e.find("Serial Number") != -1:
            re = "%s%s<br>" %(re,v)
    return re
def get_soc_info(log):
    re = OrderedDict()
    re['soc'] = find_in(log,"Soc voltage : ","\n")
    re['core'] = find_in(log,"Core voltage : ","\n")
    re['DIMM'] = find_in(log,"DIMM1 voltage :","\n")
    re['node'] = find_in(log,"Brought up "," node")
    re['CPUs'] = find_in(log,"node, "," CPUs")
    return re
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

    if dimm_list.find(" S1: ")!= -1:
        re['DPC']  = "2DPC"
    elif dimm_list.find(" S0: ")!= -1:
        re['DPC']  = "1DPC"

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
    if len(dimm_type) > 50:
        re['dimm_type'] = "%s..." %(dimm_type[0:50])
    else:
        re['dimm_type'] = dimm_type
    return re
def is_number(s):
    try:
        int(s,0)
        return True
    except:
        return False
def print_dly(name,_min,_max,step):
    print "%s[0x%03x-0x%03x]\t" %(name,_min,_max),
    for i in range(0,_min,step):
        print ".",
    for i in range(_min,_max,step):
        print "*",
    print ""
def dump_dly_param():
    global g_dly_param
    for e in g_dly_param:
        if max(g_dly_param[e]) < 0x3f:
            step = 1
        elif max(g_dly_param[e]) < 0x100:
            step = 2
        else:
            step = 8
        print_dly(e,min(g_dly_param[e]),max(g_dly_param[e]),step)
def get_dly_param():
    global g_dly_param,g_uefi_log
    dly_type = mcu_id = rank_id = slice_id = bit_id = ""
    for e in g_uefi_log.split("\n"):
        dly_type_mcu_str =  find_in(e, "MCU"," saved leveling")
        if dly_type_mcu_str == "":
            dly_type_mcu_str =  find_in(e, "MCU"," saved Vref")
        rank_id_str = find_in(e, "Target Rank",":")
        slice_id_str = find_in(e,"Slice",":")
        bit_id_str = find_in(e,"Bit"," Bit")
        if bit_id_str == "":
            bit_id_str = find_in(e,"Nibble"," Nibble")
        if dly_type_mcu_str != "" and dly_type_mcu_str.count(" ") == 1:
            v_0 = dly_type_mcu_str.split(" ")[0]
            v_1 = dly_type_mcu_str.split(" ")[1]
            if is_number(v_0) and v_1 !="" :
                mcu_id = v_0
                dly_type = v_1
        if rank_id_str != "" and mcu_id !="":
            if is_number(rank_id_str):
                rank_id = rank_id_str
        if slice_id_str !="" and rank_id !="":
            if is_number(slice_id_str):
                slice_id = slice_id_str
        if bit_id_str !="":
            e = _replace(e)
            if e.find("Bit") != -1:
                k = "Bit"
            elif e.find("Nibble") != -1:
                k = "Nibble"
            else:
                continue
            for bit_str in e.split(k):
                if  bit_str.count(": ") == 1:
                    bit_str_0 = bit_str.split(": ")[0]
                    bit_str_1 = bit_str.split(": ")[1]
                    if is_number(bit_str_0) and is_number(bit_str_1):
                        bit_id = bit_str_0
                        dly_value = int(bit_str_1,0)
                        key = "%s_M_%s_R_%s_S_%s_B_%s" %(dly_type,mcu_id,rank_id,slice_id,bit_id)
                        if key in g_dly_param:
                            g_dly_param[key] = g_dly_param[key] + [dly_value]
                        else:
                            g_dly_param[key] = [dly_value]      
    return g_dly_param
def grep(_str,pwd,options="-h"):
    c = "grep %s '%s' -R '%s' -a" %(options,_str,pwd)
    return commands.getstatusoutput(c)

def log_count(log):
    msg = ""
    re = OrderedDict()
    for e in log.split("\n"):
        kmesg = find_in(e,"] ","")
        if kmesg != "":
            e = kmesg
        if e in re:
            re[e] = re[e] + 1
        else:
            re[e] = 1
    for e in re:
        msg = "%s[x%s]%s" %(msg,re[e],e)
    return msg

def load_known_issues():
    if os.path.exists(args.known_issues):
        args.known_issues = open_file(args.known_issues).replace("\r", "").split("\n")
    else:
        args.known_issues = args.known_issues.split(",")
    print "args.known_issues %s" %(args.known_issues)
def is_known_issues(grep_log):
    for log in grep_log.split("\n"):
        is_found = False
        for e in args.known_issues:
            if e == "":
                continue
            if log.find(e) != -1:
                is_found = True
        if is_found == False:
            return False
    return True
def check_expect_signal():
    global g_uefi_log,g_cli_log
    status = OrderedDict()
    for e in args.expect_signal:
        if g_uefi_log.find(e) == -1 and g_cli_log.find(e) == -1:
            status[e] = "NOT FOUND"
    return status
def load_expect_signal():
    if args.expect_signal == "":
        return
    if os.path.exists(args.expect_signal):
        args.expect_signal = open_file(args.expect_signal).replace("\r", "").split("\n")
    else:
        args.expect_signal = args.expect_signal.replace("\r", "").split(",")
    print "args.expect_signal %s" %(args.expect_signal)      
def load_failure_signature():
    if os.path.exists(args.fail_signal):
        args.fail_signal = open_file(args.fail_signal).replace("\r", "").split("\n")
    else:
        args.fail_signal = args.fail_signal.replace("\r", "").split(",")
    print "args.fail_signal %s" %(args.fail_signal)  
def check_failure_signature():
    status = OrderedDict()
    for tty_name in ["uefi","atf","s0cli","s1cli","bmc"]:
        log = "%s/%s" %(get_log_dir(),get_log_name(tty_name + ".log"))
        if os.path.exists(log) == False:
            continue
        for e in args.fail_signal:
            if e == "":
                continue
            re = grep(e,log)
            if get_exec_cmd_status(re) == 0:
                grep_log = get_exec_cmd_log(re)
                if is_known_issues(grep_log) == False:
                    status["%s %s" %(tty_name,e)] = log_count(grep_log)
    return status
def wr_report(html):
    wrlog(html,"%s/Report.html" %(get_log_dir()),args.html_print)
def linux_test():
    global g_test_param,g_uefi_log,g_cli_log
    global g_configure,g_loop_count,g_cli_status
    global s0_cli,s1_cli,atf,uefi,bmc
    global g_eye2d
    s0_cli = s1_cli = atf = uefi = bmc = None
    s0cli_bg = s1cli_bg = bmc_bg = atf_bg = sensor_bg = None
    total = 1
    total_pass = 0
    total_fail = 0
    status = OrderedDict()
    for e in g_test_param:
        total = total * len(g_test_param[e])
    for loop_at in range(0,total):
        g_loop_count = g_loop_count + 1
        g_uefi_log=g_cli_log=g_configure=re=""
        #for ip in [args.hostip,args.bmcip]:
        #    if check_ip_alive(args.hostip) == False :
        #        do_exit("Error : check_ip_alive %s" %(ip),1)
        if args.start_test != 0:                       
            BMCoff()
            bmc_off_start = time.time()
        if "bios_fw" in g_test_param:
            bios_fw = get_loop_element(g_test_param,"bios_fw",loop_at)[0]
            re = exec_cmd(xconsole_args({"atfbios_fw":args.bios_fw}))
            if get_exec_cmd_status(re) != 0:
                do_exit("Firmware upgrade %s" %(bios_fw),1)
            set_configure("bios_fw",bios_fw)
        if "sk" in g_test_param:
            args.sk = get_loop_element(g_test_param,"sk",loop_at)[0]
            set_configure("sk",args.sk)
        if "mcu_mask" in g_test_param:
            args.mcu_mask = get_loop_element(g_test_param,"mcu_mask",loop_at)[0]
            set_configure("mcu_mask",args.mcu_mask)
        if "rank_mask" in g_test_param:
            args.rank_mask = get_loop_element(g_test_param,"rank_mask",loop_at)[0]
            set_configure("rank_mask",args.rank_mask)
        if "slice_mask" in g_test_param:
            args.slice_mask = get_loop_element(g_test_param,"slice_mask",loop_at)[0]
            set_configure("slice_mask",args.slice_mask)
        if "eye_type" in g_test_param:
            eye_type = get_loop_element(g_test_param,"eye_type",loop_at)[0]
            dmt_2deye_nv_cfg(eye_type)
            set_configure("eye_type",eye_type,is_hex=False)
        nv_value_ = None
        nv_cmd = ""
        for nv in g_test_param:
            if nv.find("SI") != -1:
                nv_value = get_loop_element(g_test_param,nv,loop_at)[0]
                if nv_value == "-":
                    nv_value = nv_value_
                else:
                    nv_value_ = nv_value
                set_configure(nv,nv_value)
                nv_cmd = nv_cmd + set_nvparam_cmd(nv,nv_value)
        if nv_cmd != "":
            re = set_nvparm(nv_cmd)
            if get_exec_cmd_status(re) != 0:
                do_exit("set_nvparm %s" %(nv_cmd),1)
        if "loop" in g_test_param:
            loop = get_loop_element(g_test_param,"loop",loop_at)[0]
            set_configure("loop",loop,is_hex=False)
        if "sub_loop" in g_test_param and len(g_test_param['sub_loop']) > 1:
            sub_loop = get_loop_element(g_test_param,"sub_loop",loop_at)[0]
            set_configure("sub_loop",sub_loop,is_hex=False)
        if args.start_test == 0:
            continue
        if args.tty_s0cli  != "":
            s0cli = xconsole(args.tty_s0cli,"s0cli")
            if s0cli == None:
                do_exit("Can't open tty_s0cli console",1)
        else:
            print "Test without tty_s0cli"
        if args.tty_s1cli  != "":
            s1cli = xconsole(args.tty_s1cli,"s1cli")
            if s1cli == None:
                do_exit("Can't open tty_s1cli console",1)
        else:
            print "Test without tty_s1cli"
        if args.tty_atf != "":
            atf = xconsole(args.tty_atf,"atf")
            if atf == None:
                do_exit("Can't open tty_atf console",1)
        else:
            print "Test without tty_atf"
        if args.tty_uefi != "":
            uefi = xconsole(args.tty_uefi,"uefi")
            if uefi == None:
                do_exit("Can't open tty_uefi console",1)
            if len(args.tty_uefi) > 1:
                if _expect(uefi,["--------------------------------------------"],timeout=5*60) == -1:
                    re="Open xconsole %s Fail" %(args.tty_uefi)
        if args.tty_bmc != "":
            bmc = xconsole(args.tty_bmc,"bmc")
            if bmc == None:
                do_exit("Can't open tty_bmc console",1) 
        tdelay=int(time.time() - bmc_off_start)
        if tdelay >= args.powertime:
            tdelay = 0
        else:
            tdelay = args.powertime - tdelay
        time.sleep(tdelay)
        BMCon()
        if args.tty_s0cli  != "":
            if _expect(s0cli,["SMpro","Firmware"],timeout=1*60) == -1:
                re="SMPRO ROM ERROR"
            s0cli_bg=__bg_start(cli_th,s0cli)
        if args.tty_s1cli  != "":
            s1cli_bg=__bg_start(cli_th,s1cli)
        #bmc_bg = __bg_start(bmc_th)
        #atf_bg = __bg_start(atf_th)
        if args.sensor_bg !=0:
            sensor_bg = __bg_start(sensor_list_th)
        if re =="":
            re = _expect(uefi,["DRAM FW version","Welcome to AEROe","DRAM Initialization"],timeout=2*60)
        if re < 0 :
            re="UEFI BOOT ERROR %d" %(re)
        else:
            re = ddr_init(uefi)
        ddr_info = dict_to_str(get_ddr_info(g_uefi_log))
        if loop_at == 0:
            wr_report(html_dict({"DDR_INFO":ddr_info},w3_border_en=True))
        cpu_info = get_cpu_info(g_cli_log)
        if cpu_info != "" and loop_at == 0:
            wr_report(html_dict({"CPU_TYPE":cpu_info},w3_border_en=True))
        ln_log_ddr_info(get_log_dir(),ddr_info)
        if re == "PASS" and args.linux_script != "":
            re = linux_boot(uefi)
            if loop_at == 0:
                soc_info = dict_to_str(get_soc_info(g_uefi_log))
                wr_report(html_dict({"SOC_INFO":soc_info},w3_border_en=True))
                cpu_serial_number = get_cpu_serial_number(g_uefi_log)
                if cpu_serial_number != "":
                    wr_report(html_dict({"CPU_INFO":cpu_serial_number},w3_border_en=True))
                lspci_info = get_lspci_info(g_uefi_log)
                if lspci_info != "":
                    wr_report(html_dict({"PCI_INFO":lspci_info},w3_border_en=True))
            if re =="":
                re = exec_linux_test(uefi)
        elif re == "AEROe2>":
            re,eye_2d_raw = aeroe2_dmt()
        elif re == "Platform Mem Tool":
            re,eye_2d_raw = platform_mem_tool()
        try:
            if re == -1:
                re = "Timeout"
            if re == -2:
                re = "Keyboard Interrupt"
            BMC_sel_list(1)
            pass_count = "pass_count %s" %(cfg2id(g_configure,"loop"))
            fail_count = "fail_count %s" %(cfg2id(g_configure,"loop"))
            fail_info = "fail_info %s" %(cfg2id(g_configure,"loop"))
            if (pass_count in status) == False:
                status[pass_count] = 0
            if (fail_count in status) == False:
                status[fail_count] = 0
            if (fail_info in status ) ==False:
                status[fail_info] = ""
            check_fail_status = check_failure_signature()
            _check_expect_signal = check_expect_signal()
            if len(_check_expect_signal) > 0 :
                wr_report(html_dict(_check_expect_signal,w3_border_en=True))
                status[fail_count] = status[fail_count] + 1
                test_status = "FAIL_EXPECT_SIGNAL"
                total_fail = total_fail + 1
                status[fail_info] = "%s %s" %(status[fail_info],test_status)
                if args.break_on_fail != 0:
                    break
            elif len(check_fail_status) > 0:
                wr_report(html_dict(check_fail_status,w3_border_en=True))
                status[fail_count] = status[fail_count] + 1
                test_status = "TEST_FAIL_SIGNAL"
                total_fail = total_fail + 1
                status[fail_info] = "%s %s" %(status[fail_info],test_status)
                if args.break_on_fail != 0:
                    break
            elif re[0:4] =="PASS":
                status[pass_count] = status[pass_count] + 1
                total_pass = total_pass + 1
                test_status = "TEST_PASS"
            else:
                status[fail_count] = status[fail_count] + 1
                test_status = "TEST_FAIL"
                total_fail = total_fail + 1
                status[fail_info] = "%s %s" %(status[fail_info],re)
                if args.break_on_fail != 0:
                    break
            test_summary ="[at %s/%s P/F [%s/%s]" %(g_loop_count,total,total_pass,total_fail)
            wr_report(html_dict({g_configure:"%s [%s] [%s]" %(test_status,re,test_summary)},w3_border_en=True))
            if args.sensor_bg !=0:
                sensor_log = "%s/sensor-%s-%s.log" %(get_log_dir(),args.test_case,g_loop_count)
                re = exec_cmd("./ipmitool_sensor_chartjs.py --log %s --sensor_interval %s" %(sensor_log,args.sensor_interval))
        except:
            print traceback.print_exc()
        try:
            __bg_stop(s0cli_bg)
            __bg_stop(s1cli_bg)
            __bg_stop(bmc_bg)
            __bg_stop(atf_bg)
            __bg_stop(sensor_bg)
        except:
            print traceback.print_exc()

    wr_report(html_dict({"STATUS SUMMARY": "FAIL" if total_fail > 0 else "PASS"}))
    wr_report(html_dict(status,w3_border_en=True))
    
    if args.sensor_bg !=0:
        sensor_log = "%s/sensor.log" %(get_log_dir())
        re = exec_cmd("./ipmitool_sensor_chartjs.py --log %s --sensor_interval %s" %(sensor_log,args.sensor_interval))
        re = exec_cmd("./ipmitool_sensor_chartjs.py --log %s --D 1 --sensor_interval %s" %(sensor_log,args.sensor_interval))
        print re[1]
        wr_report(re[1])    
    return total_fail
    #dump_dly_param()
#def main
g_uefi_log=g_cli_log=g_configure=""       
g_loop_count = 0
sys_argv=' '.join([str(e) for e in sys.argv])
sys_argv = nv_args(sys_argv)
sys_argv = nv_args(sys_argv,"--file")
sys_argv = nv_args(sys_argv,"--nv ")
print sys_argv

cfg_file_argv = find_in(sys_argv,"--cfg_file "," ")
cfg_file_list = [item for item in cfg_file_argv.split(',')]
cfg_file      = ""
for e in cfg_file_list:
    cfg_str = _replace(open_file(e),{"\r":" ","\n":" "})
    cfg_file="%s%s " %(cfg_file,cfg_str)
args_cmd = _replace(sys_argv,{"%s "%(sys.argv[0]):"","--cfg_file %s" %(cfg_file_argv):cfg_file})
args_cmd = nv_args(args_cmd)
args_cmd = nv_args(args_cmd,"--nv ")
args_cmd_parser=[]
e = args_cmd.split('"')
for i in range(0,len(e)):    
    if (i%2) == 0:
        for ee in e[i].split(" "):
            if ee != "":args_cmd_parser.append(ee)
    else:args_cmd_parser.append(e[i])
args = parser.parse_args(args_cmd_parser)

wrlog(' '.join(args_cmd_parser), "%s/%s" %(get_log_dir(),"test_args.log"))

args.time_start_test = now()
if args.board_type.lower().find("snow") != -1:
    args.sol_atf = args.sol_s0cli = args.sol_s1cli= "0"
    
if args.tty_atf == "" and args.sol_atf != "0":
    args.tty_atf = args.sol_atf
if args.tty_uefi == "" and args.sol_uefi != "0":
    args.tty_uefi = args.sol_uefi
if args.tty_s0cli == ""  and args.sol_s0cli != "0":
    args.tty_s0cli = args.sol_s0cli
if args.tty_s1cli == ""  and args.sol_s1cli != "0":
    args.tty_s1cli = args.sol_s1cli
if args.tty_bmc == "" and args.bmcip != "0":
    args.tty_bmc = "ssh"
    
cfg_file = find_in(sys_argv,"--cfg_file "," ")
for e in cfg_file.split(","):
    if args.board_cfg == "" and e.find("boards/") != -1:
        args.board_cfg = find_in(e,"boards/","")  
    test_cfg = find_in(e,"cfg/",".cfg")
    if test_cfg.find("/") != -1:
        test_cfg = find_in(test_cfg,"/","")
    if args.test_cfg == "" and test_cfg !="":
        args.test_cfg = "%s%s" %(args.test_cfg,test_cfg)
if args.board_cfg =="" and args.board != "":
    args.board_cfg = args.board
if args.board_cfg =="" and args.bmcip != "":
    args.board_cfg ="BMCIP_%s" %(args.bmcip)
if args.test_cfg =="":
    args.test_cfg = args.linux_script.split(" ")[0]
g_cli_status=0
s0_cli=s1_cli=atf=uefi=bmc=None
g_test_param=OrderedDict()
g_eye2d=OrderedDict()
g_dly_param = OrderedDict()
g_nvparm = get_nvparam_define()
g_args_nv = nv_name(args.nv_scan)
if args.web_link =="":
    args.web_link = "http://" + get_ip()
if args.loop > 0:
    g_test_param['loop']=list(range(1,args.loop+1))
if args.bios_fw !="":
    g_test_param['bios_fw']= [item for item in args.bios_fw.split(',')]
if args.eye_type !="":
    g_test_param['eye_type'] = [i for i in args.eye_type.split(',')]
if args.sk !="":
    g_test_param['sk'] = [i for i in args.sk.split(',')]
if args.mcu_mask !="":
    g_test_param['mcu_mask'] = [i for i in args.mcu_mask.split(',')]
if args.rank_mask !="":
    g_test_param['rank_mask'] = [i for i in args.rank_mask.split(',')]
if args.slice_mask !="":
    g_test_param['slice_mask'] = [i for i in args.slice_mask.split(',')]
for e in g_args_nv:
    g_test_param[e] = g_args_nv[e]
if args.sub_loop > 0:
    g_test_param['sub_loop']=list(range(1,args.sub_loop+1))
if args.sys_log !="":
    sys_log = open("%s" %(args.sys_log),"a+",0)
    sys.stdout = sys_log
wr_report(html_header(args.board))
wr_report(html_dict({"CLI ARGV":sys_argv}))
load_known_issues()
load_failure_signature()
load_expect_signal()
for e in [args.bmcip,args.hostip]:
    if e != "":
        os.system("ssh-keygen -f ~/.ssh/known_hosts -R %s > /dev/null"%(e))
try:
    if args.bmcip == "":
        print "ERROR Request BMCIP"
    if args.wait != 0:
        is_run = False
        ps_run = ""
        while True:
            ps = exec_cmd("ps -ef --sort=start_time",False,False)[1].split('\n')
            for i in range(len(ps)-1,-1,-1):
                pid = "%s" %(get_pid(ps[i]))
                if ps[i].find(args.bmcip + " ") != -1 and ps[i].find(get_log_dir()) == -1 :
                    if ps[i].find("./xconsole.py ") != -1 or ps[i].find("ipmitool ") or ps[i].find("screen ")  or ps[i].find(" bash "):
                        continue
                    if ps_run != pid:
                        print "%s ... is running" %(find_in(ps[i],get_pid(ps[i],6)))
                        print "kill -9 %s to close" %(pid)
                        ps_run = pid
                    is_run = True
                    break
            if is_run == False:
                break
            time.sleep(5) 
    if args.cmd != "":
        re = exec_cmd(xconsole_args({"cmd":args.cmd}))
    if args.cleannv != 0 :
        print  "cleannv ..."
        re = exec_cmd(xconsole_args({"cmd":"cleannv"}))
    if args.bmc_fw !="" and args.flash_fw != 0:
        re = 0,"debug without check exit code"
        print "Program %s ... " %(args.bmc_fw)
        c = xconsole_args({"bmc_fw":args.bmc_fw,"tty_bmc":args.tty_bmc})
        print c
        if True:
            os.system(c)
            re = 0,"debug without check exit code"
        else:
            re = exec_cmd(c)
        wr_report(html_dict({"Firmware upgrade":"%s %s" %(args.bmc_fw,"PASS" if re[0] == 0 else "FAIL")}))
        if re[0] != 0:
            print "Program %s failed" %(args.bmc_fw)
            do_exit(re[1])
        print "Waiting reboot ...in 3*60"
        time.sleep(3*60)
    if args.enable_root != 0:
        re = exec_cmd(xconsole_args({"cmd":"enable_root"}))
    if args.scp_fw !="" and args.flash_fw != 0:
        print "Program %s ... " %(args.scp_fw)
        re = exec_cmd(xconsole_args({"scp_fw":args.scp_fw}))
        wr_report(html_dict({"Firmware upgrade":"%s %s" %(args.scp_fw,"PASS" if re[0] == 0 else "FAIL")}))
        
        if re[0] != 0:
            print "Program %s failed" %(args.scp_fw)
            do_exit(re[1])
    if args.atfbios_fw !="" and args.flash_fw != 0:
        print "Program %s ... " %(args.atfbios_fw)
        re = exec_cmd(xconsole_args({"atfbios_fw":args.atfbios_fw}))
        wr_report(html_dict({"Firmware upgrade":"%s %s" %(args.atfbios_fw,"PASS" if re[0] == 0 else "FAIL")}))
        if re[0] != 0:
            print "Program %s failed" %(args.atfbios_fw)
            do_exit(re[1])
    if args.nvparm_board_setting !="" and args.flash_fw != 0:
        print "Program %s ... " %(args.nvparm_board_setting)
        re = exec_cmd(xconsole_args({"nvparm_board_setting":args.nvparm_board_setting}))
        wr_report(html_dict({"Firmware upgrade":"%s %s" %(args.nvparm_board_setting,"PASS" if re[0] == 0 else "FAIL")}))
        if re[0] != 0:
            print "Program %s failed" %(args.nvparm_board_setting)
            do_exit(re[1])
    if  args.fan != "":
        set_fan(args.fan)
    ln_log_test_cfg(get_log_dir())
    re = linux_test()
    sys.exit(re)
except KeyboardInterrupt:
    print "main KeyboardInterrupt !!!!"