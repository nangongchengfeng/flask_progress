# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:45
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : auth.py
# @Software: PyCharm
import string
import random

from flask import Blueprint, render_template, request
from exts import mail
from flask_mail import Message
from flask import Flask, current_app
from tool.LogHandler import log

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    # TODO document why this method is empty
    pass


@bp.route("/register")
def register():
    # 验证用户提交邮箱和验证是否正确
    log.info("Registering")
    return render_template("register.html")


# 邮箱的验证码
@bp.route("/captcha/email")
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx
    email = request.args.get('email')
    # 4 位： 顺机产生4个数值,字母，数值
    source = string.digits * 4
    captcha = "".join(random.sample(source, 4))
    message = Message(subject="乘风平台验证码", sender='3063254779@qq.com', recipients=[email], body=f"您的验证码是: {captcha}")
    mail.send(message)
    print(captcha)
    #使用数据库存储

    return "发送邮件验证码成功"


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="Test", sender='3063254779@qq.com', recipients=["1794748404@qq.com"], body="Test message")
    mail.send(message)
    return "发送成功"
