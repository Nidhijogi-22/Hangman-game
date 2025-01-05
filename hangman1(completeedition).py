# # word="hangman"
# # words_length=7
# # correct_pos=0
# # incorrect_pos=0
# word="hangman"
# total_attempts=10
# current_word = ['_', '_', '_', '_', '_', '_', '_'] 
# user_input=input("Guess the word by entering a letter: ")
# guessed_letters=str(user_input)
# attempts_left=10

#replit

import pygame
import os
import math
import random

pygame.init() #to initialize the pygame module to avoid any unnecesary errors
width, height = 1000, 700
win=pygame.display.set_mode((width, height)) #dimensions for the pygame screen
pygame.display.set_caption("Hangman Game!")

radius=20
gap=15
letters=[]
startx=round((width-(radius*2+gap)*13)/2)
starty=400
A=65 #ascii
for i in range(26):
     x=startx+gap*2+((radius*2+gap)*(i%13))
     y=starty+((i//13)*(gap+radius*2))
     letters.append([x, y, chr(A+i), True])

letter_font=pygame.font.SysFont("couriernew", 40)
word_font=pygame.font.SysFont("couriernew", 40)
title_font=pygame.font.SysFont("Times New Roman", 70)

images=[]
for i in range(7):
     image=pygame.image.load("hangmanimages/hangman"+str(i)+".png")
     images.append(image)
print(images)

hangman_status=0
words=["CRICKET", "FOOTBALL", "BOOKS", "HANDBAG", "WATCH", "PAINTING", "HANGMAN", "KEYHOLE", "JACKPOT", "FUNNY", "GALAXY", "PUPPY", "BOOKWORM", "LUCKY", "PYTHON", "COMPILER", "LUXURY"]
word=random.choice(words)
guessed=[]

white=(255, 218, 185)
black=(0, 0, 0)
FPS = 60 #frames per second(max)
clock=pygame.time.Clock() 
run=True

def draw():
    win.fill(white)
    
    text=title_font.render("HANGMAN GAME!", 1, black)
    win.blit(text, (width/2-text.get_width()/2, 20))

    display_word=" "
    for letter in word:
        if letter in guessed:
            display_word+=letter+ " "
        else:
            display_word+= " _ "
    text=word_font.render(display_word,1, black)
    win.blit(text, (300, 150))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, black, (x, y), radius, 3)
            text=letter_font.render(ltr, 1, black)
            win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_msg(message):
    win.fill(white)
    text=word_font.render(message, 1, black)
    win.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)




while run:
    clock.tick(FPS)
    
    # draw()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        if event.type==pygame.MOUSEBUTTONDOWN:
               m_x, m_y = pygame.mouse.get_pos()
                  #to check the x-y positions of the mouse, to compare the dist b/w the mouse and the button and check if the user on the mouse button or not.
               for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x-m_x)**2+(y-m_y)**2)
                    if dis<radius:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                             hangman_status+=1
    draw()
    
    won=True                        
    for letter in word:
        if letter not in guessed:
            won=False
            break
    if won:
       display_msg(f"You Won!🥳, \n You guessed {word} correctly!!!🎉")
       break

    if hangman_status==6:
        display_msg(f"You Lost..., the word was {word}☹️")
        break
                   
pygame.quit()