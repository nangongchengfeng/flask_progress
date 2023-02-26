# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:45
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : qa.py
# @Software: PyCharm
from flask import Blueprint, request, render_template

qa = Blueprint("qa", __name__, url_prefix="/")


@qa.route("/")
def index():
    # TODO document why this method is empty
    return "success"


@qa.route("/qa/public", methods=["GET", "POST"])
def public_qa():
    if request.method == "GET":
        return render_template('public_question.html')
