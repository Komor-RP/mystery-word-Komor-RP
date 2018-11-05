#?
import random

# print(repr(word_file.readlines()))

def clean_text(user_text):
    new_text = ""

    for char in user_text:
        if char.isalpha():
            new_text = new_text + char

    return new_text


easy_mode_words = []

with open('words.txt') as word_file:

    for all_words in word_file.readlines():

        #easy_mode_words = [] you had this here before  yeah i know...I w
        #was trying it out there to run it
        #when you have it here, the for loop will make it "[]" every loop, clearing anything
        #you put into it
        #haha ooooh ok ;)  Have you gotten it to run anywhere else?  
        #I tried three spots and nothing
        #it works now, but only with the easy list, I'm going to leave the others for you to fix
        #they have the same issues as I've explained for the easy list

        if len(all_words) > 3 and len(all_words) < 7:
            easy_mode_words.append(clean_text(all_words))
            

        normal_mode_words = []
        if len(all_words) > 5 and len(all_words) < 9:
            normal_mode_words.append(clean_text(all_words))


        hard_mode_words = []
        if len(all_words) > 8:
            hard_mode_words.append(clean_text(all_words))
            
print(easy_mode_words)

user_text = input(
    "Please choose your level of difficulty.\
    Enter 1 for Easy Mode, 2 for Normal Mode, and 3 for Hard Mode.")

if user_text == "1":
    random.choice(easy_mode_words)





# easy_mode_words = clean_text(easy_mode_words)
print(easy_mode_words)

if user_text == "2":
    random.choice(normal_mode_words)

if user_text == "3":
    random.choice(hard_mode_words)

input("You have 8 guesses to select the correct letters of the mystery word.\
      Correct guesses don't count against the 8 guesses.  Good luck!")

# >notebooks>listcomprehensions

# random.random() for





