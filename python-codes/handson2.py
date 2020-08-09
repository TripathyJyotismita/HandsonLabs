class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        print(dict(zip(self.ingredients, self.toppings)))


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

#output: {'vanilla': 'chocolate sauce'}

def group_by_owners(files):
    dct = {}
    if isinstance(files, dict):
        for k, v in files.items():
            print(k,v)
            if v not in dct:
                dct[v] = [k]
            else:
                dct[v].append(k)

    print(dct)
    lst = {v: [k] for k,v in files.items() if isinstance(files,dict)}
    print(lst)
if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy',
    }
    print(group_by_owners(files))

#Output: {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}

#1. Find common elements in sorted arrays 
ar1=[15, 5, 10, 20, 40, 80, 120]
ar2=[6, 7, 20, 80,120, 100]
ar3=[3, 4, 15, 20, 30, 70, 80, 120]

abc = [x for x in ar1 if x in ar2 if x in ar3]
print(abc)

#Merge two sorted arrays with O(1) extra space

abc = [' ' + str(x) for x in ar1 for y in ar2]
print(abc)
import random
x=random.randint(0, 17)
print('x',x)
print(dir(random))
y= random.randrange(11,14,1)
print(y)


#What do you mean by *args and **kwargs?
'''
In cases when we don’t know how many arguments will be passed to a function, like when we want to pass a list or a tuple of values, we use *args.
'''
def fun(*args):
    print(args[1])

def fun1(**kwargs):
    print(kwargs)

fun(['1','4','10'], ['11','41','11'], ('121','141','11'))
fun1(a=1,b=2,c=7)

#What is the iterator protocol?
'''
The iterator protocol for Python declares that we must make use of two functions to build an iterator- iter() and next().

iter()- To create an iterator
next()- To iterate to the next element
__next__ is a wrapper descriptor which in turn makes a call to next(). So why not skip the work and do just that instead?
'''
a=iter([2,4,6,8,10])
print('next',a.__next__())
print('next',next(a))

tup = (1,2,3)
a,b,c=tup
print('b',b)

#What is a frozen set in Python?
'''
First, let’s discuss what a set is. A set is a collection of items, where there cannot be any duplicates. A set is also unordered.
However, a set is mutable. A frozen set is immutable. This means we cannot change its values. This also makes it eligible to be used as a key for a dictionary.

>>> myset=frozenset([1,3,2,2])
>>> myset
frozenset({1, 2, 3})

>>> type(myset)
<class ‘frozenset’>
'''
'''
Read random line in a file
'''
import random
lines= open('Tasks-Devops.txt').readlines()
print('lines:',random.choice(lines))

l=[9,19,12,11,12,23,1]
print([x for x in l if x>44])

z=(filter(lambda x:x>44, l))
for a in z:
    print(a)

map =  map(lambda x: x**3 , l)
for m in map:
    print(m)

print([x**3 for x in l])


import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
match=re.search(regex,'jyotismita@gmail.com')
print(match)
pattern = '^[0-9a-zA-Z]+@[a-zA-Z]+\.(com|co\.in)'

x=re.search(pattern, 'jyotismita@gmail.co.in')
print(x)


a=1
a=a+1
print(a)

b=a
b=a+2
print(a,b)
item='milk'
groceries=[]
groceries.append(item)
print(groceries)

items=groceries
item='cheese'
items.append(item)
print(items)
print(groceries, items)

#fibonacci series and generators
def fib(n):
    a,b = 0,1
    while a<n:
        yield a
        a,b = b, a+b


x = fib(10)
for y in x:
    print('y',y)

for i in range(5):
    print(y)



abc = lambda x: x**3, l
print(abc)
print(abc[1])

my_tuple = ('sara', 6, 5, 0.97)
my_list = ['sara', 6, 5, 0.97]


endpoint = "https://status.aws.amazon.com/data.json"

import requests
def extract(obj, key):
    arr = []
    def extract_val(obj,arr,key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v,(dict,list)):
                    extract_val(v,arr,key)
                elif k == key:
                    arr.append(k)
        elif isinstance(obj, list):
            for item in obj:
                extract_val(item, arr, key)
        return arr


def json_pare():
    print('import requests')
    endpoint = "https://status.aws.amazon.com/data.json"
    response = requests.get(endpoint)
    data= response.json()
    values = extract(data, 'service')
    return values

json_pare()

def json_parse1():
    print ('jsonparse1')
    endpoint = "https://status.aws.amazon.com/data.json"
    res = requests.get(endpoint)
    data = res.json()
    res= []
    res_dict={}
    for k,v in data.items():
        if isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    for a, b in i.items():
                        if a == 'service':
                            res.append(i[a])
                            if i[a] in res_dict:
                                res_dict[i[a]] +=1
                            else:
                                res_dict[i[a]] =1
                elif isinstance(i, list):
                    print ('found list in the json!!')

    print ('res', res)
    print ('resdict', res_dict)
#json_parse1()


#DECORATOR
def decorator_fun(function_name):
    def wrapper_fun():
        obj = function_name()
        string_obj = obj.lower()
        return string_obj
    return wrapper_fun

@decorator_fun
def hello_fun():
    return 'HELLO'

print(hello_fun())

for i,j in enumerate(l):
    print(i,j)

print(set(l))
set_l=frozenset(set(l))

sum1= (lambda x: x+x for x in range(1,101))

print(sum(range(0,101)))




