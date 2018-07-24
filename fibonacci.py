# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 13:36:34 2018

@author: ellie.cai
"""

#fibonacci solution 1 

a=[0,1]

for i in range(2,20):

    a.append(a[i-1]+a[i-2])

    

print(a)







def fab1(n):

    a=[0,1]

    for i in range(2,n+1):

        a.append(a[i-1]+a[i-2])

    return a[n]




print(fab1(20))




        

#fibonnaci solution 2 







def fab(n):

    if n==0:

        return 0

    if n==1:

        return 1

    if n>1:

        return fab(n-1)+fab(n-2)

    

print(fab(20))