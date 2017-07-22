#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import multiprocessing


def music():
    for i in range(10):
        print u'正在听音乐 %s' % time.ctime()
        time.sleep(1)

def movie():
    for i in range(10):
        print u'正在看电影 %s' % time.ctime()
        time.sleep(1)


def main():
    processes = []
    t1 = multiprocessing.Process(target=music, args=())
    processes.append(t1)

    t2 = multiprocessing.Process(target=movie)
    processes.append(t2)

    for t in processes:
        t.start()

    for t in processes:
        t.join()

    print "All done"

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print u"一共执行了: %s 秒" % (end-start)