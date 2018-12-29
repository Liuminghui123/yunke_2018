import unittest,time,sys
from page_object.login_page import LoginPage
from model.myunit import Mytest
sys.path.append('./test_case')
sys.path.append('../model')
sys.path.append('../page_object')

class LoginTest(Mytest):
    '''登录测试'''
    def test_login_null(self):
        '''用户名，密码空'''
        po = LoginPage(self.driver)
        po.login_action('', '')
        time.sleep(1)
        self.assertEqual(po.alert_text(),'请输入手机号')


