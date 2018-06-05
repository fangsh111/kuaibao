import sys
sys.path.append('..')
from app import  db
####定义用户model
class user(db.Model):
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(100),index=False)
    blogs=db.relationship('blog',backref='author',lazy='dynamic')
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
