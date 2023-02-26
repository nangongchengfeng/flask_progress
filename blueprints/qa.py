# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:45
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : qa.py
# @Software: PyCharm
from flask import Blueprint, request, render_template, g, redirect, url_for

from decorators import login_requir
from exts import db
from tool.LogHandler import log
from .forms import QuestionForm
from models import QuetionModel
qa = Blueprint("qa", __name__, url_prefix="/")


@qa.route("/")
def index():
    # TODO document why this method is empty
    return "success"


@qa.route("/qa/public", methods=["GET", "POST"])
@login_requir
def public_qa():
    if request.method == "GET":
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuetionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            log.error(form.errors)
            return redirect(url_for("qa.public_qa"))
