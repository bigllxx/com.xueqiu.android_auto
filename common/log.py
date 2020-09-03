import logging
import os
import time

# 创建logs 目录  当前运行脚本绝对路径的上一级/report/logsReport
logsPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report/logsReport')
# print(logsPath)
if not os.path.exists(logsPath):
    os.mkdir(logsPath)


class Log(object):
    # 创建logger
    logger = logging.getLogger(__name__)

    def __init__(self):
        current_day = time.strftime("%Y_%m_%d")
        self.logfile = os.path.join(logsPath, current_day + '.log')

    def __conslole(self, name, msg):
        # 设置日志格式
        format = logging.Formatter('%(asctime)s -%(levelname)s -%(message)s')
        # 设置 打印输出流
        c_handler = logging.StreamHandler()
        c_handler.setFormatter(format)
        #  设置 日志文件记录功能
        f_handler = logging.FileHandler(self.logfile, encoding="utf8")
        f_handler.setFormatter(format)
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)

        # 把输出流和文件写入 设置logger
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

        if name == "debug":
            self.logger.debug(msg)
        elif name == "info":
            self.logger.info(msg)
        elif name == "warn":
            self.logger.warning(msg)
        elif name == 'error':
            self.logger.error(msg, exc_info=True)

        self.logger.removeHandler(c_handler)
        self.logger.removeHandler(f_handler)
        f_handler.close()

    #  定义常用的日志方法

    def debug(self, message):
        self.__conslole('debug', message)

    def info(self, message):
        self.__conslole('info', message)

    def warn(self, message):
        self.__conslole('warn', message)

    def error(self, message):
        self.__conslole('error', message)

