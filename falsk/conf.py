import os
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS=[
    {'name':'qq','url':'https://www.tx.com/qq'},
    {'name':'wx','url':'https://www.tx.com/wx'}
]

###mysk
basedir=os.path.abspath(os.path.dirname('__file__'))####基本目录
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')###sqlite数据库
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')#####