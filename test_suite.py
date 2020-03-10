# 1.导包
import time
import unittest
from script.test_login import TestLogin

# 2.创建测试集合
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

# 3.添加测试用例
suite.addTest(unittest.makeSuite(TestLogin))

# 生成简易测试报告
# unittest.TextTestRunner().run(suite)

# 4.设置报告路径
report_path = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 5.打开文件
with open(report_path, "wb") as f:
    #     5.1 创建执行器
    runner = HTMLTestRunner(f, title="report", description="hahah")
    #     5.2 执行测试套件
    runner.run(suite)