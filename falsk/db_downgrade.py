######数据库回退到前一个版本
import sys
sys.path.append('..')
from migrate.versioning import api
from app import db
from conf import SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO

v= api.db_version(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO)
api.downgrade(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO,version=v-1)
v = api.db_version(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO)

print('db downgrade done ,current version is '+str(v))
