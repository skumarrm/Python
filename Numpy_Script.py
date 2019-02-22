import numpy as np
import os
a = np.arange(15).reshape(3, 5)
print(a)
print(os.environ['b']) # reading the environmental variable b
print("__________________")
new_array = np.zeros((4,3), dtype=float)
print(new_array)
print("__________________")
newer_array = np.zeros_like(new_array,dtype=int)
print(newer_array)
print("__________________")
newer_array = np.copy(new_array)
print(newer_array)
print("__________________")
newer_array=np.array([1,2,3,4,5,6])
print(newer_array)
print("__________________")
new_array = np.arange(1, 10, 2)
print(new_array)
print("__________________")
new_array = np.linspace(1, 100, num=10, endpoint=True)
print(new_array)
print("__________________")
new_array = np.logspace(1, 10, num=10, endpoint=True, base=2)
print(new_array)
print("__________________")
x = np.linspace(0, 1, 7)
y = np.linspace(0, 1, 11)
xx, yy = np.meshgrid(x, y)
print(xx,yy)
print("__________________")
x = np.arange(12)
a,b,c,d = np.split(x, 4)
print(a,b,c)
print("__________________")
x = np.arange(27).reshape((3,9))
a,b,c = np.split(x, [2,6], axis=1)
print(a,b,c)
print("__________________")
    a = np.arange(30).reshape((2,3,5))
    b = np.arange(42).reshape((2,3,7))
    print(a,b)
    print("__________________")
    c = np.concatenate((a, b), axis=1)
    print(c)
np.arange(6).reshape((3, 2))
a[:, np.newaxis]
a.ravel()
a.flatten()
np.linspace(0, 10, num=50).view(complex)
np.linspace(0, 10, num=50).astype(complex)
np.arange(210).reshape((2,3,5,7)).transpose()
np.arange(210).reshape((2,3,5,7)).transpose((2,1,0,3))
np.arange(210).reshape((2,3,5,7)).swapaxes(1,3)
np.rollaxis(np.arange(210).reshape((2,3,5,7)), 2, 0)
np.roll(np.arange(10).reshape((2,5)), 2, axis=1)

x = np.arange(12)
a,b,c = np.split(x, 3)

x = np.arange(27).reshape((3,9))
a,b,c = np.split(x, [2,6], axis=1)

a = np.arange(30).reshape((2,3,5))
b = np.arange(42).reshape((2,3,7))
c = np.concatenate((a, b), axis=1)

"""
__package__
__name__
__dict__
__doc__
__file__
__path__
__import__
"""
"""
hello
"""