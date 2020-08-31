#!/usr/bin/env python
# coding=utf-8
'''
Author: niuyukai
email: 0906150215@csu.edu.cn
Date: 2020-08-17 12:38:17
LastEditTime: 2020-08-30 22:22:48
Description: 
FilePath: \hw1\test1_v1.py
'''
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:40:30 2020

@author: niuyukai
"""

import numpy as np
import matplotlib.pyplot as plt
 
#object
p_o = np.array([0,2])
p_o = p_o.astype(np.float64)
v_o = np.array([5,0])
v_o = v_o.astype(np.float64)

#missile
p_m = np.array([0,0])
p_m = p_m.astype(np.float64)
v_m = 10.

#step time is 0.01
dt = 0.01

#x = np.array([4,4])
#y = np.array([1,0])
#a = np.linalg.norm(x-y,axis=0)
#print(a)

#draw figure 
plt.figure(figsize=(10, 10), dpi=80)
plt.title(" missile flight simulator ", fontsize=40)
plt.xlim(0, 2)
plt.ylim(0, 3)
plt.xticks([])
plt.yticks([])
  
while True:
    m_length = np.linalg.norm(p_o-p_m,axis=0)      
    if m_length <= (v_m * dt):       
        print("collision")
        plt.plot(p_m[0], p_m[1], 'o')
        plt.pause(0.1)
        break    
    #missle position update
    p_m += (p_o - p_m)/m_length * v_m * dt
    #object position update 
    p_o += v_o * dt
    
    x_o, y_o = p_o
    x_m, y_m = p_m
     
    plt.plot(x_o, y_o, 'r.', alpha=.5)
    plt.plot(x_m, y_m, 'bx', alpha=.5)
    plt.legend(("target", "missile"), loc="upper left", prop={'size': 12})
    plt.pause(0.1)