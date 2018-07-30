# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:25:21 2018

@author: ellie.cai
"""



def movedisk(frompole,topole):
    print('move disk from '+frompole +' to '+topole)



def hanoi(height,leftpole,middlepole,rightpole):
    if height>=1:
        hanoi(height-1,leftpole,rightpole,middlepole)
        movedisk(leftpole,rightpole)
        hanoi(height-1,middlepole,leftpole,rightpole)
    


hanoi(3,'a','b','c')

