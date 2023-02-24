# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 11:13
# @Author  : 南宫乘风
# @Email   : 1794748404@qq.com
# @File    : logging_tool.py
# @Software: PyCharm
import logging
import os

import colorlog

from common.log_rank import LogRank
# from apollo_config import project_name
# from tools.log_push import dingding_log
project_name="zhiliaooa"
env="dev"
log_path = '../logs/'
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_file = '{}.log'.format(project_name)
# 检测日志目录是否存在
if not os.path.exists(log_path):
    os.makedirs(log_path)


def getLogging(logFilename=log_path + log_file):
    logger = logging.getLogger()

    old_callHandlers = logging.Logger.callHandlers  #

    def callHandlers(self, record):
        try:
            return old_callHandlers(self, record)
        finally:
            if record.levelno == logging.ERROR:
                print(LogRank.error.value, record.message)
                # dingding_log(LogRank.error.value, record.message)
            elif record.levelno == logging.WARN:
                # dingding_log(LogRank.warn.value, record.message)
                print(LogRank.warn.value, record.message)

    if env != 'dev':
        logging.Logger.callHandlers = callHandlers

    if not logger.handlers:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s.%(msecs)03d %(levelname)s | [%(threadName)s] %(name)s [%(lineno)d] | %(filename)s %(funcName)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=logFilename,
            filemode='a')
        filehandler = logging.FileHandler(logFilename, encoding='utf-8')
        logger.addHandler(filehandler)

        # 控制台输出配置
        console_handler = logging.StreamHandler()
        color_conf = colorlog.ColoredFormatter(log_colors={
            'DEBUG': 'cyan',
            'INFO': 'white',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        })
        console_handler.setFormatter(color_conf)
        logger.addHandler(console_handler)
    return logger


logger = getLogging()

if __name__ == '__main__':
    logger.info("1111")
