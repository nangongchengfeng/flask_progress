# -*- coding: utf-8 -*-
# @Time    : 2023/2/26 18:40
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : decorators.py
# @Software: PyCharm
from flask import session, redirect, g, url_for
from functools import wraps


def login_requir(func):
    @wraps(func)  # 保留源信息，本质是endpoint装饰，否则修改函数名很危险
    def inner(*args, **kwargs):  # 接收参数，*args接收多余参数形成元组，**kwargs接收对于参数形成字典
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))  # 没有登录就跳转到登录路由下

    return inner
