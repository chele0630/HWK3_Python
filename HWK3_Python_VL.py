# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:42:28 2019

@author: Lucas
"""

import os
import csv

election_csv = os.path.join("C://Users//Lucas//Desktop//election_data.csv")

with open(election_csv, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
#total number of votes cast
    
#text = open("C://Users//Lucas//Desktop//election_data.csv", "r")
#myLines = text.readlines()
#numLines=len(myLines)
#print (numLines)

       
#complete list of candidates who received votes
 
def unique(candidates): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in candidates: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print (x)
      
    
  
    
#percentage of votes each candidate won
       
#total number of votes each candidate won

#winner of elecation based on popular vote
       
       
#print("Election Results")
#print("----------------------")
#print("Total Votes: ", numLines)
#print()
#print("Winner: ", winner)
       
       
        
        
