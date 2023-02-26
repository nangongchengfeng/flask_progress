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
    password = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)


class EmailCaptchaModel(db.Model):
    __tablename__ = 'email_captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100), nullable=False)
    # False是0,true是1
    used = db.Column(db.Boolean, default=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


class QuetionModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship(UserModel, backref='questions')


class AnswerModel(db.Model):
    __tablename__ = 'anser'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    # 关系
    author = db.relationship(UserModel, backref='answers')
    question = db.relationship(QuetionModel, backref=db.backref('answers', order_by=create_time.desc()))
