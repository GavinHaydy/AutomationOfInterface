"""
    @Author: GavinHaydy
    @Email: bugpz2779@gmail.com
    @CSDN: 'https://blog.csdn.net/BUGPZ'
"""
import logging
import logging.handlers
import time
import os


class Log(object):
    """
        logging的初始化操作，以类封装的形式进行
    """

    def __init__(self):
        # 定义对应的程序模块名name，默认为root
        self.logger = logging.getLogger()
        # 设置输出的等级
        levels = {'NOTSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}

        # log_path是存放日志的路径
        time_str = time.strftime('%Y_%m_%d', time.localtime(time.time()))
        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './logs'))
        # 如果不存在这个logs文件夹，就自动创建一个
        if not os.path.exists(lib_path):
            os.mkdir(lib_path)
        # 日志文件的地址
        self.log_name = lib_path + '/' + time_str + '.log'

        # 必须设置，这里如果不显示设置，默认过滤掉warning之前的所有级别的信息
        self.logger.setLevel(logging.INFO)

        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s] [%(filename)s] [%(levelname)s]: %(message)s')
        # [2019-05-15 14:48:52,947] - test.py] - ERROR: this is error

        # 创建一个FileHandler， 向文件log_name输出日志信息
        # fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh = logging.handlers.RotatingFileHandler(filename=self.log_name,
                                                  maxBytes=1024 * 1024 * 50,
                                                  backupCount=5)
        # 设置日志等级
        fh.setLevel(logging.INFO)
        # 设置handler的格式对象
        fh.setFormatter(self.formatter)
        # 将handler增加到logger中
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        # # 关闭打开的文件
        fh.close()

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == "__main__":
    logger = Log()
    logger.info("this is info")
    logger.debug("this is debug")
    logger.error("this is error")
    logger.warning("this is warning")
    logger.critical("critical")
