# 导包
import requests

# 创建接口封装类
class LoginApi:
    def __init__(self):
        self.url_verify = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.url_login  = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 创建接口调用方法
    # 获取验证码
    def get_login_verify_code(self,session):
        response = session.get(self.url_verify)
        return response

    # 发送登录请求
    def login(self,session,user,pwd,code):
        login_data={
            "username": user,
            "password": pwd,
            "verify_code": code
        }
        response = session.post(self.url_login,data=login_data)
        return response