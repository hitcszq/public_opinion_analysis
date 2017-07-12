import sys
from pymongo import *
def store_test_data():
    print "-----------store test data ------------"
    collection = db.test_collection
    with open("../predict_data/Test2.csv","r") as test_data:
        test_data.next()
        for line_itr in test_data:
            if line_itr == "":
                break
            line=line_itr.strip().split("\t")
            sentence_id=line[0]
            content=line[1]
            collection.insert_one({"SentenceId":sentence_id,"Content":content})


def store_predict_data():
    print "-----------store predict data ------------"
    collection=db.predict_collection
    with open("../predict_data/Label_Test2.csv") as predict_data:
        predict_data.next()
        for line_itr in predict_data:
            if line_itr == "":
                break
            line=line_itr.strip().split(",")
            sentence_id=line[0]
            view=line[1]
            opinion=line[2]
            collection.insert_one({"SentenceId":sentence_id,"View":view,"Opinion":opinion})             
        

if __name__ == "__main__":
    client = MongoClient("localhost", 27017)
    db = client.sentiment_db
    store_test_data()
    store_predict_data()
