#!/usr/local/bin/python3
import asyncio
import json
import logging
import websockets
import datetime
import time
import threading
import subprocess
from threading import Thread
import os
import argparse
import string

logging.basicConfig()

parser = argparse.ArgumentParser(description='ddr utils web!')

parser.add_argument('--port', dest='port',default=2120,type=int,help='www port')

args = parser.parse_args()

USERS = set()

def ddr_utils_py():
    return "./linux_test.py " 
def exec_cmd(e):
    re = subprocess.getstatusoutput(e)
    return re
def find_in( s, first, last ,A=0,B=0):
    try:
        start = s.index( first ) + len( first ) 
        if last == "":
            end = len(s)
        else:
            end = s.index( last, start ) 
        return s[start-A:end+B]
    except ValueError:return ""
def shell_pid(flag=""):
    if flag == "":
        #flag = ddr_utils_py()
        flag = " --sys_log "
    re=[]
    ps = exec_cmd("ps -ef --sort=start_time")[1].split('\n')
    for i in range(len(ps)-1,-1,-1):
        if ps[i].find(flag) != -1 and ps[i].find("test_cfg.py") == -1:
            re.append(ps[i])
    return re 
def get_pid_ps(ps):
    cmd_list = ps.split(' ')
    for j in range(1, len(cmd_list)):
        if cmd_list[j] != "":
            return cmd_list[j]
    return ""
def get_board_ps(ps):
    board = find_in(ps, "--cfg_file boards/", ",")
    if board == "":
        board = find_in(ps, "--board_cfg ", " ")
    if board == "":
        board = find_in(ps, "--bmcip ", " ")
    if board =="":
        board = find_in(ps, "--cfg_file boards/", " ")
    if board =="":
        board = find_in(ps, "--cfg_file boards/","")
    return board
def get_log_ps(ps):
    log = find_in(ps, "--sys_log ", " ")
    if log =="":
        log = find_in(ps, "--sys_log ", "")
    return log
def get_cmd_ps(ps):
    py_script = ""
    for e in ps.split(" "):
        if e.find(".py") != -1:
            py_script = e
    return find_in(ps,py_script, "", A=len(py_script))
def ascii(text):
    try:
        return ''.join([x for x in text if x in string.printable])
    except:
        return ""
def json_data_format(data):
    data = data.replace("\r","")
    data = data.replace("{","")
    data = data.replace("}","")
    data = data.replace(":","")
    data = data.replace("\\","")
    data = data.replace("\"","")
    data = data.replace("\t","")
    data = data.replace("\"","")
    
    str = ""
    for e in data.split("\n"):
        str = str + e 
        if len(e)> 1 and e[len(e)-1] != ">":
            str = str + "</br>"
    return ascii(str)
    
def file_date(f):
    try:
    	if f == "NA":
    		return "0"
    	return os.stat(f)[8]
    except:
        return "0"
async def register(websocket):
    USERS.add(websocket)
    
async def unregister(websocket):
    USERS.remove(websocket)

def board_json_format(board_name,pid,log,cmd,data):
    class_name = board_name.replace(" ","").replace(".","_")
    j = '"%s":{"name":"%s","pid":"%s","log":"%s","cmd":"%s","data":"%s"}' \
        %(class_name,board_name,pid,log,cmd,data)
    return j
def get_ps_json_data(filter=""):
	shell_ps = shell_pid()
	j = '{'
	for ps in shell_ps:
	    board = get_board_ps(ps)
	    pid = get_pid_ps(ps)
	    log = get_log_ps(ps)
	    cmd = json_data_format(get_cmd_ps(ps))
	    if filter != "" and log.find(filter) == -1:
	    	continue
	    if os.path.exists(log) == False:
	    	continue
	    try:
	    	data = json_data_format(exec_cmd("tail -n 25 " + log)[1])
	    except:
	    	data = json_data_format("Can't read log %s" %(log))
	    j = j + board_json_format(board,pid,log,cmd,data) + ","
	if len(j) > 1:
		j = j[0:len(j)-1]
	j = "%s}" %(j)
	print (j)
	return j

async def ws_send(websocket, path):
    await register(websocket)
    try:
        FILES_0 = []
        FILES_1 = ["NA"]
        moddate_0 = []
        await websocket.send(get_ps_json_data())
        await asyncio.sleep(1)
        while True:           
            await websocket.send(get_ps_json_data())
            await asyncio.sleep(1)
            continue
            moddate_1 = [file_date(e) for e in FILES_1] 
            if moddate_1 != moddate_0 or FILES_0 !=FILES_1:
                print (moddate_0)
                print (moddate_1)
                moddate_0 = moddate_1
                FILES_0 = FILES_1
                await websocket.send(get_ps_json_data())
                await asyncio.sleep(1)
            else:
                shell_ps = shell_pid()
                FILES_1 = [get_log_ps(ps) for ps in shell_ps]
                BOARD_PS = [get_board_ps(ps) for ps in shell_ps]
                print (BOARD_PS)
                #moddate_0 = [file_date(e) for e in FILES_1]
                await asyncio.sleep(1)
    finally:
        await unregister(websocket)

start_server = websockets.serve(ws_send, "0.0.0.0", args.port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
