# -*- coding: utf-8 -*-
"""
Filename: Popular Baby Names Analysis - Generate Dataset

File Purpose: Combine data files for each year into one large dataset for analysis.

@author: Payal Patel 

Inputs: 
    - Yearly text files of most popular baby names
    - Text files of most popular baby names by state 
    
Outputs: 4 datasets - 
    1) popularBabyNames_National.csv - popular baby names across the US from 1880 - 2019
    2) popularBabyNames_State.csv - popular baby names by state from 1910 - 2019
    3) popularBabyNames_State_Transformed.csv - transforms #2 into wide dataset (column per state)
    4) popularBabyNames.csv - combines National dataset and State dataset, for single dataset containing most popular baby names 

"""

#####################################################################
### Import Libraries ###
import numpy as np
import pandas as pd
import os
import sys

#####################################################################

#####################################################################
### Change Working Directory ###
os.chdir('C:/Users/19197/Desktop/github/Tableau/popular-baby-names/names-national')

#####################################################################

#####################################################################
### Create National Baby Names Dataset ###
directory = 'C:/Users/19197/Desktop/github/Tableau/popular-baby-names/names-national'
popularBabyNames_National = pd.DataFrame(columns = ['Name', 'Gender', 'Frequency']) 

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        df = pd.read_csv(filename, names = ['Name', 'Gender', 'Frequency'])
        #df['Filename'] = filename
        df['Year'] = filename[3:-4]
        popularBabyNames_National = popularBabyNames_National.append(df)
    else:
        continue 

#####################################################################
    
#####################################################################
### Change Working Directory ###
os.chdir('C:/Users/19197/Desktop/github/Tableau/popular-baby-names/namesbystate')

#####################################################################
    
#####################################################################
### Create State Baby Names Dataset ###   
directory = 'C:/Users/19197/Desktop/github/Tableau/popular-baby-names/namesbystate'
popularBabyNames_State = pd.DataFrame(columns = ['State', 'Gender', 'Year', 'Name', 'State Frequency']) 

for filename in os.listdir(directory):
    if filename.endswith(".TXT"):
        df = pd.read_csv(filename, names = ['State', 'Gender', 'Year', 'Name', 'State Frequency'])
        popularBabyNames_State = popularBabyNames_State.append(df)
    else:
        continue    
    
#####################################################################    
    
#####################################################################
### Merge State Baby Names Dataset with National Baby Names Dataset ###           
popularBabyNames_State_Transformed = popularBabyNames_State.set_index(['Year', 'Name', 'Gender','State']).unstack(['State'])

popularBabyNames_State_Transformed = popularBabyNames_State_Transformed.fillna(0)
    
popularBabyNames_State_Transformed= popularBabyNames_State_Transformed.reset_index()

popularBabyNames = pd.merge(popularBabyNames_National.astype(str), popularBabyNames_State_Transformed.astype(str), how= 'outer', on = ['Year','Name', 'Gender'])
#####################################################################


#####################################################################
### Write datasets to CSV Files ###   
os.chdir('C:/Users/19197/Desktop/github/Tableau/popular-baby-names/')

popularBabyNames_National.to_csv('popularBabyNames_National.csv')
popularBabyNames_State.to_csv('popularBabyNames_State.csv')
popularBabyNames_State_Transformed.to_csv('popularBabyNames_State_Transformed.csv')
popularBabyNames.to_csv('popularBabyNames.csv')

#####################################################################



    