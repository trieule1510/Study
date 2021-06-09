#!/usr/bin/python
import os
import argparse
from collections import OrderedDict
import datetime
parser = argparse.ArgumentParser(description='ipmitool sensor list to chart')
#public
parser.add_argument('--log', dest='log',default="sensor.log",help='load sensor list log')
parser.add_argument('--O', dest='O',default="",help='log out')
parser.add_argument('--D', dest='D',default="",help='prints out html')
parser.add_argument('--tag', dest='tag',default="",help='log tag')
parser.add_argument('--filter', dest='filter',default="",help='filter')
parser.add_argument('--sensor_interval', dest='sensor_interval',default=10,type=int,help='sensor_interval')
parser.add_argument('--sensor_na', dest='sensor_na',default="-1",help='cover sensor_na to value')
#Private
parser.add_argument('--sensor_count', dest='sensor_count',default=10,type=int,help='sensor_count')
parser.add_argument('--sensor_split', dest='sensor_split',default="|",help='sensor_split')
parser.add_argument('--datetime', dest='datetime',default="",help='datetime')

args = parser.parse_args()

def id_by_time():
    return str(datetime.datetime.today().strftime('%y%m%d%H%M%S%f'))
def open_file(filename):
    try:
        f = open(filename, "r")
        text=f.read()
        f.close()
        return text;
    except:return ""
def wrlog(msg,file_name=""):
    try:
        f=open(file_name, "a+")
        f.write("%s" %(msg))
        f.close()
    except:
        print "ERR wrlog %s " %(file_name)
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
def sensor_filter(sensor_list,_type,_filter):
    _sensor_list = OrderedDict()
    for e in sensor_list:
        append = False
        for f in _filter.split(","):
            msg = ""
            for m in sensor_list[e][0]:
                msg = msg + m
            if _type in sensor_list[e][0] and msg.find(f) != -1:
                append = True
        if append:
            _sensor_list[e] = sensor_list[e]
    return _sensor_list
def color(i):
    try:
        e = ['AliceBlue','AntiqueWhite','Aqua','Aquamarine','Azure','Beige','Bisque','Black','BlanchedAlmond','Blue','BlueViolet','Brown','BurlyWood','CadetBlue','Chartreuse','Chocolate','Coral','CornflowerBlue','Cornsilk','Crimson','Cyan','DarkBlue','DarkCyan','DarkGoldenRod','DarkGray','DarkGrey','DarkGreen','DarkKhaki','DarkMagenta','DarkOliveGreen','DarkOrange','DarkOrchid','DarkRed','DarkSalmon','DarkSeaGreen','DarkSlateBlue','DarkSlateGray','DarkSlateGrey','DarkTurquoise','DarkViolet','DeepPink','DeepSkyBlue','DimGray','DimGrey','DodgerBlue','FireBrick','FloralWhite','ForestGreen','Fuchsia','Gainsboro','GhostWhite','Gold','GoldenRod','Gray','Grey','Green','GreenYellow','HoneyDew','HotPink','IndianRed','Indigo','Ivory','Khaki','Lavender','LavenderBlush','LawnGreen','LemonChiffon','LightBlue','LightCoral','LightCyan','LightGoldenRodYellow','LightGray','LightGrey','LightGreen','LightPink','LightSalmon','LightSeaGreen','LightSkyBlue','LightSlateGray','LightSlateGrey','LightSteelBlue','LightYellow','Lime','LimeGreen','Linen','Magenta','Maroon','MediumAquaMarine','MediumBlue','MediumOrchid','MediumPurple','MediumSeaGreen','MediumSlateBlue','MediumSpringGreen','MediumTurquoise','MediumVioletRed','MidnightBlue','MintCream','MistyRose','Moccasin','NavajoWhite','Navy','OldLace','Olive','OliveDrab','Orange','OrangeRed','Orchid','PaleGoldenRod','PaleGreen','PaleTurquoise','PaleVioletRed','PapayaWhip','PeachPuff','Peru','Pink','Plum','PowderBlue','Purple','RebeccaPurple','Red','RosyBrown','RoyalBlue','SaddleBrown','Salmon','SandyBrown','SeaGreen','SeaShell','Sienna','Silver','SkyBlue','SlateBlue','SlateGray','SlateGrey','Snow','SpringGreen','SteelBlue','Tan','Teal','Thistle','Tomato','Turquoise','Violet','Wheat','WhiteSmoke','Yellow','YellowGreen']
        return e[i]
    except:
        return 'red'
