import pygame, sys
import numpy as np

pygame.init()

width = 600
height = 600
line_width = 15

board_row = 3 
board_col = 3

colour = (28,170,156)
line_colour = (23,145,135)
circle_colour = (239,231,200)
line_colour_2 = (200,145,135)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(colour)

board = np.zeros((board_row,board_col))

def draw_figures():
	for row in range(board_row):
		for col in range(board_col):
			if board[row][col] == 1:
				pygame.draw.circle(screen, circle_colour, (int(col*200 + 100), int(row*200 + 100)), 60, 15)

			elif board[row][col] == 2:
				pygame.draw.line(screen, line_colour_2, (col*200 + 55, row*200+200-55), (col*200+200-55, row*200+55), 25)
				pygame.draw.line(screen, line_colour_2, (col*200 + 55, row*200+55), (col*200+200-55, row*200+200-55), 25)


def draw_line():
	#1st horizontal
	pygame.draw.line(screen, line_colour, (0,200), (600,200), line_width)
	#2nd horizontal 
	pygame.draw.line(screen, line_colour, (0,400), (600,400), line_width)
	#1st vertical
	pygame.draw.line(screen, line_colour, (200,0), (200,600), line_width)
	#2nd vertical
	pygame.draw.line(screen, line_colour, (400,0), (400,600), line_width)

def mark_square(row, col, player):
	board[row][col] = player

def available_square(row, col):
	return board[row][col] == 0

def is_board_full():
	for i in range(board_row):
		for j in range(board_col):
			if board[i][j] == 0:
				return False
	return True

def check_win(player):
	for col in range(board_col):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_line(col, player)
			return True

	for row in range(board_row):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_line(row, player)
			return True

	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc(player)
		return True

	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc(player)
		return True

	return False

def draw_vertical_line(col,player):
	posX = col*200+100

	c = (255,255,255)

	pygame.draw.line(screen, c, (posX, 15), (posX,height-15), 15)

def draw_horizontal_line(row,player):
	posY = row * 200+100

	c = (255,255,255)

	pygame.draw.line(screen, c, (15, posY), (width-15, posY), 15)

def draw_asc(player):
	c = (255,255,255)

	pygame.draw.line(screen, c, (15, height-15), (width -15,15), 15)

def draw_desc(player):
	c = (255,255,255)

	pygame.draw.line(screen, c, (15,15), (width-15, height-15), 15)

def restart():
	screen.fill(colour)
	draw_line()
	players = 1
	for row in range(board_row):
		for col in range(board_col):
			board[row][col] = 0


draw_line()

players = 1
game_over = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
			mouseX = event.pos[0]
			mouseY = event.pos[1]

			clicked_row = int(mouseY // 200)
			clicked_col = int(mouseX // 200)

			if available_square(clicked_row, clicked_col):
				if players == 1:
					mark_square(clicked_row, clicked_col, players)
					if check_win(players):
						game_over = True
					players = 2

				elif players == 2:
					mark_square(clicked_row, clicked_col, players)
					if check_win(players):
						game_over = True
					players = 1

				draw_figures()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()

	pygame.display.update()