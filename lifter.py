#%% MODULE BEGINS
module_name = 'lifter'

'''
Version: 1.0

Description:
    child class file

Authors:
    Team Awesome
    Henry & Cameron

Date Created     :  3/29/2024
Date Last Updated:  4/24/2024
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
import logging

#Class definitions Start Here
class Lifter(Person):

  def __init__(self, file):
    self.logger = logging.getLogger(__name__)
    self.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    self.logger.addHandler(ch)

    fh = logging.FileHandler('Log/lifter.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    self.logger.addHandler(fh)

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
    self.logger.info("Displaying data...")

    print(self.data)

  def showViolin(self):
    self.logger.info("Generating violin plot...")

    sns.violinplot(data=self.data)
    plt.show()

  def showWhisker(self):
    self.logger.info("Generating whisker plot...")

    self.data.plot(kind='box', figsize=(10, 6))
    plt.show()

  def showScatter(self, column):
    self.logger.info("Generating scatter plot for column " + column + "...")
    
    self.data.plot(kind='scatter', x='WeightCategory', y=column,  figsize=(10, 6))
    plt.show()

  def exportViolin(self):
    self.logger.info("Exporting violin plot...")

    sns.violinplot(data=self.data)
    plt.xticks(rotation=45)
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'violin.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def exportWhisker(self):
    self.logger.info("Exporting whisker plot...")

    self.data.plot(kind='box', figsize=(10, 6))
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'whisker.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def exportScatter(self, column):
    self.logger.info("Exporting scatter plot for column " + column + "...")

    self.data.plot(kind='scatter', x='WeightCategory', y=column,  figsize=(10, 6))
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'scatter.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def searchTotal(self, Total):
    self.logger.info("Searching total values for value " + Total + "...")

    self.data = self.data.query(f"Total == {Total}")
    return self.data.query(f"Total == {Total}")

  def calculateStats(self, column):
    self.logger.info("Calculating stats for column " + column + "...")

    stats = {
      'column': column,
      'mean': self.data[column].mean(),
      'median': self.data[column].median(),
      'std': self.data[column].std(),
        }
    return stats

  def showUniqueValues(self, column):
    self.logger.info("Displaying unique values for column " + column + "...")

    return self.data[column].unique()

  def generatePermutations(self, r, column):
    self.logger.info("Generating permutations for column " + column + "...")

    permutations = list(itertools.permutations(self.showUniqueValues(column), r))
    return permutations

  def generateCombinations(self, r, column):
    self.logger.info("Generating combinations for column " + column + "...")

    combinations = list(itertools.combinations(self.showUniqueValues(column), r))
    return combinations
  
  def calculateJointCounts(self, column1, column2):
    self.logger.info("Calculating joint counts for columns " + column1 + " and " + column2 + "...")

    joint_count = (self.data[column1] & self.data[column2]).sum()
    return joint_count
  
  def calculateJointProbabilities(self, column1, column2):
    self.logger.info("Calculating joint probabilities for columns " + column1 + " and " + column2 + "...")

    joint_prob = (self.data[column1] & self.data[column2]).sum() / len(self.data)
    return joint_prob
  
  def calculateConditionalProbabilities(self, column1, column2):
    self.logger.info("Calculating conditional probabilities for columns " + column1 + " and " + column2 + "...")

    prob_A = self.data[column1].sum() / len(self.data)
    prob_B = self.data[column2].sum() / len(self.data)
    joint_prob_AB = len(self.data[(self.data[column1] == 1) & (self.data[column2] == 1)]) / len(self.data)
    conditional_prob_A_given_B = joint_prob_AB / prob_B
    return conditional_prob_A_given_B