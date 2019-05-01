# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:09:29 2019

@author: preet
"""

class Counter:
    def __init__(self):
        self.__count = 0
    
    def count(self):
        self.__count += 1
        print(self.__count)
        
counter = Counter()
counter.count()
counter.count()
print(counter.__count)