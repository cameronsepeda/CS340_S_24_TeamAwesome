#%% MODULE BEGINS
module_name = 'person'

'''
Version: 1.0

Description:
    parent class file

Authors:
    Team Awesome
    Henry & Cameron

Date Created     :  3/29/2024
Date Last Updated:  4/24/2024
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#custom imports
import config

#other imports
from copy import deepcopy as dpcpy
from matplotlib import pyplot as plt
import numpy as np 
import os
import pandas as pd
import seaborn as sns
import logging

#Class definitions Start Here
class Person:
  CONSTANTS = {"lbs_to_kg" : config.LBS_TO_KGS, "wilks_m_a": config.WILKS_M_A, "wilks_m_b": config.WILKS_M_B, "wilks_m_c": config.WILKS_M_C, "wilks_m_d": config.WILKS_M_D,
  "wilks_m_e": config.WILKS_M_E, "wilks_m_f": config.WILKS_M_F, "wilks_f_a": config.WILKS_F_A, "wilks_f_b": config.WILKS_F_B, "wilks_f_c": config.WILKS_F_C,
  "wilks_f_d": config.WILKS_F_D, "wilks_f_e": config.WILKS_F_E, "wilks_f_a": config.WILKS_F_F, "output_dir": config.output_dir}

  def __init__(self):
    self.logger = logging.getLogger(__name__)
    self.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    self.logger.addHandler(ch)

    fh = logging.FileHandler('Log/person.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    self.logger.addHandler(fh)

  def showHistogram(self):
    self.logger.info("Generating histogram plot...")

    self.data.hist(figsize=(10, 6))
    plt.tight_layout()
    plt.show()
  
  def showLine(self):
    self.logger.info("Generating line plot...")

    self.data.plot(kind='line', figsize=(10, 6))
    plt.show()

  def exportHistogram(self):
    self.logger.info("Exporting histogram plot...")

    self.data.hist(figsize=(10, 6))
    plt.tight_layout()
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'histogram.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def exportLine(self):
    self.logger.info("Exporting line plot...")

    self.data.plot(kind='line', figsize=(10, 6))
    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])

    plt.savefig(os.path.join(self.CONSTANTS["output_dir"], 'line.png'), dpi=300, bbox_inches='tight')
    plt.close()

  def exportPickle(self, filename='data.pkl'):
    self.logger.info("Exporting pickle file...")

    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])
        
    pickle_file_path = os.path.join(self.CONSTANTS["output_dir"], filename)  
    self.data.to_pickle(pickle_file_path)

  def exportCSV(self, filename='data.csv'):
    self.logger.info("Exporting csv file...")

    if not os.path.exists(self.CONSTANTS["output_dir"]):
      os.makedirs(self.CONSTANTS["output_dir"])
        
    csv_file_path = os.path.join(self.CONSTANTS["output_dir"], filename)
        
    self.data.to_csv(csv_file_path)

  def searchWeightCategory(self, weightCategory):
    self.logger.info("Searching weight categories...")

    self.data = self.data.query(f"WeightCategory == {weightCategory}")
    return self.data.query(f"WeightCategory == {weightCategory}")