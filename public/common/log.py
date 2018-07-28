# -*- coding:utf-8 -*-
import logging
import time
import os
from config import globalparam

log_path = globalparam.log_path


class Log:
    def __init__(self):
        #字符串的参数使用{NUM}进行表示，0表示第一个参数，1表示第二个参数，以后顺次递加
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __printconsole(self, level, message):
         #创建一个logger
         logger = logging.getLogger()
         #设置日志级别
         logger.setLevel(logging.DEBUG)
         #创建一个handler,用于写入日志文件
         fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
         fh.setLevel(logging.DEBUG)
         #再创建一个handler，用于输出到控制台
         ch = logging.StreamHandler()
         ch.setLevel(logging.DEBUG)
         #定义handler的输出格式
         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
         fh.setFormatter(formatter)
         ch.setFormatter(formatter)
         #给logger添加handler
         logger.addHandler(fh)
         logger.addHandler(ch)
         #记录一条日志
         if level == 'info':
             logger.info(message)
         elif level == 'debug':
             logger.debug(message)
         elif level =='warning':
             logger.warning(message)
         elif level == 'error':
             logger.error(message)
         logger.removeHandler(ch)
         logger.removeHandler(fh)
         #关闭打开的文件
         fh.close()

    def debug(self, message):

        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)
