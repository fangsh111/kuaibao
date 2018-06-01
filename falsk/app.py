from flask import Flask ,render_template,flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired

from contextlib import closing
import json
import re
import requests
import random
from werkzeug.utils import redirect

####登录模块,利用
class login_from(FlaskForm):
    openid=StringField('opneid',validators=[DataRequired()])
    remember_me=BooleanField('remember_me',default=False)

app=Flask(__name__)
###读取配置文件
app.config.from_object('conf')
db= SQLAlchemy(app)

####定义用户model
class user(db.Model):
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(100),index=False)
    def __repr__(self):
        return '<User %r>' %(self.name)

###首页
@app.route('/')
@app.route('/index')
def index():
    user={'name':'fansh',}
    return render_template('index.html',title='首页',user=user)
####登录
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form =login_from()
    ####登录提交成功，跳转到index界面
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    ####在
    return render_template('login.html',form= form,providers= app.config['OPENID_PROVIDERS'])



if __name__=='__main__':
    app.debug = True
    app.run('127.0.0.1')
