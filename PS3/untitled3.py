# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:04:35 2022

@author: Marry
"""

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1} 
def get_frequency_dict(sequence):

    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def display_hand(hand):
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
word=str(input('enter a word'))
word_hand=get_frequency_dict(word)
print(word_hand)
def update_hand(hand,word):
    update_key=''
    for key in hand:
        if key not in word_hand:
            if hand.get(key)>1:
                update_key+=key*hand.get(key)
            else:    
                update_key+=key   
    return get_frequency_dict(update_key)   
new_hand=update_hand(hand, word)  
print(new_hand) 
display_hand(new_hand)     