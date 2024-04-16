#%% MODULE BEGINS
module_name = 'person'

'''
Version: 1.0000000000000000000000000000000000000000001

Description:
    <***>

Authors:
    Team Awesome
    Cameron & Henry

Date Created     :  3/30/24
Date Last Updated:  4/16/24

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#custom imports
import config

#other imports
from   copy       import deepcopy as dpcpy
from   copy       import deepcopy as dpcpy
from   matplotlib import pyplot as plt
import numpy  as np 
import os
import pandas as pd

#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class Person:
  CONSTANTS = {"lbs_to_kg" : config.LBS_TO_KGS, "wilks_m_a": config.WILKS_M_A, "wilks_m_b": config.WILKS_M_B, "wilks_m_c": config.WILKS_M_C, "wilks_m_d": config.WILKS_M_D,
  "wilks_m_e": config.WILKS_M_E, "wilks_m_f": config.WILKS_M_F, "wilks_f_a": config.WILKS_F_A, "wilks_f_b": config.WILKS_F_B, "wilks_f_c": config.WILKS_F_C,
  "wilks_f_d": config.WILKS_F_D, "wilks_f_e": config.WILKS_F_E, "wilks_f_a": config.WILKS_F_F,}

  
  def __init__(self):
    pass

  def showHistogram(self, data):
    data.hist(figsize=(10, 6))
    plt.show()
  
  def showLine(self,data):
    data.plot(kind='line', figsize=(10, 6))
    plt.show()

  def searchWeightCategory(self, weightCategory, data=None):
    if data is None:
      data = self.data

    return data.query(f"WeightCategory == {weightCategory}")


#Function definitions Start Here
def main():
    pass
#

#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code start here



#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Self-run block
if __name__ == "__main__":
    
    print(f"\"{module_name}\" module begins.")
    
    #TEST Code
    main()
