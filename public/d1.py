# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/7 15:03
from public.publicLogs import PublicLogs
from public.publicGetYaml import PublicGetYaml
from public.publicOperate import PublicOperate
from public.d import GetVariable as common
log  =PublicLogs()
class PageOperate(object):
    def __init__(self,path,driver):
        self.yaml = PublicGetYaml(path)
        self.driver = driver
        self.operate= PublicOperate(self.driver)


# get_introduce

    def get_caselen(self,name):
        for i in range(self.yaml.caselen(name)):
            self.getCaseEle = self.yaml.get_elementinfo(name,i)
            self.getCaseFindType = self.yaml.get_findtype(name,i)
            self.getCaseInfo = self.yaml.get_introduce(name,i)
            self.getCaseOperateType=self.yaml.get_operate_type(name,i)
            self.getCaseEle1 = self.yaml.get_elementinfo1(name,i)
            self.getCaseFindType1 = self.yaml.get_findtype1(name,i)
            self.getCaseSend  = self.yaml.get_send_content(name,i)
            self.getCaseIndex  = self.yaml.get_index(name,i)
            print "%s"%common.find_element_by_id




if __name__ == '__main__':

    page = PageOperate("../yaml_data/test_jhj_login/jhj_login.yaml","driver")
    page.get_caselen('testcase')