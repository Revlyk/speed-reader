########################################################################
#
# CS 101
# Program 4
# Christopher Hoffman
# clhd5d@mail.umkc.edu
#
# Problem: Create a program that can displays a book word by word to the user. The book must be specified by the user,
#           and the user has the options to pick the font, as well as the amount of words per minute.
#
#
# ALGORITHM :
# 1.	Ask user for file name.
#   a.	Try/Except to prevent errors for incorrect names.
#   b.	Keep asking until file can be opened.
#   c.	Files are UTF-8. Verify encoding under utf-8.
# 2.	Ask user for Words per Minute. (Divide Words per Minute/60 to figure out pause between words)
#   a.	Try/Except to prevent errors from non-numbers
#   b.	Keep asking until valid number (1<= x >= 1000).
#   c.	If word ends in punctuation, double pause time.
# 3.	Ask user for font size.
#   a.	Try/Except to prevent errors from non-numbers
#   b.	Force font size between 5 and 36 inclusive.
# 4.	Ask user for word to start reading at.
#   a.	Try/Except to prevent errors from non numbers
#   b.	Number range from 1 – last word of book inclusive
#   c.	Keep asking until valid number or user hits enter with no input.
#   d.	Enter with no input starts at 1.
# 5.	Split file into individual words.
# 6.	Create window.
# 7.	Output words to window.
# 8.	Display Current word out of total (Current/Total)
#   a.	Display should be at bottom of window.
#   b.	Font size should  not be large.
#   9.	Allow users to click to pause.
#   a.	Clicking again would unpause.
# 10.	Close window.
#   a.	User should be able to escape the window without causing an error.
# 11.	Close file
# 12.	Ask user if they want to run the program again
#
########################################################################

import graphics as gfx
import time
run= True

# Function asking the user if they want to continue playing. Keeps asking until the user gives a valid response.
def play_again():

    while True:

        result = input("Do you want to play again? ==> ")

        if result.upper() in ["Y", "YES"]:
            return True
        if result.upper() in ["N", "NO"]:
            return False
        print("You must enter Y/YES/N/NO")

# Function to open a file for the user. Keeps asking until a valid file is opened.
def open_file(prompt):
    while True:
        try:
            file = open(input(prompt), encoding="utf-8")
            return file
        except: Exception
        print("Please enter a valid file.")

# Function that converts the file the user selected into a list of individual strings words.
def word_list(input_file):
    words = []
    for line in input_file:
        for word in line.split():
            words.append(word)
    return words

# Function asking the user the number of words per minute to be displayed, and caclulates the pauses between each word.
def words_per_minute(prompt):
    while True:
        try:
            wpm = int(input(prompt))
            wps = wpm / 60
            pause = 1 / (wps)
            return (pause)
        except: Exception
        print("You must enter a valid number from 1 to 1000")

# Function asking the user what size font they would like for the main display that reads the book.
def font_size(prompt):
    while True:
        try:
            font = int(input(prompt))
            if 5 <= font <= 36:
                return font
            else:
                print("You did not enter a valid number.")
        except:Exception
        print("You must pick a number from 5 to 36.")

# Function asking the user where they would like to start reading from.
def starting_word(prompt):
    while True:
        start = input(prompt)
        if start == "":
            start = 1
        try:
            start = int(start)
            if 1 <= start <= word_count:
                return start
        except: Exception
        print("You must enter a valid starting point. You may pick any number from 1 to then end of the book.")
    return start

# Function that opens the reading window, and displays all of the text for the user.
def reading_window():
    count = starting_spot

    window = gfx.GraphWin("Speed Reader", 600, 400)
    text_main = gfx.Text(gfx.Point(300, 200), "Click to begin")  # Starts with a pause
    text_main.draw(window)  # Auto updates, do not have to redraw it when it changes.
    text_main.setSize(font)
    text_secondary = gfx.Text(gfx.Point(300, 350), str(count) + "/" + str(word_count))
    text_secondary.draw(window) # Separate from text_main, have to draw separately.
    text_secondary.setSize(10)


    window.getMouse()  # Pause to view result
    try:
        for word in words[starting_spot::1]:
            if window.isClosed() == True:
                return
            text_main.setText(word)
            if word[-1] == ".":               # Double pause if word ends in punctuation.
                time.sleep(pause_time * 2)
            elif word[-1] == ",":             # Double pause if word ends in punctuation.
                time.sleep(pause_time * 2)
            elif word[-1] == ";":             # Double pause if word ends in punctuation.
                time.sleep(pause_time * 2)
            else:
                time.sleep(pause_time)        # Normal pause if no punctuation at the end.
            count += 1
            text_secondary.setText(str(count) + "/" + str(word_count)) # Updates the word counter at the bottom.
            click = window.checkMouse()

            while click is not None:
                time.sleep(1)
                if window.isClosed() == True:
                    return
                unclick = window.checkMouse()
                if unclick is not None:
                    break
    except: Exception
    return

    window.close()  # Close window when done
    return


while run == True :


    input_file = open_file("What book would you like to read?")

    words = word_list(input_file)

    word_count = len(words)     # Calculates the length of the book.

    word_str = str(word_count)  # Converts the length of the book to a string to be used in prompts.

    pause_time = words_per_minute("How many words would you like per minute?")

    font =  font_size("What size font would you like?")

    starting_spot = starting_word("Please select a location to start reading from. You may enter any word from 1 to "
                                  + word_str)


    reading_window()


    run = play_again()





