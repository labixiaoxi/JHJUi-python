# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/8 9:51
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.publicLogs import  PublicLogs
from selenium.webdriver.common.by import By

log = PublicLogs()
import time,os
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

 # # 重写元素定位方法
    def find_element(self,timeout,poll_frequency,type,loc):
        # return WebDriverWait(self.driver, timeout,poll_frequency).until(lambda x:x.find_element(type,loc))

        if type =='id':
            return WebDriverWait(self.driver, timeout,poll_frequency).until(lambda x:x.find_element(By.ID,loc))
        elif type =='name':
            return WebDriverWait(self.driver, timeout,poll_frequency).until(lambda x:x.find_element(By.NAME,loc))
        elif type =='class_name':
            return WebDriverWait(self.driver, timeout,poll_frequency).until(lambda x:x.find_element(By.CLASS_NAME,loc))



    # 重写定义send_keys方法
    def send_keys(self,timeout,poll_frequency,type,loc,value):
        try:
                return self.find_element(timeout,poll_frequency,type,loc).send_keys(value)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self,loc))

    # 重写定义click方法
    def click(self,timeout,poll_frequency,type,loc):
        return self.find_element(timeout,poll_frequency,type,loc).click()

 #    # 重写多元素定位方法
    def find_elements(self,timeout,poll_frequency,type,loc,index):
        elements=WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_elements(type,loc))
        return elements[index]


    # 重写定义send_keys方法
    def eles_send_keys(self,timeout,poll_frequency,type,loc,index,value):
        try:
                return self.find_elements(timeout,poll_frequency,type,loc,index).send_keys(value)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self,loc))

    #清除
    def eles_clear(self,timeout,poll_frequency,type,loc,index):
        try:
                return self.find_elements(timeout,poll_frequency,type,loc,index).clear()
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self,loc))









