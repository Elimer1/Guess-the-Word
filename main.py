# word = input("Enter Word: ")
# word = [word,["-" for letter in word]]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
word = "hello"
hidden_word = ["-","-","-","-","-"] 
guesses = 5

def update_word(word,hidden_word,letter):
    """function updates if new letter was guessed and print the up to date hidden word"""
    letter_occurence = word.count(letter)
    temp = 0
    while letter_occurence:
        letter_index = word.index(letter,temp)
        hidden_word[letter_index] = letter.title()
        temp = letter_index + 1
        letter_occurence -= 1

def update_letters(letters,letter):
    """fucntion makes any slected letter red"""
    letters[letters.index(letter.title())] = f"\033[31m{letter.title()}\033[0m"
    return 

def decrement_guesses():
    global guesses
    guesses -= 1

def     

decrement_guesses()
print(guesses)

# update_word(word,hidden_word,"l")
# print(hidden_word)