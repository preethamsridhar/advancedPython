# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:48:58 2019

@author: preet
"""

import os
import subprocess
# =============================================================================
# def getch():
#     os.system("bash -c \"read -n 2\"")
#     print(s)
# getch()
# =============================================================================

# =============================================================================
# p = os.popen('ls -la')
# print(p.read())
# 
# =============================================================================
# =============================================================================
# 
# command = " "
# while(command != "exist"):
#     command = input("Command: ")
#     handle = os.popen(command)
#     line = " "
#     while line:
#         line = handle.read()
#         print(line)
#     handle.close()
# =============================================================================
# =============================================================================
#     
# os.system('touch xyz')
# p = os.popen('ls -la')
# print(p.read())
# p = subprocess.Popen('cp -r xyz abc', shell=True)
# p = os.popen('ls -la')
# print(p.read())
# =============================================================================


process = subprocess.Popen(['ls','-l'], stdout=subprocess.PIPE)
print(process.stdout.read())


