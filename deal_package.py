# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 22:06
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : deal_package.py.py
# @Software: PyCharm
import os


# 列出项目使用的依赖
def export_package():
    # os.system("pipreqs ./ --encoding='utf-8' --force")
    os.system("pip freeze > requirements.txt")


# 安装项目使用的依赖
def input_package():
    os.system("pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple")


if __name__ == '__main__':
    export_package()
