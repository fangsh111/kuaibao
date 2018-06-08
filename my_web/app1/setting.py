import os

basedir=os.path.abspath(os.path.dirname('__file__'))####基本目录
# basedir=sys.path[0]
# print(basedir)
####sqllite 配置
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app1.db')###sqlite数据库
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')#####SQLAlchemy-migrate 存储数据的地方，方便数据库的迁移升级操作？，迁移信息，元数据等？
SQLALCHEMY_TRACK_MODIFICATIONS=True

###session 会话验证配置
SECRET_KEY='1qaz@WSX#EDC$RFV^YHN*IK<'