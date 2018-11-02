from WordList import WordList


class WordGameController:
    """
    PRESENTATION LAYER
    Runs game logic and updates terminal
    """
    
    def __init__(self):
        self.available_words = WordList()
        self.guess_limit = 8
        self.diff = None
        self.mystery_word = None
        self.guessed = set()
        self.wrong = 0
        self.display = None
        self.status = None
        

    def prompt_difficulty(self):
        """
        Prompts user for difficulty and sets the cleaned variable to the instance variable
        """
        diff = input("Select your difficulty: ")
        self.diff = self.clean_input(diff)

    def entire_game(self):
        """
        Pulls together the controlller methods needed to run a game to completion.
        """
        self.prompt_difficulty()
        self.set_up_word()
        self.runGame()
        
    
    def reset_controller(self):
        """
        Resets instance variables to play another game.
        """
        self.diff = None
        self.mystery_word = None
        self.guessed = set()
        self.wrong = 0
        self.display = None
        self.status = None

    def set_up_word(self):
        """
        Instructs data layer to pull the word list.
        Gets a random word based on difficulty.
        """
        self.available_words.get_wordlist()
        if (self.diff == "EASY"): 
            self.mystery_word = self.clean_input(self.available_words.get_random_word("EASY"))
        elif (self.diff == "MEDIUM"):
            self.mystery_word = self.clean_input(self.available_words.get_random_word("MEDIUM"))
        else:
            self.mystery_word = self.clean_input(self.available_words.get_random_word("HARD"))

        self.display =  *(("_", char) for char in self.mystery_word ),
    
    def runGame(self):
        """
        Updates interface and tells the game to continue prompting responses until the game ends.
        """
        self.update_interface()
        while( self.wrong < self.guess_limit and self.status == None):
            self.prompt_guess()
        
        self.endGame(self.status)

    def playAgain(self):
        """
        Asks user if they want to play another game. Returns True or False
        """

        playAgain = input("Do you want to play again? (Y or N) ")
        if playAgain == "Y":
            return True
        else:
            return False
            print("Thanks for playing!")
            
    

    def prompt_guess(self):
        """
        Called by runGame method
        Asks for guesses and keeps on asking until it receives
        a valid input. 
        """
        try:
            guess = self.clean_input(input("Guess a letter! \n"))
            self.handle_guess(guess)
        except ValueError:
            self.prompt_guess()

    
    def handle_guess(self, guess):
        """
        Called by prompt_guess method
        This is a helper function called by prompt guess. It takes a the user guess
        and evaluates it to see if it's correct
        """
        
        if not guess.isalpha() or len(guess) > 1:
            print("Enter a single letter!")
            raise ValueError()
        elif guess in self.guessed:
            print("You have already guessed this letter.")
            raise ValueError()
        self.guessed.add(guess)

        if guess in self.mystery_word:
            print(f'Yes! "{guess}" is in the mystery word!')
        else:
            self.wrong += 1
            print(f'No! {guess} is not in the mystery word.')
            print(f'You have {self.guess_limit - self.wrong} guesses left.')

        
        self.update_interface()
        


    def update_interface(self):
        """
        Called by handle_guess method to update the interface and show the user where they are in the game.
        Also checks if there are any unfilled spots in the display, meaning the user has won, or if the user is 
        out of guesses, meaning they lost.
        """

        result = "win"
        
        for letter in self.display:
            if (letter[1] in self.guessed):
                print(letter[1], end=" ")
            else:
                result = "notwin"
                print(letter[0], end=" ")
        print("")
        
        if result == "win":
            self.status = "win"
        elif self.wrong == 8:
            self.status = "loss"


    def endGame(self, result):
        """
        Based on result argument, tells user if they won or lost
        """
        if result == "loss":
            print("You Lost.")
            print(f'The mystery word was {self.mystery_word}')
        else:
            print("You Won!")
            

    @staticmethod
    def clean_input(outside_input):
        """
        makes all inputs capital letters
        """
        all_upper = outside_input.upper()
        return all_upper