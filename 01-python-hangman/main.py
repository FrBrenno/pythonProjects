import os
import Body
from random import randint


WORDS = []


def load_words():
    """Loads all the words of the game in a list"""
    os.chdir("\\Users\\brenn\\Documents\\GitHub\\pythonProjects\\01-python-hangman\\")
    file_name = "words.txt"
    with open(file_name, 'r') as f:
        for w in f:
           WORDS.append(w.strip().lower())
      
    
def shuffle():
    """Shuffles the list of words"""
    for i in range(len(WORDS)):
        rd = randint(0, len(WORDS)-1)
        WORDS[i], WORDS[rd] = WORDS[rd], WORDS[i]

def menu():
    """Initial menu where the player choose to play or quit"""

    print("#"*35)
    print("  Welcome to the menu of Hangman  ")
    print("#"*35)
    print("To start the game, enter [Y]")
    print("To quit the game, enter [N]")

    while True:
        choice = input("Enter here: ").strip().lower()
        if choice == 'y':
            load_words()
            shuffle()
            print('The game has started!')
            print('Enter [-1] to quit in game.')
            game()
        elif choice == 'n':
            exit()
        else:
            print("The option does not exist. Please select one of the two options above.")


def game():
    """All the game logic is in this function. 
    First, all items are initialized, the body object, thats draws the hangman in the screen, the selected word, that is put in a set to get only once the letters of
    it and an list with the showable word. The last one is modified each time that the player answer a good letter.
    Second, all the graphics are made in prints functions.
    """
    body = Body.Body()
    guesses = []
    flag = True
    word = WORDS[randint(0, len(WORDS)-1)]
    set_word = set(word)
    correct_lst = [" _ "]*len(word)

    print("#"*16, " # ", "#"*16)
    print(" "*13, " HANGMAN ", " "*13)
    print("#"*16, " # ", "#"*16)
    
    while flag:
        print("\n")
        print('The words has {} letters.'.format(len(word)))
        body.show()    

        print(' '.join(correct_lst))

        print("Your guesses were: ",  guesses)
        letter = input('Your guess: ').strip().lower()

        body.ch_status(len(guesses))

        if letter in set_word:
            """Verify that the letter entered is in the word set, remove it from there, and two cases are available:
            this letter is multiple times in the word, so we have to get all indexes, put them in a list and replace the right element of the correct_lst with
            the correct letter. The second case is easier, we just have to put the letter in the correct place in the string.
            After all, all lists are trasncripted to string to be showed in the screen.            
            """
            set_word.remove(letter)
            if word.count(letter) !=1:
                indexes = [index for index, i in enumerate(list(word)) if i == letter]
                for i in indexes:
                    correct_lst[i] = letter
                print(' '.join(correct_lst))
            else:
                correct_lst[word.index(letter)] = letter
                print(' '.join(correct_lst))
        else:
            """If the letter is not in the word, add it to guesses list as a error."""
            guesses.append(letter)

        if body.dead_status:
            """If the player lose the game"""
            flag = False
            print('\n')
            print('\./'*35)
            print('Oh non, you lost the game!')
            body.show() 
            print(' '.join(correct_lst))
            print('\n')
            print(f"The correct word was: {word}")
            print('You are going to the menu to restart the game and try again.')
            print('\./'*35)
            print('\n')
            menu()
        elif len(set_word) == 0:
            """If the player wins the game"""
            flag = False
            print('\n')
            print('\./'*35)
            print('Oh yeah, you won the game!')
            body.show() 
            print(' '.join(correct_lst))
            print('You are going to the menu to restart the game.')
            print('\./'*35)
            print('\n')
            menu()
    


menu()




