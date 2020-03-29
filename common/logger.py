import logging
from logging.handlers import RotatingFileHandler
from common.constant import LOGS_DIR
from common.configer import conf
from common.move_dir import file_log


class Logger:

    def __new__(cls, *args, **kwargs):
        file = file_log(LOGS_DIR)

        log_config = conf.get_conf("log")
        # 实例化日志收集器
        log = logging.getLogger("AutoApiTest")
        log.setLevel(log_config['logger_level'])

        # 设置日志格式
        log_fmt = logging.Formatter(fmt='%(asctime)s - 【%(levelname)s】: \n%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        #print(log_fmt.__str__())

        # 实例化控制台渠道
        log_stream = logging.StreamHandler()
        log_stream.setFormatter(log_fmt)
        log_stream.setLevel(log_config['stream_level'])

        # 实例化输出文件渠道
        log_file = logging.FileHandler(file, encoding="UTF-8")
        log_file.setFormatter(log_fmt)
        log_file.setLevel(log_config['file_level'])

        # 日志文件过大处理, 当单个日志文件大于10M时, 重新开新的文件, 最多4个
        log_rotating = RotatingFileHandler(file, maxBytes=2684354, backupCount=3, encoding="utf8")
        log_rotating.setFormatter(log_fmt)
        log_rotating.setLevel(log_config['file_level_rf'])

        # 将实例化渠道添加到收集器中
        log.addHandler(log_stream)
        # log.addHandler(log_file)
        log.addHandler(log_rotating)
        return log


logger = Logger()


if __name__ == '__main__':
    logger.info("asfasfsafas")
