# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:45
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : auth.py
# @Software: PyCharm
import string
import random
from werkzeug.security import generate_password_hash
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from exts import mail, db
from flask_mail import Message
from tool.LogHandler import log
from models import EmailCaptchaModel, UserModel

from .forms import RegisterForm

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    # TODO document why this method is empty
    pass


# GET :从服务获取数据
# POSt ：将客户端的数据提交个服务器
@bp.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":

        log.info("Registering")
        return render_template("register.html")
    else:
        # Post 去请求
        # 验证用户提交邮箱和验证是否正确
        # 表单验证：flask-wtf
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            log.info(f"用户： {username}  邮箱地址： {password} 已经注册成功")
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            log.info(f"用户注册验证不通过，即将返回注册页面")
            return redirect(url_for("auth.register"))


# 邮箱的验证码
@bp.route("/captcha/email")
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx
    email = request.args.get('email')
    # 4 位： 顺机产生4个数值,字母，数值
    source = string.digits * 4
    captcha = "".join(random.sample(source, 4))
    # IO操作，INPUT /OUTPUT
    message = Message(subject="乘风平台验证码", sender='3063254779@qq.com', recipients=[email],
                      body=f"您的验证码是: {captcha}")
    mail.send(message)

    log.info("Sent email: {} and  captcha : {} ".format(email, captcha))
    emailcaptcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(emailcaptcha)
    db.session.commit()
    # 使用数据库存储
    # Restful API
    # {'code': '200', 'message': '请求成功'}
    return jsonify({'code': 200, 'message': '请求成功'})


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="Test", sender='3063254779@qq.com', recipients=["1794748404@qq.com"], body="Test message")
    mail.send(message)
    return "发送成功"
