
import os
print(os.name)  #获取操作系统类型
print(os.getenv('PATH')) #获取环境变量

o=os.path.split('E:\python\python-learn\内置模块.py')   #目录名和文件名分离
print(o)   # 输出: ('E:\\python\\python-learn', '内置模块.py')

print(os.path.dirname(r'E:\python\python-learn\内置模块.py')) #获取目录名
print(os.path.basename(r'E:\python\python-learn\内置模块.py')) #获取文件名

print(os.path.exists('E:\it\py\内置模块.py')) #判断文件是否存在
print(os.path.isfile('E:\it\py\内置模块.py')) 
print(os.path.isdir('E:\it\py')) 

print(os.path.abspath('内置模块.py')) #获取绝对路径
print(os.path.isabs('E:\python\python-learn\内置模块.py')) 

os.system('cls')

import sys #跟解释器交互
print(sys.getdefaultencoding()) #获取默认编码
print(sys.path)  #获取模块搜索路径
print(sys.platform) #获取操作系统平台
print(sys.version) #获取python解释器版本信息操作系统平台

os.system('cls')
import time
print(time.time()) #获取当前时间戳
print(time.localtime()) #获取当前时间，返回struct_time格式 时间元组
print(time.asctime())
print(time.ctime())   
print(time.strftime('%Y-%m-%D %H:%M:%S'))   #将struct_time格式化成字符串
print(time.strptime('2020-10-10 10:10:10','%Y-%m-%d %H:%M:%S')) #将字符串格式化成struct_time


#日志模块 logging
import logging
logging.basicConfig(filename='log.log',filemode='w+',level=logging.NOTSET,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
logging.critical('critical message')
logging.warning('warning message')
logging.warning('warning message')
logging.debug('debug message') 


import random
print(random.random()) #随机整数
print(random.randrange(1,5)) #随机整数

# import requests as req
# print(req.get('https://www.baidu.com').text)