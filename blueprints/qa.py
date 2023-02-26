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
from .forms import QuestionForm, AnswerForm
from models import QuetionModel, AnswerModel

qa = Blueprint("qa", __name__, url_prefix="/")


@qa.route("/")
def index():
    questions = QuetionModel.query.order_by(QuetionModel.create_time.desc()).all()
    return render_template("index.html", questions=questions)


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


@qa.route("/qa/detail/<qa_id>")
def qa_detail(qa_id):
    question = QuetionModel.query.get(qa_id)
    return render_template("detail.html", question=question)


@qa.route("/answer/public", methods=["POST"])
@login_requir
def answer_public():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content, question_id=question_id, author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for("qa.qa_detail", qa_id=question_id))
    else:
        log.error(form.errors)
        return redirect(url_for("qa.qa_detail", qa_id=request.get("question_id")))

