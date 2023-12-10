# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:37:44 2022

@author: Marry
"""
x=int(input("plaese enter marks of 1st subject"))
y=int(input("please enter marks of 2nd subject"))
z=int(input("please enter marks of 3rd subject"))
a=(x+y+z)/3
if a>75:
    print("your average is greater than 75")
    print("you are above standard")
    print("admissiom granted")
else:
    print("admission not granted")