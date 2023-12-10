
secret_word='apple'
count=0
guess=""
while count<6:
    letters_guessed=str(input('enter lowercase letter'))
    guess+=letters_guessed
    count+=1
def get_guessed_word(secret_word,letters_guessed):
    guessed_word=''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word+=(letter+' ')
        else:
            guessed_word+=("_"+' ')
    return guessed_word        
print (get_guessed_word(secret_word,guess))        