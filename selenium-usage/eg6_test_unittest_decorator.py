#!/usr/bin/env python
# encoding:utf-8
import sys
import unittest
import selenium
__author__ = 'Samren'


def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))


class MyTestCase(unittest.TestCase):
    """
    装饰器：让你的测试用例更智能
    """
    @unittest.skip("skip this test case.")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(selenium.__version__[0] < 2,
                     "not supported in this library version")
    def test_format(self):
        u"""这个测试用例只在某些库特定版本下执行"""
        print "Tests that work for only selenium > 2.0."

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        u"""这个测试用例只在Windows环境下执行"""
        print "yes, it is win platform"

    @unittest.expectedFailure
    def test_fail(self):
        u"""如果成功了就是unexpected success"""
        self.assertEqual(1, 0, "broken")

    @skipUnlessHasattr('abc', '__doc__')
    def test_create_your_own_test_decorator(self):
        self.assertEqual("abc", 'abc')


@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    """
    这个测试类不会被执行
    使用场景：当某些预备资源不满足条件时，跳过整个测试类
    """
    def test_not_run(self):
        print "you never see this test case"
        self.assertTrue(True)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(MyTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(MySkippedTestCase))
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not res.wasSuccessful())