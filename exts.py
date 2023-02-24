# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:34
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : exts.py
# @Software: PyCharm
# 解决循环运用
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
db = SQLAlchemy()
mail=Mail()
