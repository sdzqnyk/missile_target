#!/usr/bin/env python
# coding=utf-8
'''
Author: niuyukai
email: 0906150215@csu.edu.cn
Date: 2020-08-21 18:15:41
LastEditTime: 2020-08-30 22:22:03
Description: 面向对象missile_v3
FilePath: \hw1\test1_v3.py
'''
import numpy as np
import matplotlib.pyplot as plt
import copy
#import uuid

tolerance = 1e-1
# plane initial 
p_p = np.array([0,2])
p_p = p_p.astype(np.float64)
v_p = np.array([5,0])
v_p = v_p.astype(np.float64) 

# missile initial
p_m = np.array([0,0])
p_m = p_m.astype(np.float64)
v_m = 10.

#draw picture
plt.figure(figsize=(10, 10), dpi=80)
plt.title(" missile flight simulator ", fontsize=40)
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.xticks([])
plt.yticks([])

class Environment:
    def __init__(self, dt=0.01):
        self.children = []  # List[Entity]
        self.dt = dt
        self.events = []  # Functional

    def step(self):
        # 1. 每个实体步进.
        for child in self.children:
            child.step(self.dt)

        # 2.根据其他实体改变自己状态.
        self.access()

        # 3.调用环境步进事件.
        self.events
       # if self.events:
            #self.events(self)

    def access(self):
        children_copy = copy.deepcopy(self.children)
        for child in self.children:
            others = [obj for obj in children_copy if obj.id != child.id]
            for other in others:
                child.access(other)

    def finish(self) -> bool:
        if np.linalg.norm(self.children[1].pos - self.children[0].pos, axis=0) <= tolerance:
            print("collision")
            x, y = self.children[1].pos
            plt.plot(x, y, 'o')
            plt.annotate('crash point', xy=(x, y),  xycoords='data',
                        xytext=(+15, +15), textcoords='offset points', fontsize=12,
                        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
            plt.pause(0.1)
            plt.show()               
            return True
        else:
            return False

class Entity(object):    
    _id = 0 

    def __init__(self, pos):        
        self.pos = pos

    def step(self, dt):
        """ 根据当前状态，步进一步. """
        pass

    def access(self, other):
        """ 根据其他对象，改变自身状态. """        
        pass

class Plane(Entity):
    _id = 0

    def __init__(self, pos, v):
        super(Plane, self).__init__(pos)
        self.v = v
        self.id = Plane._id
        Plane._id += 1

    def step(self, dt):
        self.pos += self.v * dt

    def access(self, other):        
        return self.v
    
class Missile(Entity):
    _id = 1
    v_m = 10.
    def __init__(self, pos, v):
        super(Missile, self).__init__(pos)
        self.id = Missile._id
        Missile._id += 1
        self.v = v

    def step(self, dt):
        self.pos += self.v * dt          

    def access(self, other):        
        self.v = Missile.v_m * ((other.pos - self.pos) / np.linalg.norm(other.pos - self.pos, axis=0))        
        return self.v

def paint_env(env: Environment):
    #print alpha, beta
    x_m, y_m = env.children[0].pos
    x_p, y_p = env.children[1].pos
    plt.plot(x_m, y_m, 'bx', alpha=.5)
    plt.plot(x_p, y_p, 'k*', alpha=.5)
    plt.legend(("Missile", "Plane"), loc="upper left", prop={'size': 12})
    plt.pause(0.1)
    
def print_env(env: Environment):
    print(env.children[0].pos, env.children[1].pos)
    print(env.children[0].v) 

if __name__ == '__main__':
    env = Environment()
   # env.events.append(paint_env(env))
   # env.events.append(print_env(env))
    env.children.append(Missile(p_m, v_m))
    env.children.append(Plane(p_p, v_p))
       
    while not env.finish():
        env.events.append(paint_env(env))
        env.events.append(print_env(env))
        env.step()
        #print_env(env)
        #paint_env(env)       