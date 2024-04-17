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
        print("Drawing a Histogram...")
        lifter.showHistogram()
    elif draw_input == 'l':
        print("Drawing a Line Plot...")
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

def run_console_ui():
    lifter = None
    while True:
        file_extension = input("What type of file are you using .csv or .pkl?: ")
        file_name = input("Enter the name of the .csv file you would like to read from: ")
        if os.path.exists("INPUT/" + file_name + file_extension):
            lifter = Lifter(file_name + file_extension)
            break
        else:
            print("File not found.")

    while True:
        print("What would you like to do with '{}'? \n".format(file_name))
        print("Display Data: Enter 'V'")
        print("Show Unique Values: Enter 'U'")
        print("Generate Combinations: Enter 'G'")
        print("Generate Permutations: Enter 'P'")
        print("Calculate: Enter 'C'")
        print("Draw a Graph: Enter 'D'")
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