from flask import Flask
import config
from exts import db,mail
from flask_migrate import Migrate
from models import auth
from apps.front import front_bp
from bbs_celery import make_celery

'''
将ORM模型映射到数据库中三部曲
1、初始化迁移仓库: flask db init
2、将ORM模型生成迁移脚本: flask db migrate
3、运行迁移脚本，生成表: flask db upgrade
'''

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

mycelery = make_celery(app)

# 注册蓝图
app.register_blueprint(front_bp)


if __name__ == '__main__':
    app.run()
