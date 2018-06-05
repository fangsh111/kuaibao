from app1 import db
class blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),unique=True)
    content=db.Column(db.String(2000))
    def __init__(self,v_title,v_content):
        self.title=v_title
        self.content=v_content
    def __repr__(self):
        return  '<Blog %r>' %self.title