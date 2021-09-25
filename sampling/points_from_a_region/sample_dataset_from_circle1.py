# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:28:25 2021

@author: lankuohsing
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

#right
def GenerateDatasetInCycle(
        point_num,
        start_theta=0.0,
        end_theta=2*np.pi,
        radius=0.0,
        center_x=0.0,
        center_y=0.0,
        label=0,
        constraint_x=0.0,
        constraint_y=0.0,
        constraint_r=0.0,
        is_constraint=False
        ):
    theta=np.linspace(start_theta,end_theta,1000)
    x=np.cos(theta)*radius+center_x
    y=np.sin(theta)*radius+center_y
    plt.plot(x,y,label="circle",color="red",linewidth=2)
    dataset=[]
    for i in range(1, point_num+1):
        theta = random.random()*2*np.pi;
        r = random.uniform(0, radius)
        x = math.sin(theta)* (r**0.5) + center_x
        y = math.cos(theta)* (r**0.5) + center_y
        if is_constraint:
            if(x-constraint_x)**2+(y-constraint_y)**2>constraint_r**2:
                continue
        plt.plot(x, y, '*', color = "black")
        dataset.append((x,y,label))
if __name__=="__main__":
    pi = np.pi
    R = 1

    plt.figure(figsize=(6,6))
    plt.title("circle")
    dataset_1=GenerateDatasetInCycle(1000,start_theta=0.0,end_theta=pi/2,radius=R,center_x=2.0,center_y=1.0,label=1,constraint_x=2.0,constraint_y=0.75,constraint_r=0.5,is_constraint=True)
    dataset_2=GenerateDatasetInCycle(1000,start_theta=3*pi/2,end_theta=2*pi,radius=R,center_x=1.0,center_y=2.0,label=2,constraint_x=0.75,constraint_y=2.0,constraint_r=0.5,is_constraint=True)
    dataset_3=GenerateDatasetInCycle(1000,start_theta=pi/2,end_theta=pi,radius=R,center_x=3.0,center_y=2.0,label=3,constraint_x=3.25,constraint_y=2.0,constraint_r=0.5,is_constraint=True)
    dataset_4=GenerateDatasetInCycle(1000,start_theta=pi,end_theta=3*pi/2,radius=R,center_x=2.0,center_y=3.0,label=4,constraint_x=2.0,constraint_y=3.25,constraint_r=0.5,is_constraint=True)
    plt.legend()
    plt.grid()
    plt.show()