# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:59:15 2020

@author: Mayra
"""
def binarySearching(array, l, r, m):
    while l <= r:
        mid = l + (r-l)//2
        if array[mid] == m:
            return mid
        elif array[mid] < m:
            l = mid + 1
        else:
            r = mid -1
    return -1
array = [3,6,2,10,77]
m = 10
result = binarySearching(array, 0, len(array)-1, m)
if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present")
