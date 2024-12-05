st='abBcdefghifjka'
print(st[-1:-2:-1])
print(st[0:7:3])
print(repr(st.startswith('bca',1,5)))
print(repr(st.count('j')))
print(repr(st.upper().isupper()))
print(repr(st.replace('a','A',1)))
print('分割fa',st.split('fa',1))
print('分割f',st.split('f',1))
print(st.capitalize()) #第一个大写其他小写
print(st.lower())

#列表
print('\n列表\n')
list1=[1,2,3,4,5,6,7,8,9]
print(list1[0:5])
list1.append('10') 
print(list1.append('10') )
print('append',list1)
list1.extend([0,'0',11,12])
print('extend 列表',list1)
list1.extend({0,'0'})
print('extend 字典',list1)
list1.insert(20,'-1')
print('insert',list1)

print('\n增删改查列表',list1)
print('删除pop',type(list1.pop(-1)))
print(f'list1  {list1}')

list2=[-1,0,21,8,3,4,7,5,6,4,7,8,9]
list3=list2.copy()
print(f'list2  {list2}')
list2.sort()
print('排序sort 由小到大',list2)
print(f'list3  {list3}')
list3.reverse()
print('排序reverse',list3)
list3.sort(reverse=True) #倒序
#list3.sort()
#list3.reverse()
print('由大到小排序',list3)


print('\n循环列表')
li=[]
[print(i*5) for i in range(1,10)] #列表推导式
[li.append(i) for i in range(1,20) if i%2==0] #列表推导式 
print('偶数 li',li)
li.append([1,2,3])
print(li[len(li)-1][1])

print('\n字典\n')
dic={'name':'zhangsan','age':18,'sex':'男'}
print(dic['name'])
print(dic.get('name'))
print(dic.get('name1','不存在'))
del dic['name']
#dic.clear()
dic.pop('age')
print(dic)
dic.popitem()
print(dic)
dic1={'name':'zhangsan','age':18,'sex':'男'}
print('values',dic1.values())
print('keys',dic1.keys())
print('items ',dic1.items())
print('items ',type(dic1.items()))
print('items ',type((1,)))

print('\集合\n')  #无序的 哈希表 不能修改 唯一性(去重))
s1=set('abc')    #定义集合
print(s1)
s1.add(10)
print('add',s1)
s1.update([1,2,3])
print('update',s1)
# s1.remove('a')
print('remove',s1)
s1.pop()    #无序排列后 默认删除第一个集合
print('pop   ',s1)
s1.discard('a')
print('discard',s1)

print('\n交集 并集\n')

print('&交集 ',set('abc') & set('cbf')) #交集  & 返回集合
print('|并集 ',set('abc') | set('cbf')) #并集  & 返回集合

import os
os.system('cls')

print('类型转换')
print(int('-123'))
print(int(1.6))
print(float(+1))
print(str(1.001000))
print(str([1,2,3]))
print(eval('1+2'))
print(list({'k':'v','k1':'v1'}))  #字典转列表 只有key的值
print(list({'k','v','k','v1'}))  #先去重 再转换

os.system('cls')

import copy
p1=[1,2,3]
p3=p1
p2=p1.copy()
p4=copy.copy(p1)
p1.append(4)
print('p1  ',p1)
print('p2  ',p2)
print('p3  ',p3)
print('p1  ',id(p1))
print('p2  ',id(p2))
print('p3  ',id(p3))
print('p4  ',id(p4))

os.system('cls')

def fname():
    global ab  #函数运行后才执行,才有全局变量ab 
    ab = 10
    print('a = ',ab)
fname()

funa=lambda x,y:x+y
print(funa(1,2))
print('a>b') if 4>5 else print('a<b')
max = lambda x,y:x if x>y else y
cmp = lambda x,y: '大' if x>y else '小'
print('max ',max(3,2))
print('cmp比大小 ',cmp(1,2))

os.system('cls')

#内置函数
import builtins
#print(dir(builtins)) #查看内置函数

from functools import reduce
print(reduce(lambda x,y:x-y,[1,2,3,4,5]))

tua=(1,2,3,4,5)
a,b,c,*d= tua
print(a,b,c,d,sep=' ; ')

# 异常

#raise Exception('这是一个自定义 报错 ')

os.system('cls')


try:
    print('try')
except Exception as e:
    print('except',e)
finally:
    print('finally')
    
