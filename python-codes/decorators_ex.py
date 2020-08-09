"""
Decorators in Python
In Python, functions are the first class objects, which means that –

Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
Functions can be defined inside another function and can also be passed as argument to another function.
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.

In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
"""

########Example1#################################
def hello_decorator(func): 
    def inner1(*args, **kwargs): 
          
        print("before Execution") 
          
        # getting the returned value 
        returned_value = func(*args, **kwargs) 
        print("after Execution") 
          
        # returning the value to the original frame 
        return returned_value 
          
    return inner1 
  
  
# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b): 
    print("Inside the function") 
    return a + b 
  
a, b = 1, 2
  
# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b))

########Example2#################################
def decorator_fun(original_fun):
	def hello_fun1():
		print("inside hello_fun1")
		original_fun()
		print("after hello_fun1")
	return hello_fun1
		

@decorator_fun
def hello_world():
	print("inside hello_world!!")

hello_world()