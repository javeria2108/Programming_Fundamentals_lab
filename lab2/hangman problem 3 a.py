# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:41:14 2022

@author: Marry
"""
import string
secret_word='apple'
print ('''welcome to the hangman game!
       I'm thinking of a word that is ''',len(secret_word),'''letters long.
       You have 6 guesses left
       available letters=''',string.ascii_lowercase)