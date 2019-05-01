# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:45:28 2019

@author: preet
"""

import os 

def child():
    print('\nA new child: ', os.getpid())
    

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print("parent: %d, child: %d\n" %pids)
        reply = input("q for quit / c for new fork")
        if reply == 'c':
            continue
        else: 
            break
    
parent()