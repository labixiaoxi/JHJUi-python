# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/8 10:03
from basePage import BasePage
from selenium.webdriver.common.by import By
from public.publicGetYaml import PublicGetYaml
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
log = PublicLogs()
class HomePage(BasePage):
    def homeMe(self,name):
        path = '../yaml_data/test_jhj_home/jhj_home.yaml'
        self.click(10,0.5,PublicGetYaml(path).get_elementType(name,0),PublicGetYaml(path).get_elementInfo(name,0))
        log.info(u"操作步骤:-------->%s"%PublicGetYaml(path).get_elementTitle(name,0))














