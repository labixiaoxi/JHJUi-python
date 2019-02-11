##环境: window

python 2.7.12

##目录: 

--apk		    apk
 
--config        存放公共数据

--logs          存放日志

--pageObject    po分层

	--basePage  对keys和click方法重写定义

	--homePage  业务操作组合,断言结果

	--loginPage 业务操作组合,断言结果

--public        公共方法

	--publicApk     获取包名,类名,版本号,版本名称等

	--publicCmd		获取设备id,可用端口,生成启动命令
      
	--publicDriver  驱动,所有参数从设备和apk获取

	--publicGetYaml 读取yaml文件

	--publicLogs    日志

	--publicOperate 操作封装,返回键,屏幕大小,滑动方向等

	--publicPhone   获取手机信息

	--publicSeriver 执行启动命令

--report			测试报告

--testCase          测试用例
	--loginCase		调取po分层,组合业务场景,调取已经写好的断言

--util				工具
	--aapt.exe		aapt获取类名和包名

--yaml_data			数据管理,包含(元素,类型,输入内容,操作内容,索引等)

--run_case          批量执行测试用例