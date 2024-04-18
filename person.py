#%% MODULE BEGINS
module_name = 'person'

'''
Version: <***>

Description:
    <***>

Authors:
    <***>

Date Created     :  <***>
Date Last Updated:  <***>

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
   import os
   #os.chdir("./../..")
#

#custom imports
import config

#other imports
from copy import deepcopy as dpcpy
from matplotlib import pyplot as plt
import numpy as np 
import os
import pandas as pd
import seaborn as sns

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
  "wilks_f_d": config.WILKS_F_D, "wilks_f_e": config.WILKS_F_E, "wilks_f_a": config.WILKS_F_F, "output_dir": config.output_dir}

  
  def __init__(self):
    pass

  def showHistogram(self):
    self.data.hist(figsize=(10, 6))
    plt.tight_layout()
    plt.show()
  
  def showLine(self):
    self.data.plot(kind='line', figsize=(10, 6))
    plt.show()

  def exportHistogram(self):
    self.data.hist(figsize=(10, 6))
    plt.tight_layout()
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'histogram.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def exportLine(self):
    self.data.plot(kind='line', figsize=(10, 6))
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'line.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def exportPickle(self, filename='data.pkl'):
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])
        
    pickle_file_path = os.path.join(self.CONSTANTS["output_dir"], filename)
        
    self.data.to_pickle(pickle_file_path)

    
  def searchWeightCategory(self, weightCategory):
    self.data = self.data.query(f"WeightCategory == {weightCategory}")
    return self.data.query(f"WeightCategory == {weightCategory}")



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
