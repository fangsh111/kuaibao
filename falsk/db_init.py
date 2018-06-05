####创建初始化数据库
import sys
sys.path.append('..')
from migrate.versioning import api
from conf import SQLALCHEMY_DATABASE_URI , SQLALCHEMY_MIGRATE_REPO
from app import  db
import os
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):###
    api.create(SQLALCHEMY_MIGRATE_REPO,'flask_sqllite')
    api.version_control(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO,api.version(SQLALCHEMY_MIGRATE_REPO))