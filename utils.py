# 通用断言方法
def common_assert(test_case,response,status_code=200,status=1,msg="登陆成功"):
    test_case.assertEqual(status_code, response.status_code)
    test_case.assertEqual(status, response.json().get("status"))
    test_case.assertIn(msg, response.json().get("msg"))
