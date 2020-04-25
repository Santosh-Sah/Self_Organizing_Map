# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:16:58 2020

@author: Santosh Sah
"""

import pandas as pd
import pickle

"""
Import dataset and read specific column. Split the dataset in training and testing set.
"""
def importSelfOrganizingMapDataset(selfOrganizingMapDatasetFileName):
    
    selfOrganizingMapDataset = pd.read_csv(selfOrganizingMapDatasetFileName)
    X = selfOrganizingMapDataset.iloc[:, :-1].values
    y = selfOrganizingMapDataset.iloc[:, -1].values
    
    return X, y

"""
Save standard scalar object as a pickel file. This standard scalar object must be used to standardized the dataset for training, testing and new dataset.
To use this standard scalar object we need to read it and then use it.
"""
def saveSelfOrganizingMapStandardScaler(selfOrganizingMapStandardScalar):
    
    #Write SelfOrganizingMapStandardScaler in a picke file
    with open("SelfOrganizingMapStandardScaler.pkl",'wb') as SelfOrganizingMapStandardScaler_Pickle:
        pickle.dump(selfOrganizingMapStandardScalar, SelfOrganizingMapStandardScaler_Pickle, protocol = 2)

"""
Save training and testing dataset
"""
def saveTrainingAndTestingDataset(X_train, y_train):
    
    #Write X_train in a picke file
    with open("X_train.pkl",'wb') as X_train_Pickle:
        pickle.dump(X_train, X_train_Pickle, protocol = 2)
        
    #Write y_train in a picke file
    with open("y_train.pkl",'wb') as y_train_Pickle:
        pickle.dump(y_train, y_train_Pickle, protocol = 2)

"""
Save SelfOrganizingMapModel as a pickle file.
"""
def saveSelfOrganizingMapModel(selfOrganizingMapModel):
    
    #Write SelfOrganizingMapModel as a picke file
    with open("SelfOrganizingMapModel.pkl",'wb') as SelfOrganizingMapModel_Pickle:
        pickle.dump(selfOrganizingMapModel, SelfOrganizingMapModel_Pickle)

"""
read SelfOrganizingMapStandardScalar from pickel file
"""
def readSelfOrganizingMapStandardScaler():
    
    #load SelfOrganizingMapStandardScaler object
    with open("SelfOrganizingMapStandardScaler.pkl","rb") as SelfOrganizingMapStandardScaler:
        selfOrganizingMapStandardScalar = pickle.load(SelfOrganizingMapStandardScaler)
    
    return selfOrganizingMapStandardScalar

"""
read SelfOrganizingMapModel from pickle file
"""
def readSelfOrganizingMapModel():
    
    #load SelfOrganizingMapModel model
    with open("SelfOrganizingMapModel.pkl","rb") as SelfOrganizingMapModel:
        selfOrganizingMapModel = pickle.load(SelfOrganizingMapModel)
    
    return selfOrganizingMapModel

"""
read X_train from pickle file
"""
def readSelfOrganizingMapXTrain():
    
    #load X_train
    with open("X_train.pkl","rb") as X_train_pickle:
        X_train = pickle.load(X_train_pickle)
    
    return X_train

"""
read y_train from pickle file
"""
def readSelfOrganizingMapYTrain():
    
    #load y_train
    with open("y_train.pkl","rb") as y_train_pickle:
        y_train = pickle.load(y_train_pickle)
    
    return y_train