#! /usr/bin/python3
# -*-coding: utf-8 -*-

import _thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % ( threadName, time.ctime() ))

try:
    _thread.start_new_thread( print_time, ("Thread-1", 2,) )
    _thread.start_new_thread( print_time, ("Thread-2", 4,) )
except:
    print("Error: 无法启动线程")
while 1:
    pass
