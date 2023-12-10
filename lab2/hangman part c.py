# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:56:02 2022

@author: Marry
"""
import string
print (string.ascii_lowercase)
count=0
guess=''
while count<6:
    letters_guessed=str(input('enter lowercase letter'))
    guess+=letters_guessed
    count+=1
def get_available_letters(letters_guessed):
      for char in letters_guessed:
        string.ascii_lowercase=string.ascii_lowercase.replace(char,'')
      return string.ascii_lowercase
print(get_available_letters(guess))    