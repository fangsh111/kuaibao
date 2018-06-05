#####数据库迁移脚本
import sys
sys.path.append('..')
import imp
from migrate.versioning import api
from app import db
from conf import SQLALCHEMY_MIGRATE_REPO,SQLALCHEMY_DATABASE_URI

v=api.db_version(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO) #获取当的版本号
migration=SQLALCHEMY_MIGRATE_REPO+('/versions/%03d_migration.py' %(v+1))###

tmp_model=imp.new_module('old_model')
old_model=api.create_model(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO)
exec(old_model,tmp_model.__dict__)
script = api.make_update_script_for_model(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO,oldmodel=tmp_model.meta,model=db.metadata)
open(migration,'wt').write(script)
api.upgrade(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(url=SQLALCHEMY_DATABASE_URI,repository=SQLALCHEMY_MIGRATE_REPO)

print('new migration saved as '+migration)
print('current db version: ' +str(v))
