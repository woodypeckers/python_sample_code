#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def music():
    for i in range(10):
        print u'正在听音乐 %s' % time.ctime()
        time.sleep(1)

def movie():
    for i in range(10):
        print u'正在看电影 %s' % time.ctime()
        time.sleep(1)

def main():
    music()
    movie()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print u"一共执行了: %s 秒" % (end-start)