from waitress import serve
import  www
import argparse

parser = argparse.ArgumentParser(description='ddr utils web!')
parser.add_argument('--port', dest='port',default=2021,type=int,help='www port')
args = parser.parse_args()
serve(www.app, host='0.0.0.0', port=args.port)