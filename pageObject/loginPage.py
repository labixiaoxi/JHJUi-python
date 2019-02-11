# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/8 10:03
from basePage import BasePage
from selenium.webdriver.common.by import By
from public.publicGetYaml import PublicGetYaml
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
log = PublicLogs()
class LoginPage(BasePage):
    def login(self,name):
        path = '../yaml_data/test_jhj_login/jhj_login.yaml'
        # self.click(10,0.5,PublicGetYaml(path).get_elementType(name,0),PublicGetYaml(path).get_elementInfo(name,0))
        # log.info(u"操作步骤:-------->%s"%PublicGetYaml(path).get_elementTitle(name,0))
        self.eles_clear(10,0.5,PublicGetYaml(path).get_elementType(name,1),
                                    PublicGetYaml(path).get_elementInfo(name,1),
                                    int(PublicGetYaml(path).get_elementIndex(name,1)))

        self.eles_send_keys(10,0.5,PublicGetYaml(path).get_elementType(name,1),
                                    PublicGetYaml(path).get_elementInfo(name,1),
                                    int(PublicGetYaml(path).get_elementIndex(name,1)),
                                    str(PublicGetYaml(path).get_elementSendKeys(name,1)))
        log.info(u"操作步骤:-------->%s:%s"%(PublicGetYaml(path).get_elementTitle(name,1),PublicGetYaml(path).get_elementSendKeys(name,1)))
        self.eles_clear(10,0.5,PublicGetYaml(path).get_elementType(name,2),
                                    PublicGetYaml(path).get_elementInfo(name,2),
                                    int(PublicGetYaml(path).get_elementIndex(name,2)))
        self.eles_send_keys(10,0.5,PublicGetYaml(path).get_elementType(name,2),
                                    PublicGetYaml(path).get_elementInfo(name,2),
                                    int(PublicGetYaml(path).get_elementIndex(name,2)),
                                    str(PublicGetYaml(path).get_elementSendKeys(name,2)))
        log.info(u"操作步骤:-------->%s:%s"%(PublicGetYaml(path).get_elementTitle(name,2),PublicGetYaml(path).get_elementSendKeys(name,2)))
        self.click(10,0.5,PublicGetYaml(path).get_elementType(name,3),PublicGetYaml(path).get_elementInfo(name,3))
        log.info(u"操作步骤:-------->%s"%PublicGetYaml(path).get_elementTitle(name,3))

    def loginAssertFail(self):
        """
        登录失败的断言
        :return:
        """
        return self.find_element(10,0.5,By.ID,'com.platform.jhj:id/code_login_tv').text

    def loginAssertPass(self):
        """
        登录成功的断言
        :return:
        """
        return self.find_element(10,0.5,By.ID,'com.platform.jhj:id/action_my').text












