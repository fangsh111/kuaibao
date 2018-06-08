from app1.model.user import user
from app1.model.blog import blog

from app1 import app ,db
from flask import request,render_template,flash,url_for,redirect,session,Flask,g,abort

@app.route('/')
def show_blogs():
    blogs = blog.query.all()
    return render_template('show_blog.html',blogs=blogs)

@app.route('/add',methods=['POST'])
def add_blog():
    if not session.get('logged_in'):
        print('没有登录')
        abort(401)
    title= request.form['title']
    content = request.form['text']
    one_blog=blog(title,content)
    db.session.add(one_blog)
    db.session.commit()
    flash('blog保存成功')
    return redirect(url_for('show_blogs'))

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        username=request.form['username']
        passwd=request.form['password']
        uname=user.query.filter_by(username=request.form['username']).first()
        upasswd=user.query.filter_by(passwd=request.form['password']).first()
        if uname is None :
            error='用户名不存在'
            return render_template('login.html', error=error)
        elif upasswd is None:
            error='密码不对'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] =True
            flash('登录成功！！')
            return redirect(url_for('show_blogs'))
    return render_template('login.html', error=error)
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('成功退出系统')
    return redirect(url_for('show_blogs'))


