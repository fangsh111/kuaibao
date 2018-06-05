###数据库升级操作
import sys
sys.path.append('..')
from migrate.versioning import api
from app import db
from conf import SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO
api.upgrade(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO)
print('db upgrade done ,current version :' +str(v))