# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:21:49 2022

@author: Marry
"""

class students(object):
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
a=students('john',18,'A')    
print (a.name)    
print (a.age)
print (a.grade)