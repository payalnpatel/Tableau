# -*- coding: utf-8 -*-
"""
Filename: Viz for Social Good Community Analysis - Generate Dataset

File Purpose: 

@author: Payal Patel 

Inputs: 
    - Viz for Social Good Annual Poll (Responses) Raw Unpivoted.xlsx dataset
    
Outputs: 1 dataset - 
    - vfsg_dataset.xlx 

"""

#####################################################################
### Import Libraries ###
import numpy as np
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
#####################################################################

#####################################################################
### Change Working Directory ###
os.chdir('C:/Users/19197/Desktop/github/Tableau/Viz-for-Social-Good-Community')

#####################################################################

#####################################################################
### Import Dataset ###
vfsg_dataset = pd.read_excel('Viz for Social Good Annual Poll (Responses) Raw Unpivoted.xlsx')
vfsg_dataset.head()
#####################################################################

#####################################################################
### EDA ###
vfsg_dataset.info()
vfsg_dataset.columns

#####################################################################

#####################################################################
### Feature Generation - "What program(s) do you use to create visualizations?" ###

## Create New Feature - # of programs used by volunteer ##
     
vfsg_dataset['What program(s) do you use to create data visualizations?'] = vfsg_dataset['What program(s) do you use to create data visualizations?'].replace('(Pen, paper, etc)', 'Pen/paper/etc', regex=True)
vfsg_dataset['What program(s) do you use to create data visualizations?'] = vfsg_dataset['What program(s) do you use to create data visualizations?'].replace(' or ', ',', regex=True)
vfsg_dataset['# of Programs Used'] = vfsg_dataset['What program(s) do you use to create data visualizations?'].astype('str').apply(lambda x: x.count(",") + 1)
   
# vfsg_dataset['# of Programs Used'][211]  
# vfsg_dataset['What program(s) do you use to create data visualizations?'][223]
# vfsg_dataset['# of Programs Used'][223]


## Create New Features for products used ##

# create columns of different programs used by volunteers
for index,row in vfsg_dataset.iterrows():
#    print(row)
#    print(index)
    programs_list = vfsg_dataset['What program(s) do you use to create data visualizations?'][index]
    programs_list = str(programs_list).split(",")
    programs_list = [x.strip() for x in programs_list]
    for program in programs_list:
        if program not in vfsg_dataset.columns:            
            vfsg_dataset[program] = ''

# update products used columns based on user response 
for index,row in vfsg_dataset.iterrows():
    programs_list = vfsg_dataset['What program(s) do you use to create data visualizations?'][index]
    programs_list = str(programs_list).split(",")
    programs_list = [x.strip() for x in programs_list]
    for program in programs_list:
        if program in vfsg_dataset.columns:
            vfsg_dataset[program][index] = 1
            

#####################################################################


#####################################################################
### Feature Generation - "How do you prefer to work on VFSG projects?" ###

vfsg_dataset['How do you prefer to work on VFSG projects?']


vfsg_dataset['How do you prefer to work on VFSG projects?'][100]


# create columns of different preferences 
for index,row in vfsg_dataset.iterrows():
#    print(row)
#    print(index)
    pref_list = vfsg_dataset['How do you prefer to work on VFSG projects?'][index]
    pref_list = str(pref_list).split(",")
    pref_list = [x.strip() for x in pref_list]
    for preference in pref_list:
        if preference not in vfsg_dataset.columns:            
            vfsg_dataset[preference] = ''

# update products used columns based on user response 
for index,row in vfsg_dataset.iterrows():
    pref_list = vfsg_dataset['How do you prefer to work on VFSG projects?'][index]
    pref_list = str(pref_list).split(",")
    pref_list = [x.strip() for x in pref_list]
    for preference in pref_list:
        if preference in vfsg_dataset.columns:
            vfsg_dataset[preference][index] = 1
            
#####################################################################
            

vfsg_dataset.to_excel('vfsg_dataset.xlsx')

#####################################################################






