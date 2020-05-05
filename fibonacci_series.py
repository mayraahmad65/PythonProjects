# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:14:36 2020

@author: Mayra
"""
def fibonnaci(x):
    if x<0:
        print("Invalid input")
    elif x==1:
        return 0
    elif x==2:
        return 1
    else:
        return fibonnaci(x-1)+fibonnaci(x-2)
print(fibonnaci(10))
