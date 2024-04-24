#%% MODULE BEGINS
module_name = 'main'

'''
Version: 1.0

Description:
    main file

Authors:
    Team Awesome
    Henry & Cameron

Date Created     :  <***>
Date Last Updated:  4/24/2024

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#custom imports
import config
from person import Person
from lifter import Lifter

#other imports
from copy import deepcopy as dpcpy
from matplotlib import pyplot as plt
import numpy as np 
import os
import pandas as pd
import seaborn as sns
import logging

#Function definitions Start Here
def main():
    #put all testing code here

    lifter = Lifter("data.csv")

    print(lifter.showData())
    print(lifter.calculateStats("Total"))

    """
    lifter.exportCSV()
    print(lifter.calculateJointCounts("Total", "WeightCategory"))
    print(lifter.calculateJointProbabilities("Total", "WeightCategory"))
    print(lifter.calculateConditionalProbabilities("Total", "WeightCategory"))
    """

#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Self-run block
if __name__ == "__main__":
    
    print(f"\"{module_name}\" module begins.")
    
    #TEST Code
    main()