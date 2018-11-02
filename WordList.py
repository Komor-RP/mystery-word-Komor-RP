from random import choice

class WordList:
    """
    DATA LAYER
    Manages words for the game
    """

    def __init__(self):
        self.easy = []
        self.medium = []
        self.hard = []

    def get_wordlist(self):
        """
        This gets the word list file, reads it, and feeds 3 separate lists into the WordList Data Layer
        """
        with open('/Users/fan/Documents/Momentum/week-1/mystery-word-Komor-RP/words.txt') as word_file:
            word_list = word_file.read().splitlines() 

        self.easy =  [ word for word in word_list if (4 <= len(word) <= 6) ]
        self.medium = [ word for word in word_list if (6 <= len(word) <= 8) ]
        self.hard = [ word for word in word_list if (len(word) > 8) ]

    def get_random_word(self, diff):
        """
        Returns a random word based on given difficulty
        """
        
        if (diff == "EASY"): 
            chosen_word = choice(self.easy)
        elif (diff == "MEDIUM"):
            chosen_word = choice(self.medium)
        elif (diff == "HARD"):
            chosen_word = choice(self.hard)
        
        return chosen_word
        
        
