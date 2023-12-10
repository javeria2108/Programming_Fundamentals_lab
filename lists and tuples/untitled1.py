# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:38:48 2022

@author: Marry
"""

def possible_combinations(list1):
    x=len(list1)
    no_of_possible_combinations=0
    possible_combinations=[]
    while no_of_possible_combinations<2**x:
        for i in list1:
             possible_combinations.append([i])
             list1.remove(i)
        no_of_possible_combinations+=1
    
        
        
        
    return possible_combinations    
list1=['orange','blue','red']
print(possible_combinations(list1))
        