from random import choice

class WordList:
    """
    DATA LAYER
    Manages words for the game
    """

    def __init__(self):
        self.word_list = None
        self.wordlength = None

    def get_wordlist(self):
        """
        This gets the word list file, reads it, and stores it into a dictionary.
        """
        with open('words.txt') as word_file:
            word_list = word_file.read().upper().splitlines()

        self.word_list = { "longest_list" : word_list}

    def get_random_word(self) -> int:
        """
        Returns a random word length and sorts the word list for the length
        """
        chosen_word = choice(self.word_list["longest_list"])

        self.wordlength = len(chosen_word)
        self.word_list["longest_list"] = [word for word in self.word_list["longest_list"] if len(word) == self.wordlength]
        
        return self.wordlength

    def reveal_word(self):
        """
        Returns a random word from the remaining list to reveal to the losing player.
        """
        return choice(self.word_list["longest_list"])


    def get_evil_word(self, letter) -> str:
        """
        Filters word list by both letter frequency and letter location.
        Returns a string showing the letter location, if any
        examples = _______. _e___
        """

        self.filter_letter(letter)
        if letter in self.word_list["longest_list"][0]:
            return self.filter_location(letter)
        else:
            display_list = ["_" for char in range(self.wordlength)]
            return "".join(display_list)

        

    def filter_letter(self, letter):
        """
        check frequencies of letter in remaining words 
        save longest list into the remaining words
        """
        #list of tuples
        letter_frequency = sorted( { (word, word.count(letter)) for word in self.word_list["longest_list"]} )
        
        max_length = []
        for x in range(3):            
            new_list = [ word[0] for word in letter_frequency if word[1]==x ]
            
            if len(new_list) > len(max_length):
                max_length = new_list

        self.word_list["longest_list"] = max_length

    def filter_location(self, letter) -> str:
        """
        sort the remaining list of words into lists based on location of letters
        keep the longest list in self.word_list["longest_word"]
        returns mapped string of the most frequent letter locations

        [(string, word) , (string, word) , (string, word)] => sort into
        { "__e_" : [word, word, word], "_e__" : [word, word, word, word]} 
        """
        
        def map_letter(word) -> str:
            """
            returns letter's mapped location in a word
            """

            letter_locations = ""
            for char in word:
                if char == letter:
                    letter_locations += char
                else:
                    letter_locations += "_"
            return letter_locations
        
        def sort_mapped_letters(mapped_letter_list) -> dict:
            """
            sort letter_mapped into lists based on letter locations
            """
            
            letter_mapping_dict = {}
            for element in letter_mapped:
                if element[0] not in letter_mapping_dict:
                    letter_mapping_dict[element[0]] = []

                letter_mapping_dict[element[0]].append(element[1])

            return letter_mapping_dict

                          
        letter_mapped = [ (map_letter(word), word) for word in self.word_list["longest_list"]]

        #sort letter_mapped into lists based on letter locations
        letter_mapping_dict = sort_mapped_letters(letter_mapped)

        max_length = []
        mapped_display = ""
        for mapped_key in letter_mapping_dict:
            if len(letter_mapping_dict[mapped_key]) > len(max_length):
                max_length = letter_mapping_dict[mapped_key]
                mapped_display = mapped_key
        
        self.word_list["longest_list"] = max_length
        
        return mapped_display
        

        
