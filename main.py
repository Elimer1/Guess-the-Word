import random

def print_display():
    print("".join(hidden_word))
    print("Remaining Letters")
    print(" ".join(letters[:13]))
    print(" ".join(letters[13:]))
    print()
    print(f"Remaining Guesses: {guesses}")

def get_input():
    global guess
    while True:
        guess = input("Enter a letter to guess: ")    
        if guess.title() not in letters:
            print("Invalid Input!")    
        else:
            return guess.title() 
        
def guessed_the_letter():
    return guess in word      

def update_hidden_word(word, hidden_word, letter):
    """function updates if new letter was guessed and print the up to date hidden word"""
    letter_occurence = word.count(letter)
    temp = 0
    while letter_occurence:
        letter_index = word.index(letter, temp)
        hidden_word[letter_index] = letter
        temp = letter_index + 1
        letter_occurence -= 1

def guessed_the_word():
    return "".join(hidden_word) == word  
        

def update_letters(letters, letter):
    """fucntion makes any selected letter red"""
    letters[letters.index(letter)] = f"\033[31m{letter}\033[0m"
    return 

word_bank = [
    "PYTHON", 
    "NETWORK", 
    "SOFTWARE", 
    "REGISTER", 
    "BASEBALL", 
    "ESPRESSO", 
    "TERMINAL", 
    "STRUCTURE", 
    "ALGORITHM", 
    "INFRASTRUCTURE"
]    

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = word_bank[random.randint(0,9)]
hidden_word = ["-" for i in range(len(word))]
guesses = 5

while guesses:
    print_display()

    guess = get_input()

    if guessed_the_letter():
        update_hidden_word(word,hidden_word,guess)
        print("Correct")

        if guessed_the_word():
            print("Congratulations! YOU WON")
            exit()
    else:
        print("Incorrect")
        guesses -= 1

    update_letters(letters,guess) 

print("You Lost")    
print(f"The word was {word}")