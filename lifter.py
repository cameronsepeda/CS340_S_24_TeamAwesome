#%% MODULE BEGINS
module_name = 'lifter'

'''
Version:  1.0000000000000000000000000000000000000000001


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
from person import Person

#other imports
from   copy       import deepcopy as dpcpy
from   matplotlib import pyplot as plt
import numpy  as np 
import seaborn as sns
import os
import pandas as pd
import itertools

#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class Lifter(Person):


  def __init__(self, file):
    self.data = pd.read_csv(file)

  def read_csv(self):
    return self.data

  def showViolin(self, data = None):
    if data is None:
      data = self.data

    sns.violinplot(data=data)
    plt.show()

  def showWhisker(self, data = None):
    if data is None:
      data = self.data

    self.data.plot(kind='box', figsize=(10, 6))
    plt.show()

  def showScatter(self, data = None):
    if data is None:
      data = self.data

    data.plot(kind='scatter', x='WeightCategory', y='Total', figsize=(10, 6))
    plt.show()

  def searchBench(self, Bench, data = None):
    if data is None:
      data = self.data

    return data.query(f"Bench == {Bench}")

  def calculateStats(self, column):
    stats = {
      'column': column,
      'mean': self.data[column].mean(),
      'median': self.data[column].median(),
      'std': self.data[column].std(),
        }
    return stats

  def showUniqueValues(self, column):
    return self.data[column].unique()

  def generatePermutations(self,r, column):
    permutations = list(itertools.permutations(self.showUniqueValues(column), r))
    return permutations

  def generateCombinations(self, r, column):
    combinations = list(itertools.combinations(self.showUniqueValues(column), r))
    return combinations


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
