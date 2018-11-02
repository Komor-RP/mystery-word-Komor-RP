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

    
    def setupGame(self):
        self.game_controller.prompt_difficulty()
        self.game_controller.set_up_word()
    
    def runGame(self):
        self.game_controller.runGame()
        
    def printTest(self):
        print(self.game_controller.mystery_word)
        print(self.game_controller.guessed)
        #print(self.game_controller.available_words.hard)
        pass
        

hangman = MysteryWord()
hangman.setupGame()
hangman.runGame()
#hangman.printTest()




        






