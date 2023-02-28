# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 11:23
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : manager.py.py
# @Software: PyCharm
import os

from flask_migrate import Migrate
from flask_script import Manager

from app import app
from exts import db

db_manager = Manager()
Migrate(app, db)


@db_manager.command
def init():
    # 模拟操作
    os.system('flask db init')
    print('迁移仓库创建完毕...')


@db_manager.command
def migrate():
    # 模拟操作
    os.system('flask db migrate')
    print('迁移脚本生成成功...')


@db_manager.command
def upgrade():
    # 模拟操作
    os.system('flask db upgrade')
    print('脚本映射到数据库成功...')


# 报错  ： 不降级则可以尝试修改一下flask_script/__init__.py中from ._compat import text_type 改成 from flask_script._compat import text_type

manager = Manager(app)
manager.add_command('db', db_manager)


@manager.command
def hello():
    print('hello')


if __name__ == '__main__':
    manager.run()
