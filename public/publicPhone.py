# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/3 16:23
import os
from publicLogs import PublicLogs
from publicCmd import PublicCmd

log=PublicLogs()
class PublicPhone(object):


    def system_version(self):
        '''
        手机系统版本
        :return:
        '''
        return_version=os.popen("adb shell getprop ro.build.version.release").readlines() #设备
        return_model=os.popen("adb shell getprop ro.product.model").readlines()           #型号
        return_brand=os.popen("adb shell getprop ro.product.brand").readlines()           #品牌
        return_device=os.popen("adb shell getprop ro.product.device").readlines()         #设备名
        try:
            version = return_version[0].split('\r')[0]
            model = return_model[0].split('\r')[0]
            brand = return_brand[0].split('\r')[0]
            device = return_device[0].split('\r')[0]
            log.info(u"设备:%s , 型号:%s, 品牌:%s, 设备名:%s"%(version,model,brand,device))
            return version,model,brand,device

        except:
            log.info("设备连接异常或设备连接多个")



    def system_phone_pix(self):
        """
        获取分辨率
        :return:

        """
        pix = os.popen("adb shell wm size")
        result= pix.readline().split("Physical size: ")[1]
        log.info("手机分辨率:"+result)
        return result



if __name__ == '__main__':
    phone = PublicPhone()
    print phone.system_version()
    print phone.system_phone_pix()