from flask import Flask
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)
app.config.from_object('app1.setting')
db= SQLAlchemy(app)
from app1.model import  user,blog
from app1.controller import blog_message

#####登录插件

