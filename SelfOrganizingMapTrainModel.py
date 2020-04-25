# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:18:10 2020

@author: Santosh Sah
"""

from minisom import MiniSom
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from SelfOrganizingMapUtils import (saveSelfOrganizingMapModel, readSelfOrganizingMapXTrain, saveSelfOrganizingMapStandardScaler, readSelfOrganizingMapModel,
                                    readSelfOrganizingMapStandardScaler)

"""
Train SelfOrganizingMap model 
"""
def trainSelfOrganizingMapModel():
    
    selfOrganizingMapStandardScalar = MinMaxScaler(feature_range=(0, 1))
    
    X = readSelfOrganizingMapXTrain()
    
    selfOrganizingMapStandardScalar.fit(X)
    saveSelfOrganizingMapStandardScaler(selfOrganizingMapStandardScalar)
    
    X = selfOrganizingMapStandardScalar.transform(X)
    
    selfOrganizingMap = MiniSom(x = 10, y = 10, input_len = 15, sigma=1.0, learning_rate=0.5)
    selfOrganizingMap.random_weights_init(X)
    selfOrganizingMap.train_random(data = X, num_iteration=100)
   
    
    saveSelfOrganizingMapModel(selfOrganizingMap)

def selfOrganizingMapFindFrauds():
    
    selfOrganizingMapModel = readSelfOrganizingMapModel()
    selfOrganizingMapStandardScaler = readSelfOrganizingMapStandardScaler()
    X = readSelfOrganizingMapXTrain()
    
    mappings = selfOrganizingMapModel.win_map(X)
    #frauds = np.concatenate((mappings[(0,2)], mappings[(1,3)]), axis = 0)
    frauds = mappings[(0,2)]
    
    frauds = selfOrganizingMapStandardScaler.inverse_transform(frauds)
    pd.DataFrame(frauds).to_csv("fraud_customers.csv")
    

if __name__ == "__main__":
    #trainSelfOrganizingMapModel()
    selfOrganizingMapFindFrauds()