#-*- encoding=utf-8 -*-
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
# In[]

# 按照固定区间长度绘制频率分布直方图
# bins_interval 区间的长度
# margin        设定的左边和右边空留的大小
def probability_distribution(data, bins_interval=1, margin=1):
    bins = range(min(data), max(data) + bins_interval*2, bins_interval)
    print(len(bins))
    for i in range(0, len(bins)):
        print(bins[i])
    plt.xlim(min(data) - margin, max(data) + margin)
    plt.title("Frequency-Distribution")
    plt.xlabel('Interval')
    plt.ylabel('Frequency')
    plt.hist(x=data, bins=bins, histtype='bar', color=['r'])
    plt.show()

# In[]
data=np.array([1,2,3,4,5,6,7,8,9,10])*10
probability_distribution(data=data,bins_interval=10, margin=0)
