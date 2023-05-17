from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://JongWoo:use9563@mini.uajgqga.mongodb.net/?retryWrites=true&w=majority  ')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('main.html') 
# 우선 메인페이지 연결함

@app.route('/page2')
def page2():
    return render_template('page2.html') 

@app.route('/teamcard')
def team():
    return render_template('teamcard.html') 


@app.route("/intro", methods=["POST"])
def intro_post():
    comment_receive = request.form['comment_give']

    doc = {
        'comment':comment_receive
    }
    db.intros.insert_one(doc)

    return jsonify({'msg':'댓글 기록 완료!'})

@app.route("/intro", methods=["GET"])
def intro_get():
    all_intros = list(db.intros.find({},{'_id':False}))
    return jsonify({'result':all_intros})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)