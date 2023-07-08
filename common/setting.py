#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :setting.py
    @Time      :2023/7/8 15:05
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''

import os
from typing import Text


def root_path():
    '''
    :return: 返回当前项目根路径
    '''
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def ensure_path_sep(path: Text) -> Text:
    '''
    兼容 windows 和 linux 不同环境的操作系统路径
    :param path: 路径参数
    :return: 路径
    '''
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return root_path() + path

if __name__ == '__main__':
    res = root_path()
    print(res)