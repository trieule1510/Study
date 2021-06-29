#

import commands
import os.path

def exec_cmd(e):
    print e
    return commands.getstatusoutput(e)
def find_in( s, first, last="",A=0,B=0):
    try:
        start = s.index( first ) + len( first ) 
        if last == "":
            end = len(s)
        else:
            end = s.index( last, start ) 
        return s[start-A:end + B]
    except ValueError:
        return ""
def fw_link(fw_www,fw_type):
    re = []
    links =  exec_cmd("curl %s | grep %s" %(fw_www,fw_type))[1]
    for e in links.split("\n"):
        link = find_in(e,'href="','">')
        if link != "":
            re.append(link)
    return re
def wget(fw_www,fw_patch,fw_dir):
    exec_cmd('mkdir -p %s' %(fw_dir))
    o = "%s/%s" %(fw_dir,os.path.basename(fw_patch))
    if untar(o)[0] == 0:
        return o
    exec_cmd('wget %s%s -O %s' %(fw_www,fw_patch,o))
    untar(o)
    return o
def untar(fw_patch):
    re = exec_cmd("tar xvfx %s -C %s" %(fw_patch,os.path.dirname(fw_patch)))
    return re
def wget_fw(fw_www,fw_type,cp_dir,fw_dir = "cfg/fw",tar=".tar.xz"):
    links = fw_link(fw_www,fw_type)
    for fw_patch in links:
        o = wget(fw_www="https://den-swweb.amperecomputing.com/",fw_patch=fw_patch,fw_dir=fw_dir)
        os.system("cp -rf %s/*signed*.hpm %s/" %(o.replace(tar, "").replace("_signed", ""),cp_dir))
        os.system("cp -rf %s/*signed*.img %s/" %(o.replace(tar, "").replace("_signed", ""),cp_dir))
        os.system("cp -rf %s/*signed*.slim %s/" %(o.replace(tar, "").replace("_signed", ""),cp_dir))
for atfbios_fw in ["jade_aptiov_atf_signed_","fansipan_aptiov_atf_signed_","snow_aptiov_atf_signed_"]:
    wget_fw("https://den-swweb.amperecomputing.com/altra-fw-builds/",atfbios_fw,"cfg/atfbios_fw")
    wget_fw("https://den-swweb.amperecomputing.com/altra-max-fw-builds/",atfbios_fw,"cfg/atfbios_fw")
wget_fw("https://den-swweb.amperecomputing.com/altra-fw-builds/","altra_scp_signed_","cfg/scp_fw")
wget_fw("https://den-swweb.amperecomputing.com/altra-max-fw-builds/","altra_scp_signed_","cfg/scp_fw")
