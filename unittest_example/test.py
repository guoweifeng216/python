#coding=utf-8
from calculator import Count
import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")


class TestAdd(MyTest):
    """test suite"""
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)


class TestSub(MyTest):

    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)


if __name__ == '__main__':
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(TestAdd("test_add"))
    # suite.addTest(TestAdd("test_add2"))
    # suite.addTest(TestSub("test_sub"))
    # suite.addTest(TestSub("test_sub2"))
    #
    # #运行测试集合
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()
