# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:34:08 2019

@author: preet
"""

def zip_longest(iter1, iter2, fillchar=None):
    for i in range(max(len(iter1), len(iter2))):
        if i >= len(iter1):
            yield (fillchar, iter2[i])
        elif i >= len(iter2):
            yield (iter1[i], fillchar)
        else:
            yield (iter1[i], iter2[i])
        i += 1

def prnt(var):
    for i in var:
        yield i

for x in prnt([2,4,5,3,1,8,6,9,7,0]):
    print(x)

p1 = (2, )
p2 = (-1, 4, 5)
for x in zip_longest(p1, p2, fillchar=0):
    print(x)