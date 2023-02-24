# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:35
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : models.py
# @Software: PyCharm
from datetime import datetime

from exts import db


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)


class EmailCaptchaModel(db.Model):
    __tablename__ = 'email_captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(100), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)
