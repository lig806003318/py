#!/usr/bin/python3
# -*- coding:utf-8 -*-

import random
import string

# goal = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 10))
# print(goal)


import os
import time
import datetime

i = 'D:\\test\\1.txt'
file_time = os.path.getctime(i)
print(file_time)  # float
b = time.localtime(file_time)
print(b)  # time.struct_time





today = datetime.datetime.now()
offset = datetime.timedelta(days=-3)
re_date = (today + offset)
print(re_date)  # datetime
time_unix = time.mktime(re_date.timetuple())
print(time_unix) # unix

print(file_time - time_unix)