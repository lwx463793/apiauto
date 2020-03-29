import unittest
from testcases.test_smoke import LoginTestCase
from common.constant import REPORT_DIR
from librarys.HTMLTestRunnerNew import HTMLTestRunner
import os
import time
from common.send_email import send_email



suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
#suite.addTests(loader.)
now = time.strftime("%Y-%m-%d_%H_%M_%S")
file =os.path.join(REPORT_DIR, now)
filename = ("{}.html".format(file))
with open(filename, "wb") as f:
    runner = HTMLTestRunner(
    stream=f, verbosity=2,
    title="测试报告", description="18期测试报告",
    tester="liumei")
    runner.run(suite)
send_email(filename)

# 创建一个测试集合
#suite = unittest.TestSuite()

# 添加测试用例
# 第一种 单个用例添加 ：接收的参数时测试用例对象
# suite.addTest(LoginTestCase('test_login'))
# suite.addTest(LoginTestCase('test_password_error'))
# suite.addTest(LoginTestCase('test_password_lt6'))

# 第二种：一次添加多条
# suite.addTests([LoginTestCase('test_login'),LoginTestCase('test_login'),LoginTestCase('test_login')])

# 第三种：一次添加一个测试用例类(类名不需要加引号)
# loader = unittest.TestLoader()
# # suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
#
# # 第四种：通过模块添加
# suite.addTest(loader.loadTestsFromModule(py18_13day_testcase))