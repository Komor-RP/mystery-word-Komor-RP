class WordList:
    """
    DATA LAYER
    methods - 
    instance variables - lists for the different difficulties
    """

    def __init__(self):
        self.easy = []
        self.medium = []
        self.hard = []

    def get_wordlist(self):
        """
        This gets the word list file, reads it, and feeds 3 separate lists into the WordList Data Layer
        /Users/fan/Documents/Momentum/week-1/mystery-word-Komor-RP/words.txt
        """
        with open('words.txt') as word_file:
            word_list = word_file.read().splitlines() 

        self.easy =  [ word for word in word_list if (4 <= len(word) <= 6) ]
        self.medium = [ word for word in word_list if (6 <= len(word) <= 8) ]
        self.hard = [ word for word in word_list if (len(word) > 8) ]

    def get_random_word(self):
        pass

