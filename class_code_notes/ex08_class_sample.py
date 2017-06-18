#encoding:utf-8


def sum():
    print "hello"
    
# object

#类的数据和方法。
#对象的属性和函数。
#类的实例方法都必须第一个参数是self


class Animal(object):  #传入的参数
    
    def __init__(self, name, age):  #实例方法, self是对象的本身。cls 指类的本身
        #__init__ 是初始化函数，不是构造函数
        self.name = name
        self.age = age
        #self.name 是对象的属性
        print "__init__", self.name  #__init__() 函数是初始化函数
        print "age is", self.age
        
    def eat(self):
        print self.name, "is eating"
        
        
a1 = Animal("monkey1", 13)  
a2 = Animal("monkey2", 15)

a1.eat()
a2.eat()