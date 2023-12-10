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
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE 
    for i in secret_word:
        if i not in letters_guessed:
            return False         
        
    return True
 



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ""
    for i in secret_word:
        if i in letters_guessed:
             available_letters += i
        else:
            available_letters += "_" + " "
    return available_letters

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    s = string.ascii_lowercase
    print (s)
    alphabets = str(s)
    a = ""
    for i in alphabets:
        if i not in letters_guessed:
           a += i 
    return(a)
    
    def hangman(secret_word):
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secret_word), "letters long.")
    num_guesses = 6
    warnings = 3
    
    letters_guessed = ""
    
    while True :
        score = (num_guesses) * len(set(secret_word))
        print('------------')
        print('You have',  num_guesses , 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = input(str("plz guess a letter :"))
        print(secret_word)     
        
    
        
        if len(guess) > 1:
            print ("your length of guess is greater than one plz enter a guess of length 1")
        if  not guess.isalpha():
            
            if warnings > 0:
                warnings -= 1
                print('Oops! That is not a valid letter. You have ' + str(warnings) + ' warnings left: ' + get_guessed_word(secret_word, letters_guessed))
            else:
                num_guesses -= 1
                print('Oops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess:' + (get_guessed_word(secret_word, letters_guessed)))
        else:   
            guess = guess.lower()
            if guess in letters_guessed:
                if warnings  > 0:
                   warnings = warnings - 1
                   print("Oops! You've already guessed that letter and you have remaining " + str(warnings) + "warnings left :" + get_guessed_word(secret_word, letters_guessed))
                else:
                    num_guesses -=1 
                    print(("Oops! You've already guessed that letter and you have remaining " + str(num_guesses) +"guesses left :" + get_guessed_word(secret_word, letters_guessed)))
            else:
                
                if guess in secret_word:
                 letters_guessed += guess
                 print('Good guess:' + get_guessed_word(secret_word, letters_guessed))
                else:
                    if guess in 'aeiou':
                     num_guesses -= 2
                    else:
                     num_guesses -= 1
                    print('Ops! that letter is not in my secret word:' + get_guessed_word(secret_word, letters_guessed))
        if num_guesses == 0:
            print("Sorry , You have ran out of guesses .The word was " + secret_word + ".")
            break  
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You've won!")
            print("Your total score for this game is :" + str(score))
            break
            
            def match_with_gaps(my_word, other_word):
    without_space = my_word.replace(" ", "")
    
    for i in range(0, len(without_space.strip())):
        if len(without_space) != len(other_word):
            return False
        if without_space[i] == other_word[i] :
            
            continue
        if  without_space[i] == "_":
            continue
        else :
            return False
    return True



def show_possible_matches(my_word):
     words_matched = ""
     
     for item in range(len(wordlist)):
         other_word = wordlist[item]
         if match_with_gaps(my_word, other_word) == True:
            words_matched += other_word + " "
     return words_matched
         
     if len(words_matched) < 0:
             
          print('No matches found') 

def hangman_with_hints(secret_word):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secret_word), "letters long.")
    num_guesses = 6
    warnings = 3

    
    letters_guessed = ""
    
    while True :
        score = (num_guesses) * len(set(secret_word))
        print('------------')
        print('You have',  num_guesses , 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = input(str("plz guess a letter :"))
    
        
    
        
        if len(guess) > 1:
            print ("your length of guess is greater than one. plz enter a guess of length of 1")
        if guess == "*" :
            print(' Possible word matches are :', show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        else:
            if not guess.isalpha():
            
                if warnings > 0:
                    warnings -= 1
                    print('Oops! That is not a valid letter. You have ' + str(warnings) + ' warnings left: ' + get_guessed_word(secret_word, letters_guessed))
                else:
                    num_guesses -= 1
                    print('Oops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess:' + (get_guessed_word(secret_word, letters_guessed)))
            else:   
                guess = guess.lower()
                if guess in letters_guessed:
                    if warnings  > 0:
                       warnings = warnings - 1
                       print("Oops! You've already guessed that letter and you have remaining " + str(warnings) + "warnings left :" + get_guessed_word(secret_word, letters_guessed))
                    else:
                         num_guesses -=1 
                         print(("Oops! You've already guessed that letter and you have remaining " + str(num_guesses) +"guesses left :" + get_guessed_word(secret_word, letters_guessed)))
                else:
                
                    if guess in secret_word:
                     letters_guessed += guess
                     print('Good guess:' + get_guessed_word(secret_word, letters_guessed))
                    else:
                        if guess in 'aeiou':
                         num_guesses -= 2
                        else:
                         num_guesses -= 1
                        print('Ops! that letter is not in my secret word:' + get_guessed_word(secret_word, letters_guessed))
        if num_guesses <= 0:
            print("Sorry , You have ran out of guesses . Try next time. The word was " + secret_word + ".")
            break  
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You've won!")
            print("Your total score for this game is :" + str(score))
            break
    
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":


    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)



         