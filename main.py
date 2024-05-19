from typing_extensions import clear_overloads
import pygame as py
import sys
from pygame.locals import QUIT
import random

width = 600
height = 600

timer = py.time.Clock()
py.init()
screen = py.display.set_mode((width, height))
py.display.set_caption('Memory Game!!')
fps = 60
white = (255, 255, 255)
black = (0,0,0)
cream = (243,255,185)
red = (178,58,72)
pink = (252,185,178)
dblue = (3,37,78)
lblue = (132,153,177)
t_font = py.font.Font('freesansbold.ttf',56)
font = py.font.Font('freesansbold.ttf',26)
rows = 6
cols = 8
new_board = True
option = []
spaces = []
used = []
def generate_board():
    global option
    global spaces
    global used
    for item in range(1, rows*cols // 2 + 1):
        option.append(item)
    for int in range(rows*cols):
        card = option[random.randint(0, len(option)-1)]
        spaces.append(card)
        if card is used:
            option.remove(card)
        else:
            used.append(card)
def draw_background():
    s_title = py.draw.rect(screen, (dblue), [0, 0, 600, 100])
    t_title = t_font.render('Memory Game', True, (white))
    screen.blit(t_title, (10,20))
    s_board = py.draw.rect(screen, (lblue), [0, 100, width, height - 200], 0)
    s_bottom = py.draw.rect(screen, (dblue), [0, height - 100, width, 100], 0)
    

def draw_board():
    global rows
    global cols
    board_list = []
    for i in range(cols):
        for j in range(rows):
            card = py.draw.rect(screen, white, [i*75 + 12, j*65 + 112, 50, 50], 0, 8)
            board_list.append(card)
            
    return board_list

while True:
    timer.tick(fps)
    screen.fill(white)
    if new_board:
        generate_board()
        print(spaces)
        new_board = False
    draw_background() 
    draw_board()
    for event in py.event.get():
        if event.type == QUIT:
           py.quit()
           sys.exit()
    py.display.flip()

