# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:38:28 2022

@author: Marry
"""

    
    
# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False 
    return True    


def get_guessed_word(secret_word, letters_guessed):
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
def hangman(secret_word):
    print ('''welcome to the hangman game!
    I'm thinking of a word that is ''',len(secret_word),'''letters long.''')


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
                print ('Oops, that is not a valid letter. You have ',remaining_guesses,'guesses left',get_guessed_word(secret_word, guess))
        else:
            letters_guessed=letters_guessed.lower()
            if 2*letters_guessed in guess:
                if warnings>0:
                    warnings-=1
                    print ('You have already guessed that letter. You have',warnings,'warnings left' )
                else:
                         remaining_guesses-=1
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
        




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)