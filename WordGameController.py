import re
from random import choice
from WordList import *


class WordGameController:
    """
    PRESENTATION LAYER
    methods - 
    instance variables - {
        wordlist
    }

    """
    def __init__(self):
        self.available_words = WordList()
        self.guess_limit = 8
        self.diff = None
        self.mystery_word = None
        self.guessed = set()
        self.wrong = 0
        self.display = None
        

    def prompt_difficulty(self):
        diff = input("Select your difficulty: ")
        self.diff = self.clean_input(diff)
    
    def set_up_word(self):
        self.available_words.get_wordlist()
        if (self.diff == "EASY"): 
            self.mystery_word = choice(self.available_words.easy)
        elif (self.diff == "MEDIUM"):
            self.mystery_word = choice(self.available_words.medium)
        else:
            self.mystery_word = choice(self.available_words.hard)

        self.display =  *(("_", char) for char in self.mystery_word ),
        
    def runGame(self):
        self.update_interface()
        while( self.wrong < self.guess_limit):
            self.prompt_guess()

        self.endGame()


    def prompt_guess(self):
        """
        Asks for guesses and keeps on asking until it receives
        a valid input. 
        """
        try:
            guess = input("Guess a letter! \n")     
            self.handle_guess(guess)
        except ValueError:
            print("Enter a single letter!")
            self.prompt_guess()

    
    def handle_guess(self, guess):
        """
        This is a helper function called by prompt guess. It takes a the user guess
        and evaluates it to see if it's correct
        """
        
        if not guess.isalpha() or len(guess) > 1:
            raise ValueError("Your guess is not valid")
        self.guessed.add(guess)

        if guess in self.mystery_word:
            print(f'Yes! "{guess}" is in the mystery word!')
        else:
            self.wrong += 1
            print(f'No! {guess} is not in the mystery word.')

        self.update_interface()


    def update_interface(self):
        for letter in self.display:
            if (letter[1] in self.guessed):
                print(letter[1], end=" ")
            else:
                print(letter[0], end=" ")
        print("")


    def endGame(self):
        if self.wrong == 8:
            print("You Lost.")
        else:
            print("You Won!")

        playAgain = input("Do you want to play again? (Y or N) ")
        
        if playAgain == "yes" 

        

    @staticmethod
    def clean_input(user_input):
        """
        makes all inputs capital letters
        NOT IMPLEMENTED YET - THROWS ERROR IF INPUT WON'T WORK
        """
        all_upper = user_input.upper()
        return all_upper