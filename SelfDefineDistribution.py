# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:10:41 2018

@author: lankuohsing
"""

# In[]
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon as E
# In[]
def exp(lam):
    p=random.random()
    return -math.log(1-p)/lam
# In[]
x1=[]
for i in range(100):
    x1.append(exp(1))
x1=sorted(x1)
y1=np.linspace(0,1,100)
plt.plot(x1,y1,color='blue')
# In[]
rv=E(scale=1)
x2=np.linspace(0,5,100)
plt.plot(x2,rv.cdf(x2),color='red')
plt.show()