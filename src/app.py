from distutils.text_file import TextFile
from flask import Flask, render_template, redirect, url_for, request

from mongoengine import connect
#from pymongo import MongoClient

from models import Article


app = Flask(__name__)

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0')





@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#returns all posts for germany
@app.route('/germany/')
def show_germany(name):
    german_posts = Article.objects.filter(temp_country='germany', )
    return render_template()


