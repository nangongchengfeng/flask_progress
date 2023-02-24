# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:32
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : config.py
# @Software: PyCharm
# MySQL所在的主机名
from apollo_config import MAIL_USERNAME, MAIL_PASSWORD,HOSTNAME,USERNAME,PASSWORD,DATABASE

HOSTNAME = HOSTNAME
# MySQL监听的端口号，默认3306
PORT = 3306
# 连接MySQL的用户名，读者用自己设置的
USERNAME = USERNAME
# 连接MySQL的密码，读者用自己的
PASSWORD =PASSWORD
# MySQL上创建的数据库名称
DATABASE = DATABASE
print("调用MySQL地址")
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI=DB_URI

#邮箱地址
MAIL_SERVER = 'smtp.qq.com'
MAIL_PROT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = MAIL_USERNAME
MAIL_PASSWORD = MAIL_PASSWORD
MAIL_DEBUG = True