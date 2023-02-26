from flask import Flask, request
from config import config
from blueprints.qa import qa
from blueprints.auth import bp

from exts import db, mail
from flask_migrate import Migrate
from tool.LogHandler import log
from models import UserModel, EmailCaptchaModel

app = Flask(__name__)

# 导入自定义配置
app.config.from_object(config)
# 数据库初始化
db.init_app(app)
mail.init_app(app)

# 数据库迁移
migrate = Migrate(app, db)
# 蓝图注册
app.register_blueprint(qa)
app.register_blueprint(bp)


# 每一次请求前执行
@app.before_request
def log_each_request():
    path=request.path
    if "static" not in path:
        log.debug('【请求方法】{}  【请求路径】{}  【请求地址】{}'.format(request.method, request.path, request.remote_addr))


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 蓝图  电影模块，音乐模块，读书模块
if __name__ == '__main__':
    log.info('项目已经启动')
    app.run(host="0.0.0.0", port=5010, debug=True)
