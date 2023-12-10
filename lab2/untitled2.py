# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:19:16 2022

@author: Marry
"""

count=0
guess=''
warnings=3
remaining_guesses=6
while count<6:   
    letters_guessed=str(input("enter lowercase letters"))
    if str.isalpha(letters_guessed)==False:
        warnings-=1
        if warnings>0:
            print('Oops!that is not a valid letter. You have ',warnings,'warnings left')
        if warnings<=0:
            print ('you have ',remaining_guesses-1,'guesses left')
    count+=1
    guess+=letters_guessed