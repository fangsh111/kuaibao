from flask import Flask ,render_template,flash,g,url_for,session
from flask_wtf import FlaskForm ####表单模块
from flask_sqlalchemy import SQLAlchemy ###数据库模块
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired
from werkzeug.utils import redirect ###重定向


import os
from flask_login import LoginManager,current_user
from flask_openid import OpenID
from conf import basedir





####登录模块,利用FlaskForm进行控制和验证
class login_from(FlaskForm):
    openid=StringField('opneid',validators=[DataRequired()])
    remember_me=BooleanField('remember_me',default=False)

app=Flask(__name__)
###读取配置文件
app.config.from_object('conf')
db= SQLAlchemy(app)

lm=LoginManager()
lm.init_app(app=app)
lm.login_view='login'
open_id =OpenID(app=app,fs_store_path=os.path.join(basedir,'tmp'))



####定义用户model
class user(db.Model):
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(100),index=False)
    blogs=db.relationship('blog',backref='author',lazy='dynamic')
    ####flask_login模块需要加一些函数
    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return  False
    def get_id(self):
        try:
            return unicode(self.id) ###python2 ???还有这操作，不太懂哎？_？
        except NameError:
            return str(self.id) #####python3

    def __repr__(self):
        return '<User %r>' %(self.name)
####定义博客model
class blog(db.Model):
    id=db.Column(db.INTEGER,primary_key=True)
    body=db.Column(db.String(300))
    timestamp=db.Column(db.DateTime)
    user_id=db.Column(db.INTEGER,db.ForeignKey(user.id))
    def __repr__(self):
        return '<blog %3>' %(self.body)

# @app.route('/')
###首页
@app.route('/index')
def index():
    user={'name':'fansh',}
    ###加载首页
    return render_template('index.html',title='首页',user=user)


@app.before_request
def  before_request():
    g.u=current_user

####获取id对应的user
@lm.user_loader
def load_user(id):
    return user.query.get(int(id))
####登录模块
@app.route('/login', methods = ['GET', 'POST'])
@open_id.loginhandler
def login():
    if g.u is not None and g.u.is_authenticated():
        return redirect(url_for('index'))
    form =login_from()
    ####登录提交成功，跳转到index界面
    if form.validate_on_submit():
        session['remember_me']=form.remember_me.data
        return open_id.try_login(form.openid.data,ask_for=['name','email'])
        # flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        # return redirect('/index')
    ####加载登录界面
    return render_template('login.html',form= form,providers= app.config['OPENID_PROVIDERS'])

if __name__=='__main__':
    app.debug = True
    app.run('127.0.0.1')
