# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/3 16:20
import  os
from publicLogs import PublicLogs
log=PublicLogs()
class PublicCmd:

    def command(self,command):
        '''

        :param command: 命令
        :return:命令返回结果
        '''
        result_list=[]
        result=os.popen(command).readlines()
        for i in result:
            if i=='\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    def execute_cmd_no(self,command):
        os.system(command)

    def is_post_user(self,post):
        '''
        :param post: 端口号
        :return:端口判断
        '''
        posts=str(post)
        result="netstat -ano |findstr "+posts
        command_result=self.command(result)
        flag=None
        if len(command_result)>0:
            # print "端口占用",posts
            flag=True

        else:
            # print "端口可用",posts
            flag=False
        return flag


    def generat_post_list(self,post,device_num):
        '''

        :param post: 端口
        :param device_num: 端口数量
        :return:生成多个未占用端口
        '''
        post_list=[]
        while len(post_list)!=device_num:
            if self.is_post_user(post)==False:
                post_list.append(post)
            post=post+1
        return post_list

    def get_device_user(self):
        '''
        :return:获取设备id
        '''
        result_list=[]
        result=self.command("adb devices")
        for i in result:
            if "List" in i:
                continue
            device_into=i.split('\t')
            try:
                if device_into[1]=='device':
                    result_list.append(device_into[0])
            except:
                log.error(u"手机设备获取有异常")
        log.info("手机设备id为:"+str(result_list))
        return result_list

    def  device_post_list(self,post):
        '''
        :param post: 端口
        :return:根据adb devices获取的设备数量生成对应可用的端口数量
        '''
        device_num=len(self.get_device_user())
        post_list=self.generat_post_list(post,device_num)
        log.info("生成的可用端口:"+str(post_list))
        return post_list

    def server_command(self):
        '''
        :return:生成启动命令(appium - p 4723 - bp 4726 - U e643cf1 - -no - reset - -session - override)
        '''
        command_list=[]
        p=self.device_post_list(4727)
        bp=self.device_post_list(2000)
        user=self.get_device_user()
        #有多少个设备就生成多少条启动命令
        for i in range(len(user)):
            command="appium -a 127.0.0.1 -p "+str(p[i])+" -bp "+str(bp[i])+" --chromedriver-port 9519"+  " -U "+str(user[i])+" --session-override"
            command_list.append(command)
        log.info(command_list)
        return self.execute_cmd_no(command_list[0])

if __name__ =='__main__':
    c=PublicCmd()
    print c.server_command()