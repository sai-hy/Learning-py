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
    
p1=person()
p1.run()
print(p1.name,id(p1.name))
print('访问隐藏属性__name1',p1._person__name1) #可读写
print('p1._name ',p1._name)
print(p1)
del p1
print('person.name ',person.name,'id ',id(person.name))

os.system('cls')
class father:
    def eat(self):
        print('father eat')
        print('father super() ',super())
class son(father):
    @staticmethod #静态方法  不访问类和对象的数据,节约内存
    def sleep():
        pass
    @classmethod #类方法 访问私有属性
    def sing(cls):
        print('cls 类对象','cls ')
    def eat(self):
        print('son ',repr(son))
        print('son self',repr(self))
        print('son eat')
        super().eat() #调用父类方法
        super(son,self).eat() #调用父类方法
son().eat()
son().sing()

os.system('cls')

print(son.__mro__) #查看继承关系

