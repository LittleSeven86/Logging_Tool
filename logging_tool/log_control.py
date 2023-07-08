#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :log_control.py
    @Time      :2023/7/8 15:08
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''
import logging
from logging import handlers
from typing import Text
import colorlog
import time
from common.setting import ensure_path_sep


def singleton(cls):
    '''
    确保每个类只有一个实例。装饰器会在每次创建类的实例时检查该类是否已经有一个实例
    :param cls:
    :return:
    '''
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class LogHandler:
    """日志打印封装"""
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(
            self,
            filename: Text,
            level: Text = "debug",
            when: Text = "D",
            fmt: Text = "%(levelname)-8s%(asctime)s%(name)s:%(filename)s:%(lineno)d 异常信息：%(message)s"
    ):
        self.logger = logging.getLogger(filename)
        formatter = self.log_color()
        # 设置日志格式
        format_str = logging.Formatter(fmt)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 往屏幕上输出
        screen_output = logging.StreamHandler()
        # 设置屏幕上显示的格式
        screen_output.setFormatter(formatter)
        # 指定间隔时间自动生成文件的处理器
        time_rotating = handlers.TimedRotatingFileHandler(
            filename=filename,
            when=when,
            backupCount=3,
            # 防止中文乱码，编码格式为utf-8
            encoding='utf-8'
        )
        time_rotating.setFormatter(format_str)
        # 设置文件的写入格式
        self.logger.addHandler(screen_output)
        self.logger.addHandler(time_rotating)
        self.log_path = ensure_path_sep('\\logs\\log.log')

    @classmethod
    def log_color(cls):
        """设置日志颜色"""
        log_colors_config = {
            'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        }

        formatter = colorlog.ColoredFormatter(
            f'%(log_color)s[%(asctime)s] [%(name)s] [%(levelname)s]: 异常信息：%(message)s',
            log_colors=log_colors_config
        )
        return formatter

    @classmethod
    def info(cls,msg):
        super

now_time_day = time.strftime("%Y-%m-%d", time.localtime())
INFO = LogHandler(ensure_path_sep(f"\\logs\\info-{now_time_day}.log"), level='info')
ERROR = LogHandler(ensure_path_sep(f"\\logs\\error-{now_time_day}.log"), level='error')
WARNING = LogHandler(ensure_path_sep(f'\\logs\\warning-{now_time_day}.log'),level = 'warning')
DEBUG = LogHandler(ensure_path_sep(f'\\logs\\debug-{now_time_day}.log'),level = 'debug')


if __name__ == '__main__':
    ERROR.logger.error("测试")
    INFO.logger.info("测试")
    WARNING.logger.warning("测试")
    DEBUG.logger.debug('测试')
