# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 21:26:51 2018

@author: lankuohsing
"""

# In[]
import numpy as np
import scipy.stats as sta
import matplotlib.pyplot as plt
# In[]
X=sta.norm(loc=950,scale=20) # 均值为950，标准差为20的正态分布
wbread=[]
# In[]
#x=X.rvs(size=100)
# In[]
for i in range(365):
    x=X.rvs(size=100)#产生100个按照X分布的随机变量
    wbread.append(x[0])
# In[]
print(np.mean(wbread))
print(sta.skew(wbread))
plt.hist(wbread,color='grey')
# In[]
wbread=[]
# In[]
for i in range(365):
    x=X.rvs(size=100)#产生100个按照X分布的随机变量
    wbread.append(max(x))
# In[]
print(np.mean(wbread))
# In[]
print(sta.skew(wbread))
# In[]
plt.hist(wbread,color='grey')