# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:39:11 2021

@author: lankuohsing
"""

# In[]
import numpy as np
import matplotlib.pyplot as plt
import random
import math
# In[]
'''
random.uniform(a, b)
Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
The end-point value b may or may not be included in the range depending on floating-point rounding in the equation a + (b-a) * random().
'''

def sample_points_from_rectangle(top_left_point:tuple,bottom_right_point,num_points:int)->np.array:
    result=np.ones((num_points,2))
    for i in range(0,num_points):
        x=random.uniform(top_left_point[0],bottom_right_point[0])
        y=random.uniform(top_left_point[1],bottom_right_point[1])
        result[i][0]=x
        result[i][1]=y
    return result
def generate_line(start,end,num)->np.array:
    return np.array(list(range(0,num)))/(num-1)*(end-start)+start
if __name__=="__main__":
    top_left_point=(0,2)
    bottom_right_point=(3,0)
    random.seed(1)
    num_points_in_area=1000
    points_in_area=sample_points_from_rectangle(top_left_point,bottom_right_point,num_points_in_area)
    print(points_in_area)
    num_points_in_line=101
    line_top_x=generate_line(top_left_point[0],bottom_right_point[0],num_points_in_line)
    line_top_y=[top_left_point[1]]*num_points_in_line
    line_bottom_x=line_top_x
    line_bottom_y=[bottom_right_point[1]]*num_points_in_line
    line_left_x=[top_left_point[0]]*num_points_in_line
    line_left_y=generate_line(top_left_point[1],bottom_right_point[1],num_points_in_line)
    line_right_x=[bottom_right_point[0]]*num_points_in_line
    line_left_y=line_left_y
# In[]
    plt.figure(figsize=(6,6))
    plt.plot(line_top_x,line_top_y,color="black",linewidth=2)
    plt.plot(line_bottom_x,line_bottom_y,color="black",linewidth=2)
    plt.plot(line_left_x,line_left_y,color="black",linewidth=2)
    plt.plot(line_right_x,line_left_y,color="black",linewidth=2)
    plt.plot(points_in_area[:,0],points_in_area[:,1],'r*')
    plt.title("rectangle")
    plt.legend()
    plt.show()