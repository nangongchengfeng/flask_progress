import traceback

from flask import Flask, request, session, g, make_response, jsonify
from config import config
from blueprints.qa import qa
from blueprints.auth import bp

from exts import db, mail
from flask_migrate import Migrate
from tool.LogHandler import log
from models import UserModel, EmailCaptchaModel
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
app.secret_key = 'CSaSvOU6h1iMb15s+GsV5TuKYSbREcBZ/g1Gjh9nCec='
# 设置session的过期时间
# app.config['PERMANENT_SESSION_LIFETIME'] = 1
#####################################################
# 导入自定义配置
app.config.from_object(config)
# 数据库初始化
db.init_app(app)
mail.init_app(app)


def set_global_exception_handler(app):
    @app.errorhandler(Exception)
    def unhandled_exception(e):
        response = dict()
        error_message = traceback.format_exc()
        app.logger.error("Caught Exception: {}".format(error_message))  # or whatever logger you use
        response["errorMessage"] = error_message
        log.error(response)
        # return response, 500


# set_global_exception_handler(app)
# 数据库迁移
migrate = Migrate(app, db)
################################################
# 蓝图注册
app.register_blueprint(qa)
app.register_blueprint(bp)


# 钩子函数
# hook before_request /before__first_request /after_request
# 每一次请求前执行
@app.before_request
def log_each_request():
    path = request.path
    if "static" not in path:
        log.debug('【请求方法】{}  【请求路径】{}  【请求地址】{}'.format(request.method, request.path, request.remote_addr))


@app.before_request
def my_session():
    if request.endpoint in ("auth", "static"):
        return
    else:
        user_id = session.get('user_id')
        print(session,user_id)
        if user_id:
            user = UserModel.query.get(user_id)
            setattr(g, "user", user)

        else:
            setattr(g, "user", None)


@app.errorhandler(Exception)
def handle_error(Exception):
    log.error(f"Caught Exception: {Exception}")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'code': '404', 'msg': '接口不存在'}), 404)


@app.errorhandler(400)
def par_err(error):
    return make_response(jsonify({'code': '400', 'msg': '请求参数不合法'}), 400)


@app.route('/actuator/health', methods=['GET', 'HEAD'])
def health():
    return jsonify({'online': True})


# 上下文处理器 ,返回所有模板可以使用
@app.context_processor
def my_context_processor():
    return {"user": g.user}


@app.after_request
def after(resp):
    '''
    被after_request钩子函数装饰过的视图函数
    ，会在请求得到响应后返回给用户前调用，也就是说，这个时候，
    请求已经被app.route装饰的函数响应过了，已经形成了response，这个时
    候我们可以对response进行一些列操作，我们在这个钩子函数中添加headers，所有的url跨域请求都会允许！！！
    '''
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


# 蓝图  电影模块，音乐模块，读书模块
if __name__ == '__main__':
    log.info('项目已经启动')
    app.run(host="0.0.0.0", port=5010, debug=True)
