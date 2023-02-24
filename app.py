from flask import Flask
import config
from blueprints.qa import qa
from blueprints.auth import bp

from exts import db, mail
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)
mail.init_app(app)


migrate = Migrate(app, db)

app.register_blueprint(qa)
app.register_blueprint(bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 蓝图  电影模块，音乐模块，读书模块
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
