secret_word="banana"
count=0
while count>7:
        letters_guessed=str( input("enter lowercase letters"))
        count=count+1

def is_word_guessed(secret_word, letters_guessed):
    for secret_word in letters_guessed:
        return True         
        
print(is_word_guessed(secret_word, letters_guessed))    
