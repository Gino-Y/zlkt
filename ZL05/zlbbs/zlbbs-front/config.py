SECRET_KEY = 'asdfgaslkjsdfofzj'

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'pythonbbs'
USERNAME = 'root'
PASSWORD = ''

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOST,
                                                                                        port=PORT,
                                                                                        db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True


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


