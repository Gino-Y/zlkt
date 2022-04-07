from wtforms import Form
from wtforms.fields import StringField
from wtforms.validators import Email, Length, EqualTo

class RegisterForm(Form):
    email = StringField(validators=[Email(message='请输入正确的邮箱！')])
    email_captcha = StringField(validators=[Length(6, 6, message='请输入正确格式的邮箱验证码！')])
    username = StringField(validators=[Length(3, 20, message='请输入正确长度的用户名')])
    password = StringField(validators=[Length(6, 20, message='请输入正确长度的密码')])
    repeat_password = StringField(validators=[EqualTo('password', message='两次密码不一致！')])
    graph_captcha = StringField(validators=[Length(4, 4, message='请输入正确长度的图形验证码！')])

    def validate_email(self, field):
        email = field.data