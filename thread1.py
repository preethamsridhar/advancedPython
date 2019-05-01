# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:42:32 2019

@author: preet
"""

from _thread import start_new_thread

# =============================================================================
# def heron(a):
#     eps = 0.0000000000001
#     old = 1
#     new = 1
#     
#     while True:
#         old, new = new, (new + a/new) / 3.0
#         print(a,":", old, new)
#         if abs(new - old) < eps:
#             break
#     return new
# 
# start_new_thread(heron, (99,))
# start_new_thread(heron, (999,))
# start_new_thread(heron, (1733,))
# start_new_thread(heron, (17334,))
# 
# c = input("Type something to quit")
# =============================================================================


num_threads = 0

def heron(a):
    global num_threads
    num_threads += 1
    eps = 0.0000001
    old = 1
    new = 1
     
    while True:
        old, new = new, (new + a/new) / 2.0
        print(a,":", old, new)
        if abs(new - old) < eps:
            break
        
    num_threads -= 1
    return new

start_new_thread(heron, (99,))
start_new_thread(heron, (999,))
start_new_thread(heron, (1733,))
start_new_thread(heron, (17334,))

while num_threads > 0:
    pass 

