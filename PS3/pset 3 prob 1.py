# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:59:55 2022

@author: Marry
"""




SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
n=6
word=str(input('enter a word'))
word_len=len(word)
def get_word_score():
    first_component=0
    for letter in word:
        first_component+=SCRABBLE_LETTER_VALUES[letter]
    second_component=(7*word_len)-3*(n-word_len)   
    if second_component>1:
        score=first_component*second_component
    else:
        score=first_component*1
    return score    
print (get_word_score())
    

    
    