# -*- coding: utf-8 -*-
"""
Filename: Popular Baby Names Analysis - Generate Dataset

File Purpose: Combine data files for each year into one large dataset for analysis.

@author: Payal Patel 

Inputs: Yearly text files of most popular baby names, text files of most popular baby names by state 
    
Outputs: 
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
popularBabyNames_National = pd.DataFrame(columns = ['Name', 'Gender', 'Frequency', 'Filename']) 

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        df = pd.read_csv(filename, names = ['Name', 'Gender', 'Frequency'])
        df['Filename'] = filename
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
### In Progress
pvt = pd.pivot_table(popularBabyNames_State, index = ['Year','Name', 'Gender'],
                     columns='State',
                     values='State Frequency', aggfunc='sum', fill_value=0)

test = pd.merge(popularBabyNames_National, pvt, how= 'outer', on = ['Year','Name', 'Gender'])
#####################################################################


#####################################################################
### Write datasets to CSV Files ###   
os.chdir('C:/Users/19197/Desktop/github/Tableau/popular-baby-names/')

popularBabyNames_National.to_csv('popularBabyNames_National.csv')
popularBabyNames_State.to_csv('popularBabyNames_State.csv')
test.to_csv('test.csv')

#####################################################################



    