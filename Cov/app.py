from flask import Flask
from flask import render_template
from flask import jsonify
from decimal import Decimal
from jieba.analyse import extract_tags
import json
import utils
import string


app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello():
    return render_template("/main.html")

@app.route('/main', methods=["GET","POST"])
def main():
    return render_template("/main.html")

@app.route('/time', methods=["GET","POST"])
def time():
    return utils.get_time()

@app.route('/c1', methods=["GET","POST"])
def get_c1_data():
    data = utils.get_c1_data()
    result = jsonify({"confirm": str(Decimal(data[0])), "suspect": str(Decimal(data[1])), "heal": str(Decimal(data[2])), "dead": str(Decimal(data[3]))})
    return result

@app.route('/c2', methods=["GET","POST"])
def get_c2_data():
    res=[]
    data = utils.get_c2_data()
    for tup in data:
        res.append({"name":tup[0],"value":int(str(tup[1]))})
    result = jsonify({"data": res})
    return result

@app.route('/l1', methods=["GET","POST"])
def get_l1_data():
    data = utils.get_l1_data()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    result = jsonify({"day": day,"confirm": confirm, "suspect": suspect, "heal": heal,"dead":dead})
    return result

@app.route('/l2', methods=["GET","POST"])
def get_l2_data():
    data = utils.get_l2_data()
    day,confirm_add,suspect_add = [],[],[]
    for a,b,c in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        suspect_add.append(c)

    result = jsonify({"day": day,"confirm_add": confirm_add, "suspect_add": suspect_add})
    return result

@app.route('/r1', methods=["GET","POST"])
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k,v in data:
        city.append(k)
        confirm.append(int(v))

    result = jsonify({"city":city,"confirm":confirm})
    return result

@app.route('/r2', methods=["GET","POST"])
def get_r2_data():
    data = utils.get_r2_data()
    d = []
    for i in data:
        k = i[0].rstrip(string.digits)
        v = i[0][len(k):]
        ks = extract_tags(k)
        for j in ks:
            if not j.isdigit():
                d.append({"name":j,"value": v})
    result = jsonify({"kws":d})
    return result
if __name__ == '__main__':
    app.run()
