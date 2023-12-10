# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:29:59 2022

@author: Marry
"""
WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1} 
def get_frequency_dict(sequence):

    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
word=str(input('enter a word'))
word_hand=get_frequency_dict(word)
word_list = load_words()

def is_word_valid(hand,word,word_list):
    for letter in word:
        if word_hand.get(letter)>hand.get(letter):
            return False
    return word in word_list    
print (is_word_valid(hand, word,word_list))        