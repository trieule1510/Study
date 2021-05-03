from flask import Flask, request

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
            print (e)
            return print ("I'm a ADMIN")
    return print ("I'm HACKER")
ip= "127.0.0.1"
is_admin(ip)