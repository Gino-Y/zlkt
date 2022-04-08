# coding=utf-8

import random, string, time

from flask import Blueprint, request, render_template, jsonify, current_app, make_response
from exts import cache
from utils import restful
from utils.captcha import Captcha
from hashlib import md5
from io import BytesIO
from .forms import RegisterForm
from models.auth import UserModel
from exts import db

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


@bp.route('/graph/capthca')
def graph_captcha():
    captcha, image = Captcha.gene_graph_captcha()
    # 将验证码存放在缓存中
    # key, value
    # bytes
    key = md5((captcha + str(time.time())).encode('utf-8')).hexdigest()
    cache.set(key, captcha)
    out = BytesIO()
    image.save(out, 'png')
    # 把out的文件指针指向最开始的位置（归位）
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image / png'
    resp.set_cookie('_graph_captcha_key', key, max_age=1800)
    return resp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("front/login.html")


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("front/register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return restful.ok()
        else:
            # form.errors中存放了所有的错误信息
            print(form.errors)
            return 'failure'