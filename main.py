#%% MODULE BEGINS
module_name = 'main'

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
from person import Person
from lifter import Lifter

#other imports
from copy import deepcopy as dpcpy
from matplotlib import pyplot as plt
import numpy as np 
import os
import pandas as pd
import seaborn as sns

#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calculate_options():
    print("Select type of calculation: \n")
    print("Stats (Mean, Median, & Standard Deviation): Enter 'S'")
    print("Joint Count: Enter 'J'")
    print("Joint Probability: Enter 'P'")
    print("Conditional Probability: Enter 'C'")
    print("Quit: Enter 'Q'. \n")

def run_calculation(calc_input, lifter):
    if calc_input == 's':
        stats_input = input("Enter Column (Options: BodyWeight, Bench, Squat, Deadlift, Total): ").lower()
        if stats_input == 'bodyweight':
            print(lifter.calculateStats("BodyWeight"))
        elif stats_input == 'bench':
            print(lifter.calculateStats("Bench"))
        elif stats_input == 'squat':
            print(lifter.calculateStats("Squat"))
        elif stats_input == 'deadlift':
            print(lifter.calculateStats("Deadlift"))
        elif stats_input == 'total':
            print(lifter.calculateStats("Total"))
        else:
            print("Invalid option.")
    elif calc_input == 'j':
        print("Calculating Joint Count...")
    elif calc_input == 'p':
        print("Calculating Joint Probability...")
    elif calc_input == 'c':
        print("Calculating Conditional Probability...")
    else:
        print("Invalid option.")

def draw_options():
    print("Select type of graph: \n")
    print("Histogram: Enter 'H'")
    print("Line Plot: Enter 'L'")
    print("Violin Plot: Enter 'V'")
    print("Whisker-Box Plot: Enter 'W'")
    print("Scatter Plot: Enter 'S'")
    print("Quit: Enter 'Q'. \n")

def run_drawing(draw_input, lifter):
    if draw_input == 'h':
        lifter.showHistogram()
    elif draw_input == 'l':
        lifter.showLine()
    elif draw_input == 'v':
        lifter.showViolin()
    elif draw_input == 'w':
        lifter.showWhisker()
    elif draw_input == 's':
        scatter_input = input("Enter Column (Options: BodyWeight, Bench, Squat, Deadlift, Total): ").lower()
        if scatter_input == 'bodyweight':
            print(lifter.showScatter("BodyWeight"))
        elif scatter_input == 'bench':
            print(lifter.showScatter("Bench"))
        elif scatter_input == 'squat':
            print(lifter.showScatter("Squat"))
        elif scatter_input == 'deadlift':
            print(lifter.showScatter("Deadlift"))
        elif scatter_input == 'total':
            print(lifter.showScatter("Total"))
        else:
            print("Invalid option.")
    else:
        print("Invalid option.")

def export_options():
    print("Select what you would like to Export: \n")
    print("Histogram: Enter 'H'")
    print("Line Plot: Enter 'L'")
    print("Violin Plot: Enter 'V'")
    print("Whisker-Box Plot: Enter 'W'")
    print("Scatter Plot: Enter 'S'")
    print("Quit: Enter 'Q'. \n")

def run_export(export_input, lifter):
    if export_input == 'h':
        lifter.exportHistogram()
    elif export_input == 'l':
        lifter.exportLine()
    elif export_input == 'v':
        lifter.exportViolin()
    elif export_input == 'w':
        lifter.exportWhisker()
    elif export_input == 's':
        scatterex_input = input("Enter Column (Options: BodyWeight, Bench, Squat, Deadlift, Total): ").lower()
        if scatterex_input == 'bodyweight':
            print(lifter.exportScatter("BodyWeight"))
        elif scatterex_input == 'bench':
            print(lifter.exportScatter("Bench"))
        elif scatterex_input == 'squat':
            print(lifter.exportScatter("Squat"))
        elif scatterex_input == 'deadlift':
            print(lifter.exportScatter("Deadlift"))
        elif scatterex_input == 'total':
            print(lifter.exportScatter("Total"))
        else:
            print("Invalid option.")
    else:
        print("Invalid option.")

