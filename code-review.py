import random

def start_game():

   welcome()

   difficulty()

   guessed_letter()

   word_to_guess = False

   while not tries < 8 and letter_listing < 8:

       #tries += 1

       if tries == 8:

           print("Game over!!!. Better luck next time!")

def welcome():

   print("Welcome to my Mystery Word Game. You have 8 guesses to get the word correct. Choose wisely")

def difficulty():

   level = input("Which level will you like to play: (1, 2 or 3) ") #Ask for level to play

   while level != "1" and level != "2" and level != "3": #Need to include a blank answer

       level = input("Sorry, that was not an option. Which level will you like to play: (1, 2 or 3) ")

   if level == "1":

       print("Easy Level it is!")

       print(random.choice(easy))

   elif level == "2":

       print("Normal level it is!")

       #return(random.choice(normal))

       print(random.choice(normal))

   elif level == "3":

       print("Hard level it is!")

       return(random.choice(hard))

words = (open('/Users/fan/Documents/Momentum/week-1/mystery-word-Komor-RP/words.txt').read().split()) #gets words from text file

#words.sort(key=len) #sorts words by their length

easy = []

for e in words:

   if len(e) >= 4 and len(e) <= 6: #gets words with 4 to 6 letters

       easy.append(e)

normal = []

for e in words:

   if len(e) >= 6 and len(e) <= 8: #gets words with 6 to 8 letters

       normal.append(e)

hard = []

for e in words:

   if len(e) >= 8: #gets words with 8+ letters

       hard.append(e)

word_to_guess = (random.choice(normal))

letter_listing = []

for w in word_to_guess:

   letter_listing.append(w)

tries = 0

def guessed_letter():

   guess = input("Pick a letter: ")

   global tries

   tries +=1
   print(letter_listing)

   if guess not in letter_listing:

       print("That letter is not part of the word. Please try again")

   elif guess in letter_listing:

       print("That letter is part of the word!")

start_game()


