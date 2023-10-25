from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args
import subprocess

#منبع بزن @sourcemr

app = Flask(__name__)


@app.route("/")
#نام ارگومان دلخواه بجای cmd
@use_args({"cmd": fields.Str(required=True)}, location="query")
def index(args):
    try:
        #منبع بزن @sourcemr
        if args["cmd"]=="":
            return "Check args not empty \nsource by Channel @sourcemr"
        elif args["cmd"].startswith("python"):
        	output = subprocess.check_output(args["cmd"], shell=True)
            return output
        else:
            return "Cannot Convert this source to api (403)"
    except subprocess.CalledProcessError as er:
        return str(er)

#پورت در قسمت پورت زده شود
app.run(host="0.0.0.0",port=5230)













#منبع بزن @sourcemr
#منبع واجبه @sourcemr
#منبع نزنی فردا میام سورساتو اسکی میرم @sourcemr