def run_console_ui():
    lifter = None
    while True:
        file_extension = input("What type of file are you using? '.csv' or '.pkl': ")
        file_name = input("Enter the name of the file you would like to read from: ")
        if os.path.exists("INPUT/" + file_name + file_extension):
            lifter = Lifter(file_name + file_extension)
            break
        else:
            print("File not found.")

    while True:
        print("What would you like to do with '{}'? \n".format(file_name + file_extension))
        print("Display Data: Enter 'V'")
        print("Show Unique Values: Enter 'U'")
        print("Search by Weight Category: Enter 'W'")
        print("Search by Total: Enter 'T'")
        print("Generate Combinations: Enter 'G'")
        print("Generate Permutations: Enter 'P'")
        print("Calculate: Enter 'C'")
        print("Draw a Graph: Enter 'D'")
        print("Export a Graph to the Output Folder: Enter 'X'")
        print("Export Pickle File: Enter 'K'")
        print("Quit: Enter 'Q'. \n")

        user_input = input("Enter Letter: ").lower()

        if user_input == 'v':
            while True:
                print(lifter.showData())
                break

        elif user_input == 'u':
            while True:
                unique_input = input("Enter Column (Options: BodyWeight, Bench, Squat, Deadlift, Total): ").lower()
                if unique_input == 'bodyweight':
                    print(lifter.showUniqueValues("BodyWeight"))
                elif unique_input == 'bench':
                    print(lifter.showUniqueValues("Bench"))
                elif unique_input == 'squat':
                    print(lifter.showUniqueValues("Squat"))
                elif unique_input == 'deadlift':
                    print(lifter.showUniqueValues("Deadlift"))
                elif unique_input == 'total':
                    print(lifter.showUniqueValues("Total"))
                else:
                    print("Invalid option.")
                break

        elif user_input == 'w':
            while True:
                weightCategory_input = input("Enter Weight Category (Options: 97, 105, 114, 123, 132, 148, 165, 181): ")
                if weightCategory_input == '97':
                    print(lifter.searchWeightCategory("97"))
                elif weightCategory_input == '105':
                    print(lifter.searchWeightCategory("105"))
                elif weightCategory_input == '114':
                    print(lifter.searchWeightCategory("114"))
                elif weightCategory_input == '123':
                    print(lifter.searchWeightCategory("123"))
                elif weightCategory_input == '132':
                    print(lifter.searchWeightCategory("132"))
                elif weightCategory_input == '148':
                    print(lifter.searchWeightCategory("148"))
                elif weightCategory_input == '165':
                    print(lifter.searchWeightCategory("165"))
                elif weightCategory_input == '181':
                    print(lifter.searchWeightCategory("181"))
                else:
                    print("Invalid option.")
                break

        elif user_input == 't':
            while True:
                searchTotal_input = input("Enter a number: ")
                print(lifter.searchTotal(searchTotal_input))
                break

        elif user_input == 'g':
            while True:
                combinations_input = input("Enter Column (Options: BodyWeight, Bench, Squat, Deadlift, Total): ").lower()
                if combinations_input == 'bodyweight':
                    print(lifter.generateCombinations(3,"BodyWeight"))
                elif combinations_input == 'bench':
                    print(lifter.generateCombinations(3,"Bench"))
                elif combinations_input == 'squat':
                    print(lifter.generateCombinations(3,"Squat"))
                elif combinations_input == 'deadlift':
                    print(lifter.generateCombinations(3,"Deadlift"))
                elif combinations_input == 'total':
                    print(lifter.generateCombinations(3,"Total"))
                else:
                    print("Invalid option.")
                break

        elif user_input == 'p':
            while True:
                permutations_input = input("Enter Column (Options: BodyWeight, Bench, Squat, Deadlift, Total): ").lower()
                if permutations_input == 'bodyweight':
                    print(lifter.generatePermutations(3,"BodyWeight"))
                elif permutations_input == 'bench':
                    print(lifter.generatePermutations(3,"Bench"))
                elif permutations_input == 'squat':
                    print(lifter.generatePermutations(3,"Squat"))
                elif permutations_input == 'deadlift':
                    print(lifter.generatePermutations(3,"Deadlift"))
                elif permutations_input == 'total':
                    print(lifter.generatePermutations(3,"Total"))
                else:
                    print("Invalid option.")
                break

        elif user_input == 'c':
            while True:
                calculate_options()
                calc_input = input("Enter Letter: ").lower()
                if calc_input == 'q':
                    break
                run_calculation(calc_input, lifter)

        elif user_input == 'd':
            while True:
                draw_options()
                draw_input = input("Enter Letter: ").lower()
                if draw_input == 'q':
                    break
                run_drawing(draw_input, lifter)

        elif user_input == 'x':
            while True:
                export_options()
                export_input = input("Enter Letter: ").lower()
                if export_input == 'q':
                    break
                run_export(export_input, lifter)

        elif user_input == 'k':
            while True:
                print(lifter.exportPickle())
                break

        elif user_input == 'q':
            break

        else:
            print("Invalid option. Please try again.")

    return lifter

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here



#Function definitions Start Here
def main():
    run_console_ui()

#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code start here



#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Self-run block
if __name__ == "__main__":
    
    print(f"\"{module_name}\" module begins.")
    
    #TEST Code
    main()