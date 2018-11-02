from random import choice 
from WordGameController import WordGameController

class MysteryWord:
    """
    APPLICATION LAYER (MAIN LAYER)
    methods - 
    instance variables - {
        difficulty the user has selected,
        number of guesses left,
        WordList instance,
        WordGameController instance,
    }
    """
    
    def __init__(self):
        self.game_controller = WordGameController()

    def runGame(self):
        self.game_controller.reset_controller()
        self.game_controller.entire_game()
        self.playAgain()

    def playAgain(self):
        playAgain = input("Do you want to play again? (Y or N) ")
        if playAgain == "Y":
            self.runGame()
        else:
            print("Thanks for playing!")
            pass

        
    def printTest(self):
        print(self.game_controller.mystery_word)
        print(self.game_controller.guessed)
        #print(self.game_controller.available_words.hard)
        pass