#%% MODULE BEGINS
module_name = 'lifter'

'''
Version: 1.0

Description:
    child class file

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
from person import Person

#other imports
from copy import deepcopy as dpcpy
from matplotlib import pyplot as plt
import numpy as np 
import os
import pandas as pd
import seaborn as sns
import itertools

#Class definitions Start Here
class Lifter(Person):

  def __init__(self, file):
    file_extension = os.path.splitext(file)[1]
    input_dir = "INPUT"
    file_path = os.path.join(input_dir, file)
        
    if file_extension == '.csv':
      self.data = pd.read_csv(file_path)
    elif file_extension == '.pkl':
      self.data = pd.read_pickle(file_path)
    else:
      print("File not supported")

  # def read_csv(self):
  #   return self.data

  def showData(self):
    print(self.data)

  def showViolin(self):
    sns.violinplot(data=self.data)
    plt.show()

  def showWhisker(self):
    self.data.plot(kind='box', figsize=(10, 6))
    plt.show()

  def showScatter(self, column):
    self.data.plot(kind='scatter', x='WeightCategory', y=column,  figsize=(10, 6))
    plt.show()

  def exportViolin(self):
    sns.violinplot(data=self.data)
    plt.xticks(rotation=45)
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'violin.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def exportWhisker(self):
    self.data.plot(kind='box', figsize=(10, 6))
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'whisker.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def exportScatter(self, column):
    self.data.plot(kind='scatter', x='WeightCategory', y=column,  figsize=(10, 6))
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'scatter.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def searchTotal(self, Total):
    self.data = self.data.query(f"Total == {Total}")
    return self.data.query(f"Total == {Total}")

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