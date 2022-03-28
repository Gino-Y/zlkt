# coding=utf-8

import random
import string


from flask import Blueprint, request, render_template, jsonify, current_app
from flask_mail import Message
from exts import mail
from exts import cache
from utils import restful


bp = Blueprint('front', __name__, url_prefix='/')


@bp.route('/')
def hello_world():
    return 'Hello World!'


@bp.route('/qwe', methods=['GET', 'POST'])
def qwe():
    return 'qwe'



@bp.get("/email/captcha")
def email_captcha():
    # /email/captcha?email=xx@qq.com
    email = request.args.get("email")
    if not email:
        return restful.params_error(message='请先传人邮箱！')
    # 随机的六位数字
    source = list(string.digits)
    captcha = "".join(random.sample(source, 6))
    subject = "【Gino课堂】注册验证码"
    body = '【Gino课堂】您的注册验证码为：{captcha}'.format(captcha=captcha)
    current_app.celery.send_task("send_mail", (email, subject, body))
    cache.set(email, captcha)
    print(cache.get(email))
    return restful.ok(message='邮件发送成功')



@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("front/login.html")


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("front/register.html")
