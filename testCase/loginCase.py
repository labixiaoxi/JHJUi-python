# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/8 10:12
import unittest,time,HTMLTestRunner
from pageObject.loginPage import LoginPage
from pageObject.homePage import HomePage

from public.publicServer import AppiumServer
from public.publicDriver import publicDrivers
class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # AppiumServer().start_server()
        # time.sleep(30)
        cls.driver = publicDrivers()
    def setUp(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def testLogin1(self):
        """登录,密码错误"""
        self.home_page.homeMe('testhome')
        self.login_page.login('testLogin1')
        self.assertEqual(u'验证码登录',self.login_page.loginAssertFail(),msg=u"断言失败")

    def testLogin2(self):
        """登录,账号错误"""
        self.login_page.login('testLogin2')
        self.assertEqual(u'验证码登录',self.login_page.loginAssertFail(),msg=u"断言失败")


    def testLogin3(self):
        """登录,账号密码正确"""
        self.login_page.login('testLogin3')
        self.assertEqual(u'我的',self.login_page.loginAssertPass(),msg=u"断言失败")


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(LoginCase('testLogin1'))
    # suite.addTest(LoginCase('testLogin2'))
    # suite.addTest(LoginCase('testLogin3'))
    html_file = '../report/result.html'
    fp = file(html_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="吴洪彬_测试报告",
        description="金惠家ui自动化"
    )
    runner.run(suite)
    fp.close()


