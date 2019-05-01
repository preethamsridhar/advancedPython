# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:42:32 2019

@author: preet
"""

#from _thread import start_new_thread, allocate_lock

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

# =============================================================================
# 
# num_threads = 0
# 
# def heron(a):
#     global num_threads
#     num_threads += 1
#     eps = 0.0000001
#     old = 1
#     new = 1
#      
#     while True:
#         old, new = new, (new + a/new) / 2.0
#         print(a,":", old, new)
#         if abs(new - old) < eps:
#             break
#         
#     num_threads -= 1
#     return new
# 
# start_new_thread(heron, (99,))
# start_new_thread(heron, (999,))
# start_new_thread(heron, (1733,))
# start_new_thread(heron, (17334,))
# 
# while num_threads > 0:
#     print("thread number: ", num_threads)
#     pass 
# =============================================================================

# =============================================================================
# num_threads = 0
# thread_started = False
# 
# lock = allocate_lock()
# 
# def heron(a):
#     global num_threads, thread_started
#     lock.acquire()
#     
#     num_threads += 1
#     thread_started = True
#     lock.release()
# 
#     eps = 0.0000001
#     old = 1
#     new = 1
#   
#     while True:
#         old, new = new, (new + a/new) / 2.0
#         print(a,":", old, new)
#         if abs(new - old) < eps:
#             break
#         
#     lock.acquire()
#     num_threads -= 1
#     lock.release()
#     return new
# 
# start_new_thread(heron,(99,))
# start_new_thread(heron,(999,))
# start_new_thread(heron,(1733,))
# 
# while not thread_started:
#     pass
# while num_threads > 0:
#     print("\nthread number: ", num_threads)
#     pass
# 
# 
# =============================================================================

# =============================================================================
# import time
# from threading import Thread
# 
# def sleeper(i):
#     print("thread %d sleeps for 5 seconds" %i)
#     time.sleep(5)
#     print("thread %d woke up" %i)
#     
# for i in range(10):
#     t = Thread(target=sleeper, args=(i,))
#     t.start()
# 
# =============================================================================

# =============================================================================
# import threading
# 
# class PrimeNumber(threading.Thread):
#     prime_numbers = {}
#     lock = threading.Lock()
#     
#     def __init__(self, number):
#         threading.Thread.__init__(self)
#         self.Number = number
#         PrimeNumber.lock.acquire()
#         PrimeNumber.prime_numbers[number] = "None"
#         PrimeNumber.lock.release()
#         
#     def run(self):
#         counter = 2
#         res = True
#         while counter * counter <= self.Number and res:
#             if self.Number % counter == 0:
#                 res = False
#             counter += 1
#         PrimeNumber.lock.acquire()
#         PrimeNumber.prime_numbers[self.Number] = res
#         PrimeNumber.lock.release()
#         
# threads = []
# while True:
#     inp = int(input("number: "))
#     if inp < 1:
#         break
#     thread = PrimeNumber(inp)
#     threads += [thread]
#     thread.start()
#     
# print(threads.join())
# 
# 
# =============================================================================

import os, re

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

for suffix in range(20, 30):
    ip = "192.168.1."+str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip,"r")
    print("pinging..", ip)
    
    while True: 
        line = ping_out.readline()
        if not line: break
    
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
            



            
4












