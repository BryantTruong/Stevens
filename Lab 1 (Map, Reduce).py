from cs115 import map, reduce
import math

#I pledge my honor that I have abided by the Stevens Honor System

def inverse(n):
#inverse function taking in n
    return 1/n

def add(a,b):
#adding a and b
    return a+b

def e(n):
#returning the reduce function
    return reduce(add, map(inverse,map(math.factorial,range(n+1))))

def error(n):
#any other errors
    return abs(e(n)-math.e)
