# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:16:06 2019

@author: preet
"""

import numpy as np
import matplotlib.pyplot as plt

class Polynomial:
    
    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]
    
    def __repr__(self):
        return "Polynomial" + str(self.coefficients[::-1])
  
    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x ** index
        return res
    
    
p = Polynomial(4, 0, -4, 3, 0)
for x in range(-3, 3):
    print(x, p(x))
    
X = np.linspace(-3, 3, 50, endpoint=True)
F = p(X)
plt.plot(X, F)
plt.show()

