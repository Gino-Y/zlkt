# coding=utf-8


import random
import string

from flask import Blueprint, request, render_template, jsonify
from flask_mail import Message
from exts import mail

bp = Blueprint('front', __name__, url_prefix='/')


@bp.route('/')
def hello_world():
    return 'Hello World!'


@bp.route('/qwe', methods=['GET', 'POST'])
def qwe():
    return 'qwe'


@bp.get("/email/captcha")
def email_captcha():
    email = request.args.get("email")
    if not email:
        return jsonify({"code": 400,
                        "message": "请先传人邮箱"})
    # 随机生成6位数字
    source = list(string.digits)
    captcha = ''.join(random.sample(source, 6))
    message = Message(subject='【Gino课堂】注册验证码',
                      recipients=[email],
                      body='【Gino课堂】您的注册验证码为：{digits}'.format(digits=captcha),
                      charset='utf8')
    try:
        mail.send(message)
    except Exception as e:
        print('邮件发送失败')
        print(e)
        return jsonify({'code': 500,
                        'message': '邮件发送失败'})

    return jsonify({'code': 200,
                    'message': '邮件发送成功'})


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("front/login.html")


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("front/register.html")
