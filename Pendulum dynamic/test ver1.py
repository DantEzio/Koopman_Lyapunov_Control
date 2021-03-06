# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:10:40 2021

@author: Wenchong
"""

import numpy as np
import torch
import pde

grid = pde.UnitGrid([64, 64])                 # generate grid
state = pde.ScalarField.random_uniform(grid)  # generate initial condition

eq = pde.DiffusionPDE(diffusivity=0.1)        # define the pde
result = eq.solve(state, t_range=10)          # solve the pde
result.plot()    