import os
from datetime import timedelta

SECRET_KEY = 'asdfgaslkjsdfofzj'

BASE_DIR = os.path.dirname(__file__)

HOST = '47.241.35.150'
PORT = '3306'
DATABASE = 'pythonbbs'
USERNAME = 'root'
PASSWORD = 'Kadfgo53254G'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOST,
                                                                                        port=PORT,
                                                                                        db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

PERMANENT_SESSION_LIFETIME = timedelta(days=7)

# MAIL_USE_TLS: 端口号587
# MAIL_USE_SSL: 端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 587
MAIL_USE_TLS = True


MAIL_USERNAME = "250205745@qq.com"
MAIL_PASSWORD = "ebsjinejuvmcbidi"
MAIL_DEFAULT_SENDER = "250205745@qq.com"

# Celery的redis配置
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"

# Flask-Caching
CACHE_TYPE = 'RedisCache'
CACHE_DEFAULT_TIMEOUT = 300
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379

# 头像配置
AVATARS_SAVE_PATH = os.path.join(BASE_DIR, 'media', 'avatars')