def get_sensor_list(file_name):
    logs = open_file(file_name)
    sensor_list = OrderedDict()
    sensor_type_list = OrderedDict()
    for e in logs.split("\n"):
        e = _replace(e, {" na ":args.sensor_na})
        ee = e.split(args.sensor_split)
        if len(ee) == args.sensor_count:
            sensor_name = ee[0]
            sensor_type = ee[2]
            if sensor_name in sensor_list:
                sensor_list[sensor_name].append(ee)
            else:
                sensor_list[sensor_name] = [ee]
            if (sensor_type in sensor_type_list) == False:
                sensor_type_list[sensor_type] = True
    return sensor_list,sensor_type_list
def len_max(sensor_list):
    _max = 0
    for e in sensor_list:
        if len(sensor_list[e]) > _max:
            _max = len(sensor_list[e])
    return _max
def to_datasets(sensor_list,sensor_type_list):
    pass
def html_header():
    h = ""
    h = h + "<!DOCTYPE html><html lang='en'><head><title>SENSOR CHART</title><link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'><script src='https://cdn.jsdelivr.net/npm/chart.js@2.8.0'></script></head>"
    h = h + "<body><h1 align='center'><img src='data:image/png;base64,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' scale='0'></h1>"
    h = h + "<p align='center'><font size='7' color='blue'><span>SENSOR CHART</span></font></p>"
    return h
def html_end():
    return "</body></html>"
def to_js_id(e):
    e = "%s_%s" %(e , args.datetime)
    return _replace(e, {" ":"_","\r":"","\n":""})
def html_chartjs(name,labels,datasets):
    h = "<p align='center'><font size='7' color='blue'><span>%s</span></font></p><div style='width:90%s;height:50%s'><canvas id='{{%s}}'></canvas></div>" %(name,'%','%',to_js_id(name))
    h = h + "<script>"
    h = h + "var %s_ctx = document.getElementById('{{%s}}').getContext('2d');" %(to_js_id(name),to_js_id(name))
    h = h + "var myChart = new Chart(%s_ctx, {" %(to_js_id(name))
    h = h + "    type: 'line',"
    h = h + "    data: {labels: %s,datasets: [%s]},options: {}});" %(labels,datasets)
    h = h + "</script>"
    return h
def chart_min_max(data):
    _min = 0x7ffffff
    _max = 0
    for e in data:
        if e == args.sensor_na:
            continue
        try:
            v = float(e)
        except:
            v = int(e,0)
        if v == -1:
            continue
        if v < _min:
            _min = v
        if v > _max:
            _max = v
    if _min == 0x7ffffff:
        _min = 0
    return _min,_max
args.datetime = id_by_time()
sensor_list,sensor_type_list = get_sensor_list(args.log)
if args.D != "":
    html = "<script src='https://cdn.jsdelivr.net/npm/chart.js@2.8.0'></script>"
else:
    html = html_header()
    
for e in sensor_type_list:
    _sensor_list = sensor_filter(sensor_list,e,args.filter)
    if  len(_sensor_list) == 0:
        continue
    labels = str(['%s' %(i*args.sensor_interval) for i in range(0,len_max(_sensor_list))])
    datasets=""
    i = 0 
    for ee in _sensor_list:
        i = i + 1
        data = [v[1] for v in _sensor_list[ee]]
        _min,_max = chart_min_max(data)
        ee = "%s [%s:%s]" %(ee.replace(" ", ""),_min,_max)
        datasets="%s{label: '%s',data: %s,backgroundColor:'%s',borderColor:'%s',fill: false}," %(datasets,ee,str(data),color(i*2),color(i*2))
    html = html + html_chartjs(e,labels,datasets)
html = html + html_end()

if args.D != "":
    print html
else:
    if args.O !="":
        log = args.O
    else:
        log = '%s%s.html' %(args.log,args.tag)
    os.system("rm -rf %s" %(log))
    print "Output file %s" %(log)
    wrlog(html, log)