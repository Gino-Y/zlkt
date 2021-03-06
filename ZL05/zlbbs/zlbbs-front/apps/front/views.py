# coding=utf-8

import random, string, time
import os
from flask import (Blueprint,
                   request,
                   render_template,
                   jsonify,
                   current_app,
                   make_response,
                   session,
                   redirect,
                   g)
from exts import cache
from utils import restful
from utils.captcha import Captcha
from hashlib import md5
from io import BytesIO
from .forms import RegisterForm, LoginForm, UploadImageForm
from models.auth import UserModel
from exts import db
from .decorators import login_required
from flask_avatars import Identicon

bp = Blueprint('front', __name__, url_prefix='/')


# 钩子函数：before_request, 在调用视图函数之前执行
@bp.before_request
def front_before_reuqest():
    if 'user_id' in session:
        user_id = session.get('user_id')
        user = UserModel.query.get(user_id)
        setattr(g, 'user', user)


# 上下文处理器
@bp.context_processor
def front_context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    else:
        return {}


@bp.route('/')
def index():
    return render_template('front/index.html')


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
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                return restful.params_error('邮箱或密码错误！')
            if not user.check_password(password):
                return restful.params_error('邮箱或密码错误！')
            session['user_id'] = user.id
            if remember == 1:
                # 默认session过期时间，就是只要浏览器 关闭了就会过期
                session.permanent = True
            return restful.ok()
        else:
            return restful.params_error(message=form.messages[0])


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
            identicon = Identicon()
            filenames = identicon.generate(text=md5(email.encode("utf-8")).hexdigest())
            avatar = filenames[2]
            user = UserModel(email=email,
                             username=username,
                             password=password,
                             avatar=avatar)
            db.session.add(user)
            db.session.commit()
            return restful.ok()
        else:
            # form.errors中存放了所有的错误信息
            message = form.messages[0]
            return restful.params_error(message=message)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@bp.route('/setting')
@login_required
def setting():
    return render_template('front/setting.html')


@bp.post("/avatar/upload")
@login_required
def upload_avatar():
    form = UploadImageForm(request.files)
    if form.validate():
        image = form.image.data
        # 不要使用用户上传上来的文件名，否则容易被黑客攻击
        filename = image.filename
        # xxx.png,xx.jpeg
        _, ext = os.path.splitext(filename)
        filename = md5((g.user.email + str(time.time())).encode("utf-8")).hexdigest() + ext
        image_path = os.path.join(current_app.config['AVATARS_SAVE_PATH'], filename)
        image.save(image_path)
        # 看个人需求，是否图片上传完成后要立马修改用户的头像字段
        g.user.avatar = filename
        db.session.commit()
        return restful.ok(data={"avatar": filename})
    else:
        message = form.messages[0]
        return restful.params_error(message=message)