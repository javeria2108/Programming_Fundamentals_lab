# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:52:53 2022

@author: Marry
"""

import string
secret_word='apple'
print ('''welcome to the hangman game!
I'm thinking of a word that is ''',len(secret_word),'''letters long.''')
def get_guessed_word(secret_word,letters_guessed):
    guessed_word=''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word+=(letter+' ')
        else:
            guessed_word+=("_"+' ')
    return guessed_word    
def get_available_letters(letters_guessed):
      letters=string.ascii_lowercase
      for char in letters_guessed:
        letters=letters.replace(char,'')
      return letters   
def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False         
        
    return True
  
guess=''
remaining_guesses=6
warnings=3
while True:
    print ('''-------------------------
you have ''',remaining_guesses,'''guesses left
Available letters:''',get_available_letters(guess))
    letters_guessed=str(input("Please guess a letter:"))
    guess+=letters_guessed
    if str.isalpha(letters_guessed)==False:
        if warnings>0:
           warnings-=1
           print('Oops!that is not a valid letter. You have ',warnings,'warnings left',get_guessed_word(secret_word, guess))
        else:
            remaining_guesses-=1
            warnings=3
            print ('Oops, that is not a valid letter. You have ',remaining_guesses,'guesses left',get_guessed_word(secret_word, guess))
    else:
        letters_guessed=letters_guessed.lower()
        if 2*letters_guessed in guess:
            if warnings>0:
                warnings-=1
                print ('You have already guessed that letter. You have',warnings,'warnings left' )
            else:
                     remaining_guesses-=1
                     warnings=3
                     print('You have already guessed that letter. You have',remaining_guesses,'guesses left')    
        elif letters_guessed in secret_word:
            print ('Good Guess:',get_guessed_word(secret_word, guess))
        
       
        else:
            if letters_guessed in "aeiou":
                remaining_guesses-=2
            else:
                remaining_guesses-=1
            print ('oops, that letter is not in my word.',get_guessed_word(secret_word, guess))    
                
    if remaining_guesses==0:
        print ('you ran out of guesses! The word was',secret_word)
        break
    score=remaining_guesses*len(set(secret_word))
    if is_word_guessed(secret_word, guess)==True:
        print ('Congratulations! You Won . Your total score is:',score)
        break
    
   
