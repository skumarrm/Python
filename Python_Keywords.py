import keyword
print(keyword.kwlist)

"""
1) None ---> Used to reprsent a Null Value or constant havng empty value,void function will return None
Eg:
def a_void_function():
    a = 1
    b = 2
    c = a + b

x = a_void_function()
print(x)

2) and,or,not are ogical operators in Python

3) as ---> it is used to create alias while importing a module
eg: import math as m1
    m1.cos(m1.pi)

4) assert ---> used for debugging purposes.If condition is true nothing happens,if it false,then it throws assertion error
   eg: assert a > 5, "The value of a is too small"
       AssertionError: The value of a is too small
       
   eg: assert condition,message => if not condition:
                                      raise AssertionError(message)
    
5) del ---> is used to delete the reference to an object. Everything is object in Python
       a=b=5
       del a
       a
       Error : a is not defined.
    a=[1,2,3]
    del a[1]
    a  ---> [1,3]
       
5) except
  Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python.
   	
   	if num == 0:
    raise ZeroDivisionError('cannot divide')
 	
 	try:
        r = 1/num
    except:
        print('Exception caught')
        return
    return r

6) finally =---->is used with try…except block to close up resources or file streams.
   Using finally ensures that the block of code inside it gets executed even if there is an unhandled exception. For example
   
try:
    Try-block
except exception1:
    Exception1-block
except exception2:
    Exception2-block
else:
    Else-block
finally:
    Finally-block
 	
7) from…import is used to import specific attributes or functions into the current namespace
   
   from math import cos
   Now no need to write math.cos()
   
8) global ---> is used to declare that a variable inside the function is global (outside the function)

globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15

read1()
write1()
read1()
write2()
read1()

9) in ---> used to test a sequence list,tuple,string

>>> a = [1, 2, 3, 4, 5]
>>> 5 in a
True
>>> 10 in a
False

for i in 'hello':
    print(i)

10) is ---> used to test object identity

is is used in Python for testing object identity. While the == operator is used to test if two variables are equal or not, is is used to test if the two variables refer to the same object.

It returns True if the objects are identical and False if not.

>>> True is True
True
>>> False is False
True
>>> None is None
True

10) lambda ---> used to create anonyms function

lambda is used to create an anonymous function (function with no name). It is an inline function that does not contain a return statement. It consists of an expression that is evaluated and returned. For example:

11) nonlocal

   nonlocal

The use of nonlocal keyword is very much similar to the global keyword. nonlocal is used to declare that a variable inside a nested function (function inside a function) is not local to it, meaning it lies in the outer inclosing function. If we need to modify the value of a non-local variable inside a nested function, then we must declare it with nonlocal. Otherwise a local variable with that name is created inside the nested function. Following example will help us clarify this.

def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)

outer_function()

12) pass ---> pass is a null statement in Python. Nothing happens when it is executed. It is used as a placeholder

Suppose we have a function that is not implemented yet, but we want to implement it in the future. Simply writing,

def function(args):

in the middle of a program will give us IndentationError. Instead of this, we construct a blank body with the pass statement.

def function(args):
    pass

class example:
    pass
    
13) lambda ----> is an anonymous function
a = lambda x: x*2
for i in range(1,6):
    print(a(i))
    
14) with ---> with statement is used to wrap the execution of a block of code within methods defined by the context manager
with

with statement is used to wrap the execution of a block of code within methods defined by the context manager.

Context manager is a class that implements __enter__ and __exit__ methods. Use of with statement ensures that the __exit__ method is called at the end of the nested block. This concept is similar to the use of try…finally block. Here, is an example.

with open('example.txt', 'w') as my_file:
    my_file.write('Hello world!')

This example writes the text Hello world! to the file example.txt. File objects have __enter__ and __exit__ method defined within them, so they act as their own context manager.

First the __enter__ method is called, then the code within with statement is executed and finally the __exit__ method is called. __exit__ method is called even if there is an error. It basically closes the file stream.

15) yield --->
yield

yield is used inside a function like a return statement. But yield returns a generator.

Generator is an iterator that generates one item at a time. A large list of value will take up a lot of memory. Generators are useful in this situation as it generates only one value at a time instead of storing all the values in memory. For example,

>>> g = (2**x for x in range(100))

will create a generator g which generates powers of 2 up to the number two raised to the power 99. We can generate the numbers using the next() function as shown below.

>>> next(g)
1
>>> next(g)
2
>>> next(g)
4
>>> next(g)
8
>>> next(g)
16

And so on… This type of generator is returned by the yield statement from a function. Here is an example.

def generator():
    for i in range(6):
        yield i*i

g = generator()
for i in g:
    print(i) 
            
"""