# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:06:10 2019

@author: preet
"""

import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return x**4 - 4*x**2 + 3*x

X = np.linspace(-3, 3, 50, endpoint=True)
F = p(X)
plt.plot(X, F)
plt.show()
