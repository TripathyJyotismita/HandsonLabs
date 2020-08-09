import threading
import time

def hello_fun1():
    print('calling threading fun')
    time.sleep(0.5)

def hello_fun2():
    print('calling threading fun2')
    time.sleep(0.5)

#t1=Thread(target=hello_fun1())
#t2=Thread(target=hello_fun2())

#t1.start()
#t2.start()
