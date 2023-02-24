# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 9:58
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : apollo_config.py.py
# @Software: PyCharm
import os

from pyapollos import ApolloClient

client = ApolloClient(app_id="zhiliaooa", cluster="default",
                      config_server_url='http://' + os.environ.get('APOLLO_CONFIG_URL'))


#获取邮箱地址的 账号和密码
MAIL_USERNAME = client.get_value('MAIL_USERNAME')
MAIL_PASSWORD  = client.get_value('MAIL_PASSWORD')
# print(MAIL_USERNAME,MAIL_PASSWORD)
# MySQL 账号和密码
HOSTNAME = client.get_value('HOSTNAME')
USERNAME = client.get_value('USERNAME')
PASSWORD = client.get_value('PASSWORD')
DATABASE = client.get_value('DATABASE')


project_name= client.get_value('project_name')
