# 导包
import json
import logging
import unittest
import app
import requests

import utils
from api.login import LoginApi

from parameterized import parameterized
from tools.db_util_tpshop import DBUtilTpshop


# 构造测试方法,读取json文件
def build_data():
    test_data = []
    with open(app.BASE_DIR + "/data/login.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        for data in json_data:
            mobile = data.get("mobile")
            password = data.get("password")
            verify_code = data.get("verify_code")
            status_code = data.get("status_code")
            status = data.get("status")
            msg = data.get("msg")
            test_data.append((mobile,password,verify_code,status_code,status,msg ))
        logging.info("test_data={}".format(test_data))
    return test_data

# 创建测试类
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()

    def setUp(self):
        self.session = requests.session()

    def tearDown(self):
        self.session.close()

    # 创建测试方法
    # 只需要传递json读取文件方法名
    @parameterized.expand(build_data)
    def test00_login(self,mobile,password,verify_code,status_code,status,msg):
        """登录"""
        response = self.login_api.get_login_verify_code(self.session)
        self.assertEqual(200, response.status_code)

        # 登录及断言
        response = self.login_api.login(self.session,mobile,password, verify_code)
        json_data = response.json()
        logging.info(json_data)
        utils.common_assert(self,response,status_code,status,msg)
        # 查询数据库数据
        result = DBUtilTpshop.exe_sql("select user_id,mobile,nickname from tp_users where mobile='13488888888'")
        # result = DBUtilTpshop.exe_sql("select t.user_id,t.mobile,t.nickname from tp_users as t where mobile='13488888888'")
        logging.info(result)

    # 登录成功
    # @unittest.skip
    def test01_login_success(self):
        """登录成功"""
        # 获取验证及断言
        response = self.login_api.get_login_verify_code(self.session)
        self.assertEqual(200, response.status_code)

        # 登录及断言
        response = self.login_api.login(self.session,"13488888888","123456", "8888")
        json_data = response.json()
        print(json_data)
        logging.info(json_data)
        utils.common_assert(self,response,200,1,"登陆成功")
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(1, json_data.get("status"))
        # self.assertIn("登陆成功", json_data.get("msg")

    # 账号不存在
    @unittest.skip
    def test02_user_isnot_exist(self):
        """账号不存在"""
        # 获取验证及断言
        response = self.login_api.get_login_verify_code(self.session)
        self.assertEqual(200, response.status_code)

        # 登录及断言
        response = self.login_api.login(self.session, "13488888899", "123456", "8888")
        json_data = response.json()
        # print(json_data)
        logging.info(json_data)
        utils.common_assert(self, response, 200, -1, "账号不存在")
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(-1, json_data.get("status"))
        # self.assertIn("账号不存在", json_data.get("msg"))

    # 密码错误
    @unittest.skip
    def test03_password_error(self):
        """密码错误"""
        # 获取验证及断言
        response = self.login_api.get_login_verify_code(self.session)
        self.assertEqual(200, response.status_code)

        # 登录及断言
        response = self.login_api.login(self.session, "13488888888", "error", "8888")
        json_data = response.json()
        # print(json_data)
        logging.info(json_data)
        utils.common_assert(self, response, 200, -2, "密码错误")
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(-2, json_data.get("status"))
        # self.assertIn("密码错误", json_data.get("msg"))