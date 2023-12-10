# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:50:39 2022

@author: Marry
"""

count=0
guess=''
warnings=3
while count<6:   
    letters_guessed=str(input("enter lowercase letters"))
    if str.isalpha(letters_guessed)==False:
        print('Oops!that is not a valid letter. You have ',warnings-1,'warnings left')
        break
    count+=1
    guess+=letters_guessed