import re

def smallest3(alist):
    smallest=10000
    smallestPos=0
    for pos,value in enumerate(alist):
        if(value<smallest):
            smallest=value
            smallestPos=pos
    return smallest,smallestPos

print(smallest3([1,4,-2,8]))

#######

def sum(x,y):
    return x+y


def mul(x,y):
    return x*y


def test(f,x,y):
    return f(x,y)


x=test(mul,2,3)
#print(x)


def operator(op):
    if op == "plus":
        return sum
    else:
        return mul

f=operator("plus")
print(f(1,2))


print(test(lambda x,y:x+y,1,8))


def ff():
    return lambda x:x*2
print("dsds")
print(ff()(4))
##issues
##

###List processing
def doubleList(alist):
    res=[]
    for x in alist:
        res=res+[2*x]
    return res

print(doubleList([2,4,9,1]))

def doubleList2(alist):
    return [2*x for x in alist]
print(doubleList2([2,4,9,1]))

def mymap(proc, alist):
    return [proc(x) for x in alist]

print(mymap(lambda x: x*2,[2,3,4,5]))
print("gapp")
print(mymap(lambda x: x>2,[2,3,4,5]))

print(list(map(lambda y: 2*y,[3, 4, 5])))

#Filter
def filt(function, alist):
    result=[]
    for x in alist:
        if function(x):
            result.append(x)
    return result

print(filt(lambda x: x>2, [1,2,3,4,3,]))

def filt2(function, alist):
    return [x for x in alist if function(x)]

print(filt2(lambda x:x>2,[1,2,3,4,4]))

## classes
class BankAccount(object):
    def __init__(self,name, pwd):
        self._balance=0
        self._owner=name
        self._pwd=pwd

    def _authenticate(self, pwd):
        return self._pwd==pwd

    def add(self,amount, pwd):
        if self._authenticate(pwd):
            self._balance += amount
        else:
            print("Transaction failed")

    def display(self):
        print(self._owner,self._balance)

b = BankAccount("satyam",22019)
b.add(20,2000)
b.add(23,22019)
b.display()

#####
#### Operator overloading
from math import *
class Point():
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def __str__(self):
        return "(%i,%i)"%(self._x,self._y)

    def __add__(self, anotherPoint):
        return Point(self._x + anotherPoint._x, self._y + anotherPoint._y)

    def normalize(self):
        factor = sqrt(self._x*self._x+self._y*self._y)
        self._x = self._x/factor
        self._y=self._y/factor



#c=Point(2,4)
#d=Point(3,6)
#e=c+d
#print(e)

def boo(point):
    point._x=100

c=Point(1.0,2.0)
boo(c)
print(c)
##classes


##regular expression

import re
data = "hello world welcome here"
p = re.compile('[a-z]+')
match = p.match(data)
print(match.start(),match.end())