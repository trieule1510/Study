
limport argparse
from flask import Flask,render_template

app =Flask(__name__)
parser = argparse.ArgumentParser(description='db')
parser.add_argument('--port', dest='port',default=1234,type=int,help='www port''mlr')
args = parser.parse_args()

@app.route("/", methods=['POST', 'GET'])
def hello():
    msg="I'm Trieu Le"
    counted = [35, 47, 39, 24, 50]
    for v in counted:
        print("v=", v)
    return render_template('for.html',counted=counted)

if __name__=="__main__":
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host= '0.0.0.0', port=args.port)


