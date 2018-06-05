from app1 import db
class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True)
    passwd=db.Column(db.String(20))
    def __init__(self,uname,upasswd):
        self.username=uname
        self.passwd=upasswd
    def __repr__(self):
        return '<User %r>' %self.username
