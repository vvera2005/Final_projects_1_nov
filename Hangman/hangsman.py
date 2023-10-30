"""This skript is hangman game"""
import random

def get_word(ml):
    "Generates the word from list"
    end = len(ml) -1
    n = random.randint(0,end)
    return ml[n]

def game(word, guesses):
    "decides if the letter is in the word"
    for letter in word:
        if letter in guesses:
            print(letter, end= " ")
        else:
            print("_", end = " ")

def play(lifes):
    "prints killing"
    kill = [        '''
           --------
           |      |
           |
           |
           |
           |
           |
          ---
        ''',
           '''
           --------
           |      |
           |      O
           |
           |
           |
           |
          ---
        ''',
          '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
           |
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |      |/
           |      |
           |
           |
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |
           |
          ---
        ''',
         '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |       \\
           |
          ---
        ''',
        ]
    print(kill[lifes])
    let = input("Enter a letter: ")
    return let

def main():
    " generates all game and functions "
    word_list = ["happy", "homeless", "man" , "fear", "crocodile" , "trust", "darling", "escape" , "fail"]
    lifes = 0
    word = get_word(word_list)
    guesses = []
    win = True
    while win:
        game(word,guesses)
        letter = play(lifes)
        guesses.append(letter)
        if letter not in word:
            lifes += 1
        if lifes >= 6:
            print('''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
           |
          ---
        ''')
            print("You lost" )
            break
        win = False
        for letter in word:
            if letter not in guesses:
                win = True
    if win is False:
        print("Congratulations!! You won")

main()

