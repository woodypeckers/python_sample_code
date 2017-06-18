import unittest


class TestSample(unittest.TestCase):
    def test_simple(self):
        "test开头的才是测试用例"
        self.assertEqual(1, 1)
        self.assertEqual(1, 1)
        
        #否则只是一个普通的实例函数
    def tesxxx(self):
        self.assertEqual(2, 2)
        
        
        
if __name__ == "__main__":
    unittest.main()