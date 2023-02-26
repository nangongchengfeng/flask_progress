# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:45
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : qa.py
# @Software: PyCharm
from flask import Blueprint

qa = Blueprint("qa", __name__, url_prefix="/")


@qa.route("/")
def all_list():
    # TODO document why this method is empty
    return "success"
