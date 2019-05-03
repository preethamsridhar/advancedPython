# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:04:10 2019

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

    def degree(self, x):
        return len(self.coefficients)
    
    @staticmethod
    def zip_longest(iter1, iter2, fillchar=None):
        for i in range(max(len(iter1), len(iter2))):
            if i >= len(iter1):
                yield (fillchar, iter2[i])
            elif i >= len(iter2):
                yield (iter1[i], fillchar)
            else:
                yield (iter1[i], iter2[i])
            i += 1
            
    def __add__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        res = [t1 + t2 for t1, t2 in Polynomial.zip_longest(c1, c2)]
        return Polynomial(*res)
    
    def __sub__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        res = [t1 - t2 for t1, t2 in Polynomial.zip_longest(c1, c2)]
        return Polynomial(*res)
    
    def derivative(self):
        derived_coeffs = []
        exponent = 1
        for i in range(1, len(self.coefficients)):
            derived_coeffs.append(self.coefficients[i] * exponent)
            exponent += 1
        return Polynomial(*derived_coeffs[::-1])
    
    def __str__(self):
        res = ""
        for i in range(len(self.coefficients) -1 , -1, -1 ):
            res += str(self.coefficients[i]) + "x^" + str(i) + " + "
        if res.endswith("+ "):
            res = res[:-3]
        return res

    
p1 = Polynomial(4, 0, -4, 3, 0)
p2 = Polynomial(-0.8, 2.3, 0.5, 1, 0.2)
p_sum = p1 + p2
p_diff = p1 - p2

X = np.linspace(-3, 3, 50, endpoint=True)
F1 = p1(X)
F2 = p2(X)


F_sum = p_sum(X)
F_diff = p_diff(X)

plt.figure(num=None, figsize=(16, 12), dpi=50, facecolor='y', edgecolor='k')
plt.rcParams.update({'font.size': 22})

plt.plot(X, F1, label="F1",linewidth=5)
plt.plot(X, F2, label="F2", linewidth=5)
plt.plot(X, F_sum, label="F_sum", linewidth=5)
plt.plot(X, F_diff, label="F_diff", linewidth=5)
plt.legend()
plt.savefig("graphPolynomial.png")
plt.show()

print(p1)
print(p2)
print(p_sum)
print(p_diff)