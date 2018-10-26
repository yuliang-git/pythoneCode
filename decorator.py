#!/usr/bin/evn python
# -*- coding:utf-8 -*- 
# study time:2018/10/24
import time


def timer(func):  # timer(test1)   func=test1
    def doce(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("the func run time %s" % (stop_time - start_time))
    return doce


@timer  # test1 = doce
def test1():
    time.sleep(1)
    print("in the bar")


@timer
def test2(name, age):
    print("test2:", name, age)


test1()
test2("sss", 22)

