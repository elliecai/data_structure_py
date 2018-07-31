# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:33:08 2018

@author: ellie.cai
"""

#0,1,1,2,3,5,8,


def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

       
fibolist=[]
for i in range(10):
    fibolist.append(fibo(i))
    
    
    




def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def trace(f):
    f.indent = 0
    def g(x):
        print( '|  ' * f.indent + '|--', f.__name__, x)
        f.indent += 1
        value = f(x)
        print ('|  ' * f.indent + '|--', 'return', repr(value))
        f.indent -= 1
        return value
    return g

fib = trace(fib)
print (fib(4))












