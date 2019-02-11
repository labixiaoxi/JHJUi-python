# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/4 14:52
import os,time
from appium import webdriver
from publicPhone import PublicPhone
from publicLogs import  PublicLogs
from publicCmd import PublicCmd
from publicApk import PublicApk

log =PublicLogs()

def publicDrivers():
    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    capabilities={}
    capabilities['platformName']='Android'
    capabilities['platformDevice']=PublicPhone().system_version()[0]
    capabilities['deviceName']=PublicCmd().get_device_user()[0]
    capabilities['appPackage']=PublicApk().getAppInfo()[0]
    capabilities['appActivity']=PublicApk().getAppInfo()[1]
    capabilities['app']=PATH("..\\apk\\jhj_uat_v2.8.4.0.uat.build_20181212090930.apk")
    capabilities['unicodeKeyboard'] = True
    capabilities['resetKeyboard'] = True
    capabilities['noReset'] = True
    driver=webdriver.Remote('http://127.0.0.1:4727/wd/hub',capabilities)
    time.sleep(10)
    log.info(u"获取成功")
    return driver



