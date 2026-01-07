# module = a file containing code you want to include in your program
#           use 'import' to inlcude a module (built-in or your own)
#           useful to break up large program reusable separable files

#import math
#import math as m
from math import pi

print(pi)

#create your own module
#created module.py
# pi = 3.14

# def square (x):
#     return x ** 2

# def cube(x):
#     return x**3 
# def circumference(r):
#     return 2 * pi *r
# def area(r):
#     return pi * r ** 2


import module
result = module.pi
sq= module.square(3)
area = module.area(3)
cube = module.cube(3)

print(result)
print(sq)
print(area)
print(cube)