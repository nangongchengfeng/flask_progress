# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:45
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : auth.py
# @Software: PyCharm
from flask import Blueprint, render_template

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    # TODO document why this method is empty
    pass



@bp.route("/register")
def register():

    return render_template("register.html")