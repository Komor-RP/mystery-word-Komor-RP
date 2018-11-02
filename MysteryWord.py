from WordGameController import WordGameController

class MysteryWord:
    """
    APPLICATION LAYER
    Pulls together controller functions to make the program run.
    """
    
    def __init__(self):
        self.game_controller = WordGameController()

    def runGame(self):
        """
        Calls game controller functions to run the game.
        """
        self.game_controller.reset_controller()
        self.game_controller.entire_game()
        anotherPlay = self.game_controller.playAgain()

        if anotherPlay:
            self.runGame()

        
    def debugPrint(self):
        """
        Print statements used to debug.
        """
        print(self.game_controller.mystery_word)
        print(self.game_controller.guessed)
        #print(self.game_controller.available_words.hard)
        pass