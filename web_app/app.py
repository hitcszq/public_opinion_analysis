# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
#from handle_query import handle_query,handle_query_neg,handle_query_price,handle_query_price_pos
from handle_query import * 

app = Flask(__name__,static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def home():
    print "app"
    return render_template('form.html')

@app.route('/query', methods=['POST'])
def deal_q():
    carname = request.form['carname']
    sentiment=handle_query(carname)
    print sentiment
    return render_template("index_query.html", sentiment=sentiment, carname=carname)

@app.route('/zhuzhuangtu/<carname>', methods=['POST','GET'])
def zhuzhuangtu(carname):
    sentiment=handle_query(carname)
    return render_template("zhuzhuangtu.html", sentiment=sentiment,carname=carname)

@app.route('/bingtu/<carname>', methods=['POST','GET'])
def bingtu(carname):
    sentiment=handle_query(carname)
    return render_template("bingtu.html", sentiment=sentiment,carname=carname)

@app.route('/neg/<carname>', methods=['POST','GET'])
def neg(carname):
    pingluntext=handle_query_neg(carname)
    return render_template("details.html",pingluntext=pingluntext)

@app.route('/neu/<carname>', methods=['POST','GET'])
def neu(carname):
    pingluntext=handle_query_neu(carname)
    return render_template("details.html",pingluntext=pingluntext)

@app.route('/pos/<carname>', methods=['POST','GET'])
def pos(carname):
    pingluntext=handle_query_pos(carname)
    return render_template("details.html",pingluntext=pingluntext)

@app.route('/price/<carname>', methods=['POST','GET'])
def aspect_price(carname):
    sentiment=handle_query_price(carname)
    return render_template("aspect.html",sentiment=sentiment,carname=carname,aspect="price",aspectname="价格".decode("utf8"))

@app.route('/exterior/<carname>', methods=['POST','GET'])
def aspect_exterior(carname):
    sentiment=handle_query_exterior(carname)
    return render_template("aspect.html",sentiment=sentiment,carname=carname,aspect="exterior",aspectname="外观".decode("utf8"))

@app.route('/oil/<carname>', methods=['POST','GET'])
def aspect_oil(carname):
    sentiment=handle_query_oil(carname)
    return render_template("aspect.html",sentiment=sentiment,carname=carname,aspect="oil",aspectname="油耗".decode("utf8"))

@app.route('/safe/<carname>', methods=['POST','GET'])
def aspect_safe(carname):
    sentiment=handle_query_safe(carname)
    return render_template("aspect.html",sentiment=sentiment,carname=carname,aspect="safe",aspectname="安全".decode("utf8"))

@app.route('/easy/<carname>', methods=['POST','GET'])
def aspect_easy(carname):
    sentiment=handle_query_easy(carname)
    return render_template("aspect.html",sentiment=sentiment,carname=carname,aspect="easy",aspectname="操控".decode("utf8"))

@app.route('/speed/<carname>', methods=['POST','GET'])
def aspect_speed(carname):
    sentiment=handle_query_speed(carname)
    return render_template("aspect.html",sentiment=sentiment,carname=carname,aspect="speed",aspectname="动力".decode("utf8"))

@app.route('/yueye/<carname>', methods=['POST','GET'])
def aspect_yueye(carname):
    sentiment=handle_query_yueye(carname)
    return render_template("aspect.html",sentiment=sentiment,carname=carname,aspect="yueye",aspectname="越野".decode("utf8"))

@app.route('/shushi/<carname>', methods=['POST','GET'])
def aspect_shushi(carname):
    sentiment=handle_query_shushi(carname)
    return render_template("aspect.html",sentiment=sentiment,carname=carname,aspect="shushi",aspectname="乘坐舒适".decode("utf8"))

@app.route('/aspectpos/<aspect>/<carname>', methods=['POST','GET'])
def aspect_pos(aspect,carname):
    if aspect == "price":
        pingluntext=handle_query_price_pos(carname)
    if aspect == "exterior":
        pingluntext=handle_query_exterior_pos(carname)
    if aspect == "oil":
        pingluntext=handle_query_oil_pos(carname)
    if aspect == "safe":
        pingluntext=handle_query_safe_pos(carname)
    if aspect == "easy":
        pingluntext=handle_query_easy_pos(carname)
    if aspect == "speed":
        pingluntext=handle_query_speed_pos(carname)
    if aspect == "yueye":
        pingluntext=handle_query_yueye_pos(carname)
    if aspect == "shushi":
        pingluntext=handle_query_shushi_pos(carname)
    return render_template("details.html",pingluntext = pingluntext)

@app.route('/aspectneu/<aspect>/<carname>', methods=['POST','GET'])
def aspect_neu(aspect,carname):
    if aspect == "price":
        pingluntext=handle_query_price_neu(carname)
    if aspect == "exterior":
        pingluntext=handle_query_exterior_neu(carname)
    if aspect == "oil":
        pingluntext=handle_query_oil_neu(carname)
    if aspect == "safe":
        pingluntext=handle_query_safe_neu(carname)
    if aspect == "easy":
        pingluntext=handle_query_easy_neu(carname)
    if aspect == "speed":
        pingluntext=handle_query_speed_neu(carname)
    if aspect == "yueye":
        pingluntext=handle_query_yueye_neu(carname)
    if aspect == "shushi":
        pingluntext=handle_query_shushi_neu(carname)
    return render_template("details.html",pingluntext = pingluntext)

@app.route('/aspectneg/<aspect>/<carname>', methods=['POST','GET'])
def aspect_neg(aspect,carname):
    if aspect == "price":
        pingluntext=handle_query_price_neg(carname)
    if aspect == "exterior":
        pingluntext=handle_query_exterior_neg(carname)
    if aspect == "oil":
        pingluntext=handle_query_oil_neg(carname)
    if aspect == "safe":
        pingluntext=handle_query_safe_neg(carname)
    if aspect == "easy":
        pingluntext=handle_query_easy_neg(carname)
    if aspect == "speed":
        pingluntext=handle_query_speed_neg(carname)
    if aspect == "yueye":
        pingluntext=handle_query_yueye_neg(carname)
    if aspect == "shushi":
        pingluntext=handle_query_shushi_neg(carname)
    return render_template("details.html",pingluntext = pingluntext)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
