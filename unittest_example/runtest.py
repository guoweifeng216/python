#coding=utf-8

import unittest
# 加载测试文件
import testadd
import testsub

# 构造测试集
# suite = unittest.TestSuite()
#
# suite.addTest(testadd.TestAdd("test_add"))
# suite.addTest(testadd.TestAdd("test_add2"))
#
# suite.addTest(testsub.TestSub("test_sub"))
# suite.addTest(testsub.TestSub("test_sub2"))

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
if __name__ == '__main__':
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(discover)
