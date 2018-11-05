from WordList import WordList


class WordGameController:
    """
    PRESENTATION LAYER
    Runs game logic and updates terminal prints
    """
    
    def __init__(self):
        self.available_words = WordList()
        self.guess_limit = None
        self.guessed = set()
        self.wrong = 0
        self.display = None
        self.status = None
        

    def entire_game(self):
        """
        Pulls together the controlller methods needed to run a game to completion.
        """
        self.set_up_word()
        self.prompt_num_guesses()
        self.runGame()
        
    
    def reset_controller(self):
        """
        Resets instance variables to play another game.
        """

        self.guessed = set()
        self.wrong = 0
        self.display = None
        self.status = None

    def prompt_num_guesses(self):
        """
        Asks player how many guesses they would like and stores it into the game instance.
        """

        try:
            self.guess_limit = int(input("How many guesses would you like? "))
            if (self.guess_limit > 24) or (self.guess_limit < 1):
                print("Invalid number of guesses")
                raise ValueError
        except ValueError:
            self.prompt_num_guesses()

    def set_up_word(self):
        """
        Instructs data layer to pull the word list.
        Sets up a display of the required length.
        """

        self.available_words.get_wordlist()
        word_length = self.available_words.get_random_word()
        self.display =  "".join( ["_" for char in range(word_length)] )


    def runGame(self):
        """
        Updates interface and tells the game to continue prompting responses 
        until requirements are met to end the game (win or lose)
        """

        self.update_interface(self.display)
        while( self.wrong < self.guess_limit and self.status == None):
            self.prompt_guess()
        
        self.endGame(self.status)

    def playAgain(self) -> bool :
        """
        Asks user if they want to play another game.
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


        mapped_display = self.available_words.get_evil_word(guess)


        if guess in mapped_display:
            print(f'Yes! "{guess}" is in the mystery word!')
        else:
            self.wrong += 1
            print(f'No! {guess} is not in the mystery word.')
            print(f'You have {self.guess_limit - self.wrong} guesses left.')

        
        self.update_interface(mapped_display)
        


    def update_interface(self, display):
        """
        Called by handle_guess method to update the interface and show the user where they are in the game.
        Also checks if there are any unfilled spots in the display, meaning the user has won, or if the user is 
        out of guesses, meaning they lost.

        """
        #union of old display and new display
        def unite_displays(display):
            new_string = ""
            for i in range(len(display)):
                if (display[i]) != "_":
                    new_string += display[i]
                elif self.display != "_":
                    new_string += self.display[i]
                else:
                    new_string += "_"
            
            return new_string
        
        self.display = unite_displays(display)
        

        printed_display = ""
        for i in range(len(self.display)):
            if self.display[i] in self.guessed:
                printed_display += self.display[i]
            else:
                printed_display += "_"
            printed_display += " "

        print(printed_display)

        if "_" not in printed_display:
            self.status = "win"
        elif self.wrong == self.guess_limit:
            self.status = "loss"


    def endGame(self, result):
        """
        Based on result argument, tells user if they won or lost
        """
        if result == "loss":
            print("You Lost.")
            print(f'The mystery word was {self.available_words.reveal_word()}')
        else:
            print("You Won!")
            

    @staticmethod
    def clean_input(outside_input):
        """
        makes all inputs capital letters
        """
        all_upper = outside_input.upper()
        return all_upper