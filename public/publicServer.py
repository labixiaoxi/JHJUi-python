# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/4 14:38
import platform
from publicCmd import PublicCmd
from publicLogs import PublicLogs
# from publicDriver import
log = PublicLogs
class AppiumServer:
    def __init__(self):
        self.server = PublicCmd()


    def start_server(self):
        if platform.system() == 'Windows':
            print (u"----------start_appium---------------------------")
            self.server.server_command()
            # android_driver()
            print (u"-----------启动成功-------------------------------")

if __name__ == '__main__':
    appium = AppiumServer()
    appium.start_server()