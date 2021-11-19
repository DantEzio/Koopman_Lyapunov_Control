# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:10:40 2021

@author: Wenchong
"""

import numpy as np
import pandas as pd


class VP_O:
    
    def __init__(self,params):
        
        '''
        System dynamic:
            dx=ay;
            dy=bx+cy+dx^2y+u
            
        parameter list: 
            a:2
            b:-0.8
            c:2
            d:-10
            delta_t:0.01
        '''
        #parameters
        self.params=params
        
    def sim(self,x0,y0,T,u):
        #list of control input, with shape of (1,T-1)
        
        #simulation step
        x,y=[x0],[y0]
        
        for t in np.arange(T):
            xtem=(1+self.params['a']*self.params['delta_t'])*x[-1]
            xbar=(xtem+x[-1])/2
            ytem=y[-1]+self.params['delta_t']*(self.params['b']*xbar+
                                               self.params['c']*y[-1]+
                                               self.params['d']*xbar**2*y[-1]+
                                               u[t])
            x.append(xtem)
            y.append(ytem)
        
        x,y=np.array(x),np.array(y)
        return x,y    
        
        
        