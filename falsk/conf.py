import os
import sys
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS=[
    {'name':'qq','url':'https://www.tx.com/qq'},
    {'name':'wx','url':'https://www.tx.com/wx'}
]

###mysk
basedir=os.path.abspath(os.path.dirname('__file__'))####基本目录
# basedir=sys.path[0]
# print(basedir)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')###sqlite数据库
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')#####SQLAlchemy-migrate 存储数据的地方，方便数据库的迁移升级操作？，迁移信息，元数据等？

SQLALCHEMY_TRACK_MODIFICATIONS=True