# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:34:08 2019

@author: preet
"""

def zip_longest(iter1, iter2, fillchar=None):
    for i in range(max(len(iter1()), len(iter2))):
        if i >= len(iter1):
            yield (fillchar, iter2[i])
        elif i >= len(iter2):
            yield (iter1[i], fillchar)
        else:
            