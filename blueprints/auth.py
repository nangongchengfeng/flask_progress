# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:45
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : auth.py
# @Software: PyCharm
from flask import Blueprint, render_template
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
    log.info("Registering")
    return render_template("register.html")


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="Test",sender='3063254779@qq.com', recipients=["1794748404@qq.com"], body="Test message")
    mail.send(message)
    return "发送成功"
