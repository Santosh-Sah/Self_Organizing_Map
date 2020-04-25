# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:18:33 2020

@author: Santosh Sah
"""

from pylab import bone, pcolor, colorbar, plot, show, save
import pylab
from SelfOrganizingMapUtils import (readSelfOrganizingMapModel, readSelfOrganizingMapXTrain, readSelfOrganizingMapYTrain)
"""
Visualizing SelfOrganizingMap
"""
def visualisingSelfOrganizingMap():
        
    selfOrganizingMapModel = readSelfOrganizingMapModel()
    X = readSelfOrganizingMapXTrain()
    y = readSelfOrganizingMapYTrain()
    
    bone()
    pcolor(selfOrganizingMapModel.distance_map().T)
    colorbar()
    markers = ['o', 's']
    colors = ['r', 'g']
    
    for i, x in enumerate(X):
        w = selfOrganizingMapModel.winner(x)
        plot(w[0] + 0.5,
             w[1] + 0.5,
             markers[y[i]],
             markeredgecolor = colors[y[i]],
             markerfacecolor = 'None',
             markersize = 10,
             markeredgewidth = 2)
        
    pylab.savefig('visualisingSelfOrganizingMap.jpg')
    show()    

        
if __name__ == "__main__":
    visualisingSelfOrganizingMap()
    

