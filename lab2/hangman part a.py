# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:41:25 2022

@author: Marry
"""


secret_word='apple'
count=0
guess=''
while count<6:   
    letters_guessed=str(input("enter lowercase letters"))
    count+=1
    guess+=letters_guessed
def is_word_guessed(secret_word, letters_guessed):
        for letter in secret_word:
            if letter not in letters_guessed:
                return False
        return True    
print(is_word_guessed(secret_word, guess))    