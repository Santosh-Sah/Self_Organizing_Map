# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:17:46 2020

@author: Santosh Sah
"""

from SelfOrganizingMapUtils import (importSelfOrganizingMapDataset, saveTrainingAndTestingDataset)

def preprocess():
    
    X, y = importSelfOrganizingMapDataset("Self_Organizing_Map_Credit_Card_Applications.csv")
    
    saveTrainingAndTestingDataset(X, y)
    

if __name__ == "__main__":
    preprocess()