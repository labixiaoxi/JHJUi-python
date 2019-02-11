# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/4 16:43
import os,yaml
class PublicGetYaml:

    def __init__(self,path):
        self.path=path

    def get_Yaml(self):
        try:
            with open(self.path,'r') as f:
                data=f.read()
                result=yaml.load(data)
                f.close()
                return result
        except Exception:
            return u"未找到yaml文件"

    def result_yaml(self):
        data=self.get_Yaml()
        return data

    #操作长度
    def caselen(self,name):
        data=self.result_yaml()
        length=len(data[name])
        return length

    #元素
    def get_elementInfo(self,name,i):
        data = self.result_yaml()
        return data[name][i]['element_info']

    #类型
    def get_elementType(self,name,i):
        data = self.result_yaml()
        return data[name][i]['find_type']

    # 输入内容
    def get_elementSendKeys(self,name,i):
        data = self.result_yaml()
        return data[name][i]['send_keys']


    def get_elementIndex(self,name,i):
        data = self.result_yaml()
        return data[name][i]['index']


    def get_elementTitle(self,name,i):
        data = self.result_yaml()
        return  data[name][i]['title']

if __name__ == '__main__':
    getyaml=PublicGetYaml("../yaml_data/test_jhj_login/jhj_login.yaml")
    print getyaml.caselen('testcase')
