from threading import Thread , Lock
import time
""" 
li=[]
def wri():    # 定义一个函数
    for i in range(5):
        li.append(i)
        time.sleep(1)
    print("写 li: ",li)
    
def red():
    print("读 li: ",li)

if __name__  == '__main__':
    # 创建线程
    t1=Thread(target=wri)
    t2=Thread(target=red)
    t1.start()
    t1.join()   # 等待t1执行完
    t2.start() """
    

#互斥锁
'''
look = Lock()
a=0
b=1000000
def add():
    global a
    look.acquire()
    for i in range(b):
        a+=1
    look.release()
    print("add中的 a=",a)
def add1():
    global a
    look.acquire()
    for i in range(b):
        a+=1
    look.release()
    print("add1中的 a=",a)
if __name__ == '__main__':
    t1=Thread(target=add)  # 创建线程
    t2=Thread(target=add1)  # 创建线程
    t1.start()                 # 启动线程
    t2.start()
'''

#进程
from multiprocessing import Process
import os
def sing(n):
    print(f"{n} sing")
    print(f"ospid {os.getpid()}")
    print(f"osppid {os.getppid()}")
    
def song(n):
    print(f"{n} song")
    print(f"ospid {os.getpid()}")
    print(f"osppid {os.getppid()}")
    
    
if __name__ == '__main__':
    p1=Process(target=sing,args=('jake',))  # 创建进程
    p2=Process(target=song,args=('rose',))   # 创建进程
    p1.start()
    p2.start()
    print('p1 pid ',p1.pid)
    print('p1 name ',p1.name)
    print('p2 pid ',p2.pid)
    print('p2 name ',p2.name)
    p1.join()
    print(f'p1状态 {p1.is_alive()}')
    print(f'p2状态 {p2.is_alive()}')