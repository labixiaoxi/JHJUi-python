# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/4 15:21


import os,time
from publicLogs import PublicLogs
log=PublicLogs()

class PublicOperate:
    def __init__(self,driver):
        self.driver=driver

    def get_back(self):
        '''
        :return:返回键
        '''
        os.popen('adb shell input keyevent 4')

    def get_window_size(self):
        '''
        :return:返回屏幕的大小
        '''
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return(x,y)
    def swipe_up(self):
        '''
        :return:向上滑动
        '''
        try:
            l=self.get_window_size()
            x1=int(l[0]*0.5)
            y1=int(l[0]*0.8)
            y2=int(l[1]*0.2)
            self.driver.swipe(x1,y1,x1,y2,1000)
        except:
            log.error(u"上滑动异常")

    def swipe_down(self):
        '''
        :return:向下滑动
        '''
        try:
            l=self.get_window_size()
            x1=int(l[0]*0.5)
            y1=int(l[0]*0.2)
            y2=int(l[1]*0.8)
            self.driver.swipe(x1,y1,x1,y2,1000)
        except:
            log.error(u"下滑动异常")

    def swipe_right(self):
        '''
        :return:向右滑动
        '''
        try:
            l=self.get_window_size()
            x1=int(l[0]*0.2)
            x2=int(l[0]*0.8)
            y1=int(l[1]*0.5)
            self.driver.swipe(x1,y1,x2,y1,1000)
        except:
            log.error(u"右滑动异常")

    def swipe_left(self):
        '''
        :return:向左滑动
        '''
        try:
            l=self.get_window_size()
            x1=int(l[0]*0.8)
            x2=int(l[0]*0.2)
            y1=int(l[1]*0.5)
            self.driver.swipe(x1,y1,x2,y1,1000)
        except:
            log.error(u"左滑动异常")

    def screenshot(self):
        '''
        :return:截图
        '''
        nowtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        path='../img/'
        self.driver.get_screenshot_as_file(path+nowtime+'.png')

    def get_id(self,id):
        try:
            return self.driver.find_element_by_id(id)
        except:
            log.error("未定位到该元素:"+id)

    def get_name(self,name):
        try:
            return self.driver.find_element_by_name(name)
        except:
            log.error("未定位到该元素:"+name)

    def get_class_name(self,class_name):
        try:
            return self.driver.find_element_by_class_name(class_name)
        except:
            log.error("未定位到该元素:"+class_name)


    def get_classname_ids(self,classname,ids):
        try:
            ele=self.driver.find_element_by_class_name(classname)
            elements=ele.find_elements_by_id(ids)
            return elements
        except:
            log.error("未定位到该元素:"+ids)

    def get_classname_names(self,classname,names):
        try:
            ele=self.driver.find_element_by_class_name(classname)
            elements=ele.find_elements_by_name(names)
            return elements
        except:
            log.error("未定位到该元素:"+names)

    def get_classname_classnames(self,classname,classnames):
        try:
            ele=self.driver.find_element_by_class_name(classname)
            elements=ele.find_elements_by_class_name(classnames)
            return elements
        except:
            log.error("未定位到该元素:"+classnames)



    def get_id_names(self,id,names):
        try:
            ele=self.driver.find_element_by_id(id)
            elements=ele.find_elements_by_name(names)
            return elements
        except:
            log.error("未定位到该元素:"+names)

    def get_id_classnames(self,id,classnames):
        try:
            ele=self.driver.find_element_by_id(id)
            elements=ele.find_elements_by_class_name(classnames)
            return elements
        except:
            log.error("未定位到该元素:"+classnames)

    def get_id_ids(self,id,ids):
        try:
            ele=self.driver.find_element_by_id(id)
            elements=ele.find_elements_by_id(ids)
            return elements
        except:
            log.error("未定位到该元素:"+ids)

    def get_name_ids(self,name,ids):
        try:
            ele=self.driver.find_element_by_name(name)
            elements=ele.find_elements_by_id(ids)
            return elements
        except:
            log.error("未定位到该元素:"+ids)

    def get_name_names(self,name,names):
        try:
            ele=self.driver.find_element_by_name(name)
            elements=ele.find_elements_by_name(names)
            return elements
        except:
            log.error("未定位到该元素:"+names)

    def get_name_classnames(self,name,classnames):
        try:
            ele=self.driver.find_element_by_name(name)
            elements=ele.find_elements_by_class_name(classnames)
            return elements
        except:
            log.error("未定位到该元素:"+classnames)









