from typing_extensions import clear_overloads
import pygame as py
import sys
from pygame.locals import QUIT
import random



#initialize pygame
py.init()

#colors
white = (255, 255, 255)
black = (0,0,0)
cream = (243,255,185)
red = (178,58,72)
pink = (252,185,178)
dblue = (3,37,78)
lblue = (132,153,177)

#constants
width = 450
height = 600
timer = py.time.Clock()
py.display.set_caption('Memory Game!!')
fps = 60

t_font = py.font.Font('freesansbold.ttf',46)
font = py.font.Font('freesansbold.ttf',26)
rows, cols = 6, 6
new_board = True
option = []
spaces = []
used = []
correct = [[0] * cols for _ in range(rows)]
guess1 = guess2 = False
guess1_num = guess2_num = 0
score = matches = 0
gameover = False

screen = py.display.set_mode((width, height))
def generate_board():
    global option, spaces, used
    option = list(range(rows * cols // 2))
    for item in range(rows*cols):
        card = option[random.randint(0, len(option)-1)]
        spaces.append(card)
        if card in used:
            used.remove(card)
            option.remove(card)
        else:
            used.append(card)
def draw_background():
    global score
    s_title = py.draw.rect(screen, (dblue), [0, 0, 600, 100])
    t_title = t_font.render('Memory Game', True, (white))
    screen.blit(t_title, (10,20))

    s_board = py.draw.rect(screen, (lblue), [0, 100, width, height - 200], 0)
    s_bottom = py.draw.rect(screen, (dblue), [0, height - 100, width, 100], 0)

    re_but = py.draw.rect(screen, white, [10, height - 90, 100, 30], 0, 5)
    t_re = font.render('Restart', True, (black))
    screen.blit(t_re, (15,512))

    t_score = font.render(f'Turns: {score}', True, (white))
    screen.blit(t_score, (130,512))
    return re_but


def checkguess(first, second):
    global spaces, correct, score, matches
    if spaces[first] == spaces[second]:
        col1 = first // rows
        row1 = first - (first // rows * rows)
        col2 = second // rows
        row2 = second - (second // rows * rows)
        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            matches += 1

def draw_board():
    global rows, cols, correct
    board_list = []
    for i in range(cols):
        for j in range(rows):
            card = py.draw.rect(screen, white, [i*75 + 12, j*65 + 112, 50, 50], 0, 4)
            board_list.append(card)
        #    t_card = font.render(f'{spaces[i*rows+j]}', True, black)
         #   screen.blit(t_card, (i*75 + 18, j*65 + 120))

    for m in range(rows):
        for n in range(cols):
            if correct[m][n] == 1:
                py.draw.rect(screen, red, [n*75 + 10, m*65 + 110, 54, 54], 3, 4)
                t_card = font.render(f'{spaces[n*rows+m]}', True, black)
                screen.blit(t_card, (n*75 + 18, m*65 + 120))

    return board_list

def reset_game():
    global option, used, spaces, new_board, score, matches, correct, guess1, guess2, guess1_num, guess2_num, gameover
    option = []
    used = []
    spaces = []
    new_board = True
    score = matches = 0
    correct = [[0] * cols for _ in range(rows)]
    guess1 = guess2 = False
    guess1_num = guess2_num = 0
    gameover = False

while True:
    timer.tick(fps)
    screen.fill(white)
    if new_board:
        generate_board()
        new_board = False
    re = draw_background() 
    draw_board()
    board = draw_board()
    for event in py.event.get():
        if guess1 and guess2:
            score += 1
            checkguess(guess1_num, guess2_num)
            py.time.delay(1000)
            guess1 = False
            guess2 = False
        if event.type == QUIT:
           py.quit()
           sys.exit()
        if event.type == py.MOUSEBUTTONDOWN:
            for i, button in enumerate(board):
                if not gameover and button.collidepoint(event.pos):
                    if not guess1:
                        guess1 = True
                        guess1_num = i
                        print(i)
                    elif not guess2 and i != guess1_num:
                        guess2 = True
                        guess2_num = i
                        print(i)

            if re.collidepoint(event.pos):
                reset_game()
                

    if matches == rows*cols//2:
        gameover = True
        win = py.draw.rect(screen, (dblue), [10, height - 300, width - 20, 80], 0, 5)
        t_win = t_font.render(f'You won in: {score} moves! ', True, (white))
        screen.blit(t_win, (45,height - 300))

    if guess1:
        t_card = font.render(f'{spaces[guess1_num]}', True, pink)
        loco = (guess1_num // rows * 75 + 18, (guess1_num - (guess1_num // rows * rows)) * 65 + 120) 
        screen.blit(t_card, loco)
    if guess2:
        t_card = font.render(f'{spaces[guess2_num]}', True, pink)
        loco = (guess2_num // rows * 75 + 18, (guess2_num - (guess2_num // rows * rows)) * 65 + 120) 
        screen.blit(t_card, loco)
    py.display.flip()
py.quit()

