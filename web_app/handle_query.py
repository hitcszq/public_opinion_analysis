# -*- coding:utf-8 -*-  
import sys
from pymongo import *

def handle_query(car_query):
    neg_num = 0
    pos_num = 0
    neu_num = 0
    re_query=".*"+car_query+".*"
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    collection = db.predict_collection
    cursor = collection.find({"View":{'$regex' : re_query}})  
    for itr in cursor:
        if itr["Opinion"] == "neg":
            neg_num+=1
        elif itr["Opinion"] == "neu":
            neu_num+=1
        else:
            pos_num+=1
    return (neg_num,neu_num,pos_num)

def handle_query_neg(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    for itr in cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        pingluntext.append(neg_test["Content"])
    return pingluntext

def handle_query_pos(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    for itr in cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        pingluntext.append(pos_test["Content"])
    return pingluntext

def handle_query_neu(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        pingluntext.append(neu_test["Content"])
    return pingluntext


def handle_query_price(car_query):
    neg_num = 0
    pos_num = 0
    neu_num = 0
    re_query=".*"+car_query+".*"
    price_list=["价格","实惠","性价比","优惠","便宜","贵","经济"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neg_num+=1
                break
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pos_num+=1
                break
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neu_num+=1
                break
    return neg_num,neu_num,pos_num

def handle_query_price_neg(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["价格","实惠","性价比","优惠","便宜","贵","经济"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neg_test["Content"])
                break
    return pingluntext

def handle_query_price_neu(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["价格","实惠","性价比","优惠","便宜","贵","经济"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neu_test["Content"])
                break
    return pingluntext


def handle_query_exterior(car_query):
    neg_num = 0
    pos_num = 0
    neu_num = 0
    re_query=".*"+car_query+".*"
    price_list=["曲面","身姿","气质","外观","造型","外型","形态","车型"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neg_num+=1
                break
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pos_num+=1
                break
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neu_num+=1
                break
    return neg_num,neu_num,pos_num

def handle_query_exterior_neg(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["曲面","身姿","气质","外观","造型","外型","形态","车型"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neg_test["Content"])
                break
    return pingluntext

def handle_query_exterior_pos(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["曲面","身姿","气质","外观","造型","外型","形态","车型"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(pos_test["Content"])
                break
    return pingluntext

def handle_query_exterior_neu(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["曲面","身姿","气质","外观","造型","外型","形态","车型"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in pos_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neu_test["Content"])
                break
    return pingluntext


def handle_query_safe(car_query):
    neg_num = 0
    pos_num = 0
    neu_num = 0
    re_query=".*"+car_query+".*"
    price_list=["制动","稳定","安全"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neg_num+=1
                break
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pos_num+=1
                break
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neu_num+=1
                break
    return neg_num,neu_num,pos_num

def handle_query_safe_neg(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["制动","稳定","安全"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neg_test["Content"])
                break
    return pingluntext

def handle_query_safe_pos(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["制动","稳定","安全"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(pos_test["Content"])
                break
    return pingluntext

def handle_query_safe_neu(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["制动","稳定","安全"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neu_test["Content"])
                break
    return pingluntext


def handle_query_oil(car_query):
    neg_num = 0
    pos_num = 0
    neu_num = 0
    re_query=".*"+car_query+".*"
    price_list=["节能","环保","油","能源","燃料"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neg_num+=1
                break
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pos_num+=1
                break
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neu_num+=1
                break
    return neg_num,neu_num,pos_num

def handle_query_oil_pos(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["节能","环保","油","能源","燃料"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(pos_test["Content"])
                break
    return pingluntext

def handle_query_oil_neg(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["节能","环保","油","能源","燃料"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neg_test["Content"])
                break
    return pingluntext

def handle_query_oil_neu(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["节能","环保","油","能源","燃料"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neu_test["Content"])
                break
    return pingluntext

def handle_query_price_pos(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["价格","实惠","性价比","优惠","便宜","贵","经济"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(pos_test["Content"])      
                break
    return pingluntext

def handle_query_easy(car_query):
    neg_num = 0
    pos_num = 0
    neu_num = 0
    re_query=".*"+car_query+".*"
    price_list=["操纵","方便"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neg_num+=1
                break
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pos_num+=1
                break
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neu_num+=1
                break
    return neg_num,neu_num,pos_num

def handle_query_easy_pos(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["操纵","方便"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(pos_test["Content"])
                break
    return pingluntext

def handle_query_easy_neg(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["操纵","方便"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neg_test["Content"])
                break
    return pingluntext

def handle_query_easy_neu(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["操纵","方便"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neu_test["Content"])
                break
    return pingluntext

def handle_query_speed(car_query):
    neg_num = 0
    pos_num = 0
    neu_num = 0
    re_query=".*"+car_query+".*"
    price_list=["车速","速度","加速","爬坡"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neg_num+=1
                break
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pos_num+=1
                break
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neu_num+=1
                break
    return neg_num,neu_num,pos_num

def handle_query_speed_neg(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["车速","速度","加速","爬坡"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neg_test["Content"])
                break
    return pingluntext

def handle_query_speed_neu(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["车速","速度","加速","爬坡"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neu_test["Content"])
                break
    return pingluntext

def handle_query_speed_pos(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["车速","速度","加速","爬坡"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(pos_test["Content"])
                break
    return pingluntext

     
def handle_query_shushi(car_query):
    neg_num = 0
    pos_num = 0
    neu_num = 0
    re_query=".*"+car_query+".*"
    price_list=["舒适","惬意","平顺"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neg_num+=1
                break
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pos_num+=1
                break
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neu_num+=1
                break
    return neg_num,neu_num,pos_num

def handle_query_shushi_neg(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["舒适","惬意","平顺"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neg_test["Content"])
                break
    return pingluntext

def handle_query_shushi_neu(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["舒适","惬意","平顺"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neu_test["Content"])
                break
    return pingluntext

def handle_query_shushi_pos(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["舒适","惬意","平顺"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(pos_test["Content"])
                break
    return pingluntext
    
def handle_query_yueye(car_query):
    neg_num = 0
    pos_num = 0
    neu_num = 0
    re_query=".*"+car_query+".*"
    price_list=["越野","机动"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neg_num+=1
                break
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pos_num+=1
                break
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                neu_num+=1
                break
    return neg_num,neu_num,pos_num

def handle_query_yueye_neg(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["越野","机动"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neg_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neg"})
    for itr in neg_cursor:
        neg_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neg_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neg_test["Content"])
                break
    return pingluntext

def handle_query_yueye_neu(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["越野","机动"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    neu_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"neu"})
    for itr in neu_cursor:
        neu_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if neu_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(neu_test["Content"])
                break
    return pingluntext

def handle_query_yueye_pos(car_query):
    pingluntext=[]
    re_query=".*"+car_query+".*"
    price_list=["越野","机动"]
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    pre_collection = db.predict_collection
    test_collection=db.test_collection
    pos_cursor = pre_collection.find({"View":{'$regex' : re_query},"Opinion":"pos"})
    for itr in pos_cursor:
        pos_test=test_collection.find_one({"SentenceId":itr["SentenceId"]})
        for price_dc in price_list:
            if pos_test["Content"].find(price_dc.decode("utf8"))!=-1:
                pingluntext.append(pos_test["Content"])
                break
    return pingluntext


 
if __name__ == "__main__":
    test_query="宝马"
    handle_query(test_query)
    #handle_query_neg(test_query)
    #handle_query_price(test_query)
    #handle_query_price_pos(test_query)
