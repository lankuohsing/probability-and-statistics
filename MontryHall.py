# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 17:02:15 2018

@author: lankuohsing
"""
# In[]
import random
def MontryHall(Dselect, Dchange):
    Dcar=random.randint(1,3)#1<=Dcar<=3
    if (Dcar==Dselect and Dchange==0):#一开始选中而且不改变选择
        return 1
    elif (Dcar!=Dselect and Dchange==0):#一开始没选中而且不改变选择
        return 0
    elif (Dcar==Dselect and Dchange==1):#一开始选中而且改变选择
        return 0
    else:                               #一开始没选中而且改变选择
        return 1
# In[]
#不确定是否改变选择
n=10000
win=0
for i in range(n):
    Dselect=random.randint(1,3)
    Dchange=random.randint(0,1)
    win=win+MontryHall(Dselect, Dchange)
print('不确定是否改变选择:',float(win)/float(n))
# In[]
#确定不改变选择
n=10000
win=0
for i in range(n):
    Dselect=random.randint(1,3)
    Dchange=0
    win=win+MontryHall(Dselect, Dchange)
print('确定不改变选择:',float(win)/float(n))
# In[]
#确定改变选择
n=10000
win=0
for i in range(n):
    Dselect=random.randint(1,3)
    Dchange=1
    win=win+MontryHall(Dselect, Dchange)
print('确定改变选择:',float(win)/float(n))