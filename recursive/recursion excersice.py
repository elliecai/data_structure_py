# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:42:23 2018

@author: ellie.cai
"""

## the questions can be found in the following website
#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php



## 1. Write a Python program to calculate the sum of a list of numbers.

def sumlist(numlist):
    if len(numlist)==1:
        return numlist[0]
    else:
        return(numlist[0]+sumlist(numlist[1:len(numlist)]))

###2. Write a Python program to converting an Integer to a string in any base.
        
def intstr(a,base):
    if a<base:
        return str(a)
    else:
        return(intstr(int(a/base),base)+str(a%base))
        
intstr(124654,2)    



####3. Write a Python program of recursion list sum.

[ [1, 2, [3, 4] ], [5, 6], 7]

####4. Write a Python program to get the factorial of a non-negative integer.
####5. Write a Python program to solve the Fibonacci sequence using recursion.
####6. Write a Python program to get the sum of a non-negative integer. 
####7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). 
####8. Write a Python program to calculate the harmonic sum of n-1.
####9. Write a Python program to calculate the geometric sum of n-1.
####10. Write a Python program to calculate the value of 'a' to the power 'b'. 

def power(a,b):
    if b<1:
        return 1
    else:
        return a*power(a,b-1)

power(2,4)

####11. Write a Python program to find  the greatest common divisor (gcd) of two integers.








[ [1, 2, [3, 4] ], [5, 6], 7]


def flat(n):
    result=[]
    
    [flat(x,result) for x in n if isinstance(x,list) else ]











1/10

len(str(1/10))



int(12/10)

len(str(1))

str(5%10)

123456/10











a=[0,12,3]

sumlist(a)


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

fib = trace(sumlist)
print(fib(a))












