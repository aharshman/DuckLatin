# -*- coding: utf-8 -*-
"""
Alexander Harshman
10/11/2021
"""

# importing everything
from graphics import *
from math import *
    

def main():
    
    i = 0
    
# Opening the window
    win = GraphWin('Duck Latin', 450, 500)
    win.setBackground('light blue')
    
# Title
    Title = Text(Point(225, 125), 'Enter a phrase:').draw(win)
    
# Entry Box
    Message = Entry(Point(225, 175), 30).draw(win)
    
# Quack!
    QuackCenter = Point(112.5, 275)
    Quack = Circle(QuackCenter, 50)
    Quack.setFill('light pink')
    Quack.draw(win)
    Quack.setWidth(2)
    Qaucktext = Text(Point(112.5, 275), 'Quack!').draw(win)
    
# Quit!
    QuitCenter = Point(337.5, 275)
    Quit = Circle(QuitCenter, 50)
    Quit.setFill('light yellow')
    Quit.setWidth(2)
    Quit.draw(win)
    Quittext = Text(Point(337.5, 275), 'Quit!').draw(win)
    
# Output text
    OutputText = Text(Point(225, 425), '').draw(win)
    
# The Duck Says
    Duck = Text(Point(225, 375), 'The Ducks Say:').draw(win)
    
# Keeping track of where the user clicks
    while True:
            click = win.getMouse()
            x = click.getX()
            y = click.getY()
            distanceQuack = sqrt(((x - 112.5)**2) + (y - 275)**2)
            distanceQuit = sqrt(((x - 337.5)**2) + (y - 275)**2)
            
        # If the user clicks inside the Quit button the window closes
            if distanceQuit <= 50:
                win.close()
            
        # If the user clicks the Quack button
            if distanceQuack <= 50:
                sentence = Message.getText()
                words = sentence.split(' ')

                
            #Setting up vowel and blend lists
                vowels = ['a', 'e', 'i', 'o', 'u']
                blends = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
                blends3 = ['scr', 'shr', 'spl', 'spr', 'str', 'thr', 'sch']
                output = ''
                
            # Loop for every word
                for word in words:
                    n = 0
                    temp = word[0].lower()
                    i += 1
                    
                # If the word starts with a vowel
                    if temp in vowels:
                        word = word + 'wack'
                    
                # If the word strats with a blend of three letters
                    elif word[0:3].lower() in blends3:
                        temp = word[0:3].lower()
                        word = word[3:] + temp + 'ack'
                    
                # If the word starts with a blend of two letters
                    elif word[0:2].lower() in blends:
                        temp = word[0:2].lower()
                        word = word[2:] + temp + 'ack'
                    
                # If the word doesn't start with a vowel or a blend
                    else:
                        word = word[1:] + temp + 'ack'
                    output += word + ' '
                
            # Displaying the translated words
                OutputText.setText(output)

    
    win.getMouse()
    win.close()
    
main()