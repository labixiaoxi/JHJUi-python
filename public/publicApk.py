# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/3 17:05
import os,re,yaml
from publicLogs import PublicLogs
log=PublicLogs()
class PublicApk(object):

    def pathYaml(self):
        with open('../yaml_data/util/path.yaml','r') as f:
            result=f.read()
            path=yaml.load(result)
            return path

    def getAppInfo(self):
        path=os.path.abspath(os.path.dirname(__file__))+"\\"
        aapt_path=path+self.pathYaml()['path']['aapt']
        apk_path=path+self.pathYaml()['path']['apk']
        get_info_command = "%s dump badging %s" % (aapt_path,apk_path)
        log.info(u"获取包名和类名的命令:"+get_info_command)
        output = os.popen(get_info_command).read()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'[\s\S]*launchable-activity: name='(\S+)'").match(output) #通过正则匹配，获取包名，版本号，版本名称
        if not match:
            raise Exception(u"命令错误,获取失败")
        packagename = match.group(1)
        activityName = match.group(4)
        versionCode = match.group(3)
        versionName = match.group(2)
        log.info( u" 包名：%s ,类名：%s 版本号：%s , 版本名称：%s " % (packagename, activityName,versionCode, versionName))
        return packagename,activityName


if __name__ == '__main__':
    apk=PublicApk()
    print apk.getAppInfo()
