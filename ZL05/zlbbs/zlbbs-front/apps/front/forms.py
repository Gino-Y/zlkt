from wtforms import Form, ValidationError
from wtforms.fields import StringField
from wtforms.validators import Email, Length, EqualTo
from models.auth import UserModel
from exts import cache
from flask import request

class RegisterForm(Form):
    # 如果使用了Email这个validator，那么就必须要安装email_validator
    # pip install email_validator
    email = StringField(validators=[Email(message='请输入正确的邮箱！')])
    email_captcha = StringField(validators=[Length(6, 6, message='请输入正确格式的邮箱验证码！')])
    username = StringField(validators=[Length(3, 20, message='请输入正确长度的用户名')])
    password = StringField(validators=[Length(6, 20, message='请输入正确长度的密码')])
    repeat_password = StringField(validators=[EqualTo('password', message='两次密码不一致！')])
    graph_captcha = StringField(validators=[Length(4, 4, message='请输入正确长度的图形验证码！')])

    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise ValidationError(message='邮箱已经被注册！')

        def validate_email_captcha(self, field):
            email_captcha = field.data
            email = self.email.data
            cache_captcha = cache.get(email)
            if not cache_captcha or email_captcha != cache_captcha:
                raise ValidationError(message='邮箱验证码错误！')

        def validate_graph_captcha(self, field):
            key = request.cookies.get('_graph_captcha_key')
            cache_captcha = cache.get(key)
            graph_captcha = field.data
            if not cache_captcha or cache_captcha.lower() != cache_captcha.lower():
                raise ValidationError(message='图形验证码错误！')
