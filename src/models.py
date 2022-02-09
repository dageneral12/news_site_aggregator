from mongoengine import *
import datetime


connect('news_base')
#connect using web protocol: 
#connect(host="mongodb://127.0.0.1:27017/my_db")
#connect('my_db', host='127.0.0.1', port=27017, username='my_user', password='my_password', authentication_source='admin')


COUNTRIES = (('Germany', 'Germany'),
        ('USA', 'United States'),
        ('UK', 'United Kingdom'),
        ('Russia', 'Russia'))

class Article(Document):
    article_tile = StringField(required=True)
    article_date = DateTimeField(default=datetime.datetime.utcnow())
    article_country = StringField(required=True)            #choices = COUNTRIES
    article_body = StringField(max_length=10000)
    temp_article = BooleanField(required=True)