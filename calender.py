# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:19:33 2020

@author: Dell
"""

from tqdm import tqdm
import time
for i in tqdm (range(50)):
    time.sleep(0.1)
import calendar
y = int(input("input the year : "))
m = int(input("input the month : "))
print(calendar.month(y,m))