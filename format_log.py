#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os
import datetime

import time

log_path = 'D:\\test'


def clean_log(path):
    os.chdir(path)
    today = datetime.datetime.now()
    offset = datetime.timedelta(days=-1)
    re_date = (today + offset)
    # 转换成时间戳 3天前
    re_date_unix = time.mktime(re_date.timetuple())
    print("当前日期   ", today.strftime('%Y-%m-%d'))  # 当前日期
    print("前3天日期  ", re_date.strftime('%Y-%m-%d'))  # 前3天日期

    # 获取文件ctime
    for i in os.listdir(path):
        file_ctime = os.path.getmtime(i)
        if file_ctime <= re_date_unix:
            # os.remove(i)
            # os.system('rmdir /s/q i')
            print('已经删除得文件:  ', i)
        else:
            print('保留得文件   :  ', i)


clean_log(log_path)
