# Flask

## 介绍

- Flask 是一个轻量级的 Web 开发框架
- 基于 Python 编写，适用于开发小型应用和 API

## 基础知识

### 安装和配置

- 使用 `pip` 安装 Flask：`pip install flask`
- 导入 Flask 库：`from flask import Flask`

### 应用程序

- 创建应用程序对象：`app = Flask(__name__)`，其中 `__name__` 参数为当前模块名
- 默认情况下，静态文件夹（即存放静态文件的文件夹）和模板文件夹（即存放 HTML 文件的文件夹）位于应用程序根目录中的 `static` 和 `templates` 文件夹中。可以通过 `static_folder` 和 `template_folder` 参数指定其他位置。
- 使用 `debug=True` 参数开启调试模式。
- 设置根路由响应函数：`@app.route('/')` 和 `def index():`

### 运行应用程序

- 通过命令行运行：`flask run`，默认端口为 5000。
- 或者在代码中运行：`if __name__ == '__main__': app.run()`。

## 路由

### 静态路由

- @app.route('/hello') 可以匹配 `http://localhost:5000/hello` 请求
- 使用 `methods=['GET']` 参数指定 HTTP 方法。

### 动态路由

- 变量规则：使用尖括号表示变量名。例如 `@app.route('/user/<username>')` 可以匹配 `http://localhost:5000/user/john` 请求。
- 可以使用 '{variable: type}' 指定变量类型。例如 `@app.route('/post/<int:post_id>')` 表示 post_id 只能是整数类型。
- 同时使用多个变量：例如 `@app.route('/path/<path:subpath>')` 表示 subpath 可以包含斜杠 `/`。

### HTTP 方法

- 支持不同的 HTTP 方法：`@app.route('/login', methods=['GET', 'POST'])`
- 常用的方法：`GET`、`POST`、`PUT`、`DELETE`

### URL 生成

- 使用 `url_for()` 函数生成 URL。例如 `url_for('index')` 会返回 `/`。

### 重定向和错误处理

- 重定向：使用 `redirect()` 函数，例如 `return redirect(url_for('index'))`。
- 错误处理：使用 `@app.errorhandler()` 装饰器和对应的响应函数，例如 `@app.errorhandler(404)` 和 `def page_not_found(error):`。

## 模板

### Jinja2 模板引擎

- 使用模板：`render_template('index.html', name=name)`，第一个参数为模板文件名，后面的参数为模板上下文。
- 在模板中使用变量：使用双花括号表示，例如 `Hello, {{ name }}!`。
- 在模板中使用控制结构：使用 `{% %}` 标签，例如 `{% if user %} Hello, {{ user }}! {% else %} Hello, Stranger! {% endif %}`。
- 继承模板：`{% extends "base.html" %}`，表示该模板继承自 base.html 模板。
- 定义块：`{% block content %}` 和 `{% endblock %}`，可以在子模板中重写。
- 包含模板：`{% include "common.html" %}`，将 common.html 模板引入到当前模板中。

### 静态文件

- 存放位置：应用程序根目录下的 `static` 文件夹。
- 使用方式：`url_for('static', filename='style.css')`。

## 表单

### WTForms 扩展

- 安装扩展库：`pip install flask-wtf`
- 导入扩展库：`from flask_wtf import FlaskForm`
- 定义表单类：`class LoginForm(FlaskForm):`，每个字段都是一个实例化后的 wtforms 字段。
- 渲染表单：`{{ form.username.label }} {{ form.username() }}`，label 表示字段的标签（即描述），() 表示渲染成 HTML 元素。

### CSRF 防护

- 使用 Flask-WTF 扩展提供的 CSRF 防护机制。
- 设置应用程序的 SECRET_KEY 属性。

## 数据库

### SQLAlchemy 扩展

- 安装扩展库：`pip install flask-sqlalchemy`
- 导入扩展库：`from flask_sqlalchemy import SQLAlchemy`
- 配置数据库连接：`app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'`
- 创建数据库实例：`db = SQLAlchemy(app)`
- 定义数据表：`class User(db.Model):`，自定义数据表需要继承 db.Model 类。
- 在数据表中定义字段：例如 `id = db.Column(db.Integer, primary_key=True)`，表示 id 为整数类型，是主键。
- 创建数据表：`db.create_all()`

### 数据操作

- 添加数据：`user = User(username='tom', password='123')` 和 `db.session.add(user)`。
- 查询数据：`user = User.query.filter_by(username='tom').first()`，使用过滤器进行数据的查询。
- 更新数据：`user.password = '456'` 和 `db.session.commit()`，更新字段值后调用 commit() 函数提交到数据库。
- 删除数据：`db.session.delete(user)` 和 `db.session.commit()`，删除记录时同样需要调用 commit() 函数。

## 蓝图

- 概述：将应用程序分割成不同的模块，每个模块都有自己的路由和视图函数。
- 创建蓝图：`bp = Blueprint('auth', __name__, url_prefix='/auth')`，其中 `auth` 是蓝图名称，`url_prefix` 参数指定蓝图的 URL 前缀。
- 注册蓝图：`app.register_blueprint(bp)`。

## 登录

- Flask-Login 扩展提供了用户认证和登录的功能。
- 安装扩展库：`pip install flask-login`
- 导入扩展库：`from flask_login import LoginManager, login_user, logout_user, current_user`
- 配置登录管理器：`login_manager = LoginManager(app)`， `login_manager.login_view = 'login'`，`login_manager.login_message = u"请先登录"`
- 定义 User 类：`class User(UserMixin, db.Model):`，自定义 User 类需要继承 UserMixin 类并在数据库实例中初始化。
- 定义表单：与使用 WTForms 扩展类似，只需要在表单类中定义相应的字段。
- 实现登录逻辑：`if form.validate_on_submit():`，验证表单数据后调用 `login_user(user, remember=form.remember_me.data)` 完成登录。
- 实现登出逻辑：`logout_user()`。
- 实现登录保护：使用 `@login_required` 装饰器，例如 `@app.route('/secret') @login_required def secret():`。

## 邮件

- Flask-Mail 扩展提供了邮件发送的功能。
- 安装扩展库：`pip install flask-mail`
- 导入扩展库：`from flask_mail import Mail, Message`
- 配置邮件：`app.config['MAIL_SERVER'] = 'smtp.163.com'`，`app.config['MAIL_PORT'] = 465`，`app.config['MAIL_USE_SSL'] = True`，`app.config['MAIL_USE_TLS'] = False`，`app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')`，`app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')`
- 创建邮件实例：`mail = Mail(app)`
- 发送邮件：`msg = Message('Hello', sender='sender@example.com', recipients=['recipient@example.com'])`，`msg.body = "This is a test email."`，`mail.send(msg)`。

## RESTful API

- Flask-RESTful 扩展提供了支持 RESTful API 的功能。
- 安装扩展库：`pip install flask-restful`
- 导入扩展库：`from flask_restful import Resource, Api`
- 创建 API 实例：`api = Api(app)`
- 定义资源：`class TodoList(Resource):`，在类中定义 HTTP 方法，例如 `def get(self):`（处理 GET 请求）。
- 添加资源到 API：`api.add_resource(TodoList, '/todos')`，其中 `/todos` 是 URL 路径。