from functools import reduce as rd, partial as pt

print('__name__ = ',__name__)
if __name__ == '__main__':
    print('__name__==__main__','这是主程序')

#含有__init__.py的文件夹,可以作为一个包 导入时先执行
# 控制要导入的模块列表 __all__ = ['a','b']

os.system('cls')

class person:
    name='jake'
    _name='rose'  #私有属性
    __name1='jake1' #隐藏属性
    def __init__(arg): #构造函数
        print('__init__ 被调用')
    def run (self):
        print(f'run {self.name}')
        print(f'run {self.name} id {id(self.name)}')
    def __del__(self): #析构函数 被del或者对象全部被调用后执行
        print('析构函数被调用')
    def __str__(self): #打印对象时调用
        return'__str__ 被打印了'
    # def __new__ (self): #创建对象时调用  静态方法 没有传参数
    #     pass
    
p1=person()
p1.run()
print(p1.name,id(p1.name))
print('访问隐藏属性__name1',p1._person__name1) #可读写
print('p1._name ',p1._name)
print(p1)
del p1
print('person.name ',person.name,'id ',id(person.name))

# os.system('cls')
class father:
    def eat(self):
        print('father eat')
        print('father super() ',super())
class son(father):
    @staticmethod #静态方法  不访问类和对象的数据,节约内存 只能访问类属性
    def sleep():
        print('son sleep')
    @classmethod #类方法 访问私有属性 只能访问类属性
    def sing(cls):
        print('cls 类对象',cls )
    def eat(self):
        print('son ',repr(son))
        print('son self',repr(self))
        print('son eat')
        super().eat() #调用父类方法
        super(son,self).eat() #调用父类方法
son().eat()
son().sing()
son().sleep()

os.system('cls')

print(son.__mro__) #查看继承关系

# 单例对象
class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self):
        print('init')
        
print(Singleton())
print(Singleton())
print(Singleton())

#通过模块实现单例模式  只有一个对象
#应用场景 : 游戏 回收站 音乐 数据库配置

os.system('cls')
#魔法方法和属性
class exp:
    '''exp类中的___doc__属性信息'''
    pass
def exp1():
    '''exp1函数中的___doc__属性信息'''
    pass
print(exp.__doc__) #魔法属性 打印类中的多行注释信息
print(exp1.__doc__) #魔法属性 打印函数中的多行注释信息
print(exp1.__module__) #打印模块
print(exp.__class__) #打印模块类
print(exp1.__class__) #打印模块类

os.system('cls')
#文件
f=open('E:\it\py\myfile1.txt','r+')
print(f.name)
print(f.mode)
print(f.closed,end='\n')

# print(f.read(),end='\n')
# print(f.read(4),end='\n')
# print('\n',f.readline())
# print(f.read())

# print('\n',f.readlines())
print('w之前 ',f.read())

f.write('hello world  hahaha \r')
print(f.tell())
f.seek(0,0)
print('w之后 ',f.read())

f.close()
# print(f.closed)

os.system('cls')

with open('myfile.txt','w',encoding='utf-8') as f:
    # print(f.read())
    print(f.encoding)
    f.write('你好吗?❓？')
    print(f.tell())
    
os.system('cls')
#图片赋值
""" with open('E:\图片\【哲风壁纸】2024-11-19 09_50_52.png','rb') as f:
    img=f.read()
    # print(img)
with open('./图片.png','wb') as f:
    f.write(img)
    print(f) """

#目录
print(os.getcwd()) #获取当前目录
print(os.listdir('../')) #获取当前目录下的文件

os.system('cls')

#迭代器  __iter__对象返回了对象  __next__
from collections.abc import Iterable, Iterator
print(isinstance('123',Iterable))
print(isinstance('123',(tuple,str)))

li=[1,2,3]
li2=iter(li)
print(li2.__next__())
print(li2.__next__())
print(li2.__next__())
# print(li2.__next__()) #报错 迭代器取完元素会报错

li3=li.__iter__()
print(li3.__next__())
print(li3.__next__())
print(li3.__next__())

os.system('cls')

str='123'
print(isinstance(str,Iterable))
print(isinstance(str,Iterator))

print(isinstance(iter(str),Iterable))
print(isinstance(iter(str),Iterator))

li=[i*5 for i in range(5)]      #列表推导式
gen=(i*5 for i in range(5))     #生成器
print(li)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))