# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:05:34 2022

@author: Marry
"""

food = ["chocolate", "chicken", "corn", "sandwich",  "soup", "potatoes", "beef", "lox", "lemonade"] 
fifth = [] 
for x in food: 
    try:
      fifth.append(x[4])
    except IndexError:
        pass
print (fifth)    
