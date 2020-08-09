#inheritance

class parent():
    def __init__(self):
        print('init from parent')

    def hello1(self):
        print('Hello from parent')


class child1(parent):
    def __init__(self):
        super().__init__()
        print('init from child1')

    def hello(self):
        print('hjello form child1')

obj = child1()
obj.hello()
obj.hello1()

import datetime
cur_time = datetime.datetime.now()
print(cur_time)

class Circle():
    def __init__(self,r):
        self.r = r

    def area(self):
        area = self.r**2*3.14
        print('area',area)
        return area

obj = Circle(2)
obj.area()

class sample():
    def __init__(self):
        self.data = ''

    def instr(self):
        self.data = input('enter str:')

    def prntstr(self):
        print(self.data.upper())

obj = sample()
obj.instr()
obj.prntstr()

num = 27
if num > 0:
    for i in range(2,num+1):
        if num%i == 0:
            print('not prime')
            break
        else:
            print('prime', num)
else:
    print('not prime')

def multipliers():
  return [lambda x : i * x for i in range(4)]

print ([m(2) for m in multipliers()])

n = 12345
rev =0
while n > 0:
    dig = n%10
    rev = rev*10+dig
    n=n//10

print('rev',rev)


class class1():
    def add(self,a):
        sum = a+2
        print('sum in class1', sum)
        return sum

class class2(class1):
    def add(self, ar1):
        sum = ar1+3
        print('sume in class2', sum)
        return sum

obj = class2
print(obj.add(2,12))

obj2=class1
print(obj2.add(1,2))


class enc():
    maxspeed = 12

    def __init__(self):
        pass
    def speed(self):
        self.maxspeed = 13
        print('maxspeed',self.maxspeed)
        print('speed')
    def __encspeed(self):
        print('enc speed',self.maxspeed)

obj = enc()
obj.speed()
obj.__encspeed()

