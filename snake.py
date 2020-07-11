import pygame as pg
import sys
import random as ran
import time

pg.init()
clock = pg.time.Clock()

width = 1104
height = 704

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

light_blue = (0,153,255)
blue = (0,138,230)
dark_blue = (0,51,204)
navy = (0, 0, 179)
white = (255,255,255)
black = (0,0,0)
red = (230, 0, 0)
light_green = (32,223,32)
green = (0,153,0)
dark_green = (0, 128, 0)
orange = (255,102,0)
dark_orange = (204,82,0)
yellow = (255,209,26)


score_font = "consolas"
button_font = "aleo" 


taskbar_out_x = 0
taskbar_out_y = 0
taskbar_out_width = width
taskbar_out_height = 112

taskbar_out = (taskbar_out_x, taskbar_out_y, taskbar_out_width, taskbar_out_height)
taskbar_in = (taskbar_out_x+10, taskbar_out_y+10, taskbar_out_width-20, taskbar_out_height-20)




vline1_x = int(width/4)
vline1_y = taskbar_out_y
vline2_x = int(width/2)
vline2_y = taskbar_out_y
vline3_x = int(3*width/4)
vline3_y = taskbar_out_y

mini_info_height = int((taskbar_out_height-20)/3)
hline1_x = taskbar_out_x
hline1_y = mini_info_height+10
hline2_x = taskbar_out_x
hline2_y = 2*mini_info_height+10
hline3_x = vline3_x
hline3_y = hline1_y


new_game_button_x = vline1_x+3
new_game_button_y = taskbar_out_y+10
new_game_button_width = int(width/4 -5)
new_game_button_height = taskbar_out_height-20

new_game_button = (new_game_button_x, new_game_button_y, new_game_button_width, new_game_button_height,)

high_score_button_x = int(width/2+3)
high_score_button_y = new_game_button_y
high_score_button_width = new_game_button_width
high_score_button_height = new_game_button_height

high_score_button = (high_score_button_x, high_score_button_y, high_score_button_width, high_score_button_height)

select_theme_button_x = hline3_x+3
select_theme_button_y = taskbar_out_y+10
select_theme_button_width = new_game_button_width-8
select_theme_button_height = int(new_game_button_height/3 -2)

select_theme_button = (select_theme_button_x, select_theme_button_y, select_theme_button_width, select_theme_button_height)













start = False
snake_size = 16
speed = 16
wait = 0.06
running = True
food_radius = int(snake_size/2)

h_score = 0



def mouse_compare(rect):
	mouse_pos = pg.mouse.get_pos()
	mouse_x = mouse_pos[0]
	mouse_y = mouse_pos[1]
	if mouse_x >= rect[0] and mouse_x <= rect[0]+rect[2] and mouse_y >= rect[1] and mouse_y <= rect[1]+rect[3]:
		return True

def hover(active, inactive, rect):
	if mouse_compare(rect) == True:
		pg.draw.rect(screen, active, rect)
	else:
		pg.draw.rect(screen, inactive, rect)



def text(text, x, y , font=button_font, size=60, colour=white):
	label = (pg.font.SysFont(font, size)).render(text, 1, colour)
	screen.blit(label, (int(x), int(y)))


def draw_l_hand_info(h_score, score, speed):
	x = 20
	y = 11
	text(("HSCORE: " + str(h_score)), x, y, score_font, 30)
	x = 37
	y += mini_info_height+1
	text(("SCORE: " + str(score)), x, y, score_font, 30)
	y += mini_info_height+2
	text(("SPEED: " + str(speed)), x, y, score_font, 30)


def draw_taskbar():
	pg.draw.rect(screen, dark_blue, taskbar_out)
	pg.draw.rect(screen, light_blue, taskbar_in)
	pg.draw.line(screen, dark_blue, (vline1_x, vline1_y), (vline1_x, taskbar_out_height-3), 5)
	pg.draw.line(screen, dark_blue, (vline2_x, vline2_y), (vline2_x, taskbar_out_height-3), 5)
	pg.draw.line(screen, dark_blue, (vline3_x, vline3_y), (vline3_x, taskbar_out_height-3), 5)

	pg.draw.line(screen, dark_blue, (hline1_x, hline1_y), (vline1_x, hline1_y), 5)
	pg.draw.line(screen, dark_blue, (hline2_x, hline2_y), (vline1_x, hline2_y), 5)
	pg.draw.line(screen, dark_blue, (hline3_x, hline3_y), (taskbar_out_width, hline3_y), 5)


	hover(dark_green, green, new_game_button)
	text("NEW GAME", new_game_button_x+15, new_game_button_height/2 -8, button_font, 60)

	hover(dark_orange, orange, high_score_button)
	text("HIGH SCORES", high_score_button_x+4, high_score_button_height/2 -7, button_font, 55)

	hover(blue, light_blue, select_theme_button)
	text("SELECT THEME", select_theme_button_x+29, select_theme_button_y/2 +6, score_font, 30)



def draw_snake(snake_x, snake_y):
	pg.draw.rect(screen, red, (snake_x, snake_y, snake_size, snake_size))



def food_gen():
	food_x = 16*ran.randint(0,68)+food_radius
	food_y = 16*ran.randint(7, 37)+food_radius
	return (food_x, food_y)

def round16(num):
    return 16*round(num/16)

def abs(num):
	if num > 0:
		return num
	else:
		return num*-1

def conditions():
	if alive == True and can_move == True and paused == False:
		return True
	else:
		return False

def name_input():
	print("name")


def draw_box(x, y, width, height, thickness=5, clickable=False, active=blue, inactive=light_blue, inside=light_blue, outside=dark_blue, ):
	if clickable == False:
		pg.draw.rect(screen, outside, (x, y , width, thickness)) # Draws top line
		pg.draw.rect(screen, outside, (x+width-thickness, y+thickness, thickness, height-2*thickness)) # Draws left line
		pg.draw.rect(screen, outside, (x, y+height-thickness, width, thickness)) # Draws bottom line
		pg.draw.rect(screen, outside, (x, y+thickness, thickness, height-2*thickness)) # Draws left line
		pg.draw.rect(screen, inside, (x+thickness, y+thickness, width-2*thickness, height-2*thickness)) # Draws inside rectangle
	else:
		pg.draw.rect(screen, outside, (x, y , width, thickness)) # Draws top line
		pg.draw.rect(screen, outside, (x+width-thickness, y+thickness, thickness, height-2*thickness)) # Draws left line
		pg.draw.rect(screen, outside, (x, y+height-thickness, width, thickness)) # Draws bottom line
		pg.draw.rect(screen, outside, (x, y+thickness, thickness, height-2*thickness)) # Draws left line
		hover(active, inactive, (x+thickness, y+thickness, width-2*thickness, height-2*thickness))




def game_over():
	global alive, game_over_button, execute, h_score, x_offset, y_offset, new_high_score, enter_name
	alive = False
	paused = True
	moving = "not"

	
	

	

	if execute == True:
		print("  pos: " + str(pos_list))
		print(" x, y: " + str((snake_x, snake_y)))

		if score > h_score:
			new_high_score = True
			h_score = score
			x_offset = 30
			y_offset = -48
		else:
			x_offset = 33
			y_offset = -28

		execute = False

	game_over_x = int(width/3 - 37)
	game_over_y = int((height/3 + 80) + 30)
	game_over_width = 2*new_game_button_width - 100
	game_over_height = new_game_button_height+30

	game_over_button = (game_over_x, game_over_y, game_over_width, game_over_height)


	enter_name_x = game_over_x
	enter_name_y = game_over_y+game_over_height-10
	enter_name_width = game_over_width
	enter_name_height = 50

	enter_name = (enter_name_x, enter_name_y, enter_name_width, enter_name_height)

	
	draw_box(game_over_x, game_over_y, game_over_width, game_over_height, 10, True)

	text("GAME OVER", game_over_x + x_offset, game_over_y+game_over_height/2 + y_offset, button_font, 90)	
	if new_high_score == True:
		text("New High Score! Enter name: ", game_over_x+20, game_over_y+game_over_height-45, button_font, 42, yellow)
		if enter_name_active == False:
			draw_box(enter_name_x, enter_name_y, enter_name_width, enter_name_height, 10, True)
		else:
			draw_box(enter_name_x, enter_name_y, enter_name_width, enter_name_height, 10, True, blue, light_blue, navy, navy)
	text(name, enter_name_x+15, enter_name_y+16, button_font, 30)
		



def new_game():
	global draw_new_food, score, start, pos_list, alive, paused, can_move, snake_x, snake_y, execute, new_high_score, enter_name, enter_name_active, name

	alive = True
	snake_x = 64
	snake_y = 128
	pos_list = [(snake_x, snake_y)]
	score = 0
	max_list = 1
	paused = False
	execute = True
	special = False
	run_special = False
	enter_name_active = False
	new_high_score = False
	name = ""

	draw_new_food = True

	moving = "not"
	last_move = ""
	can_move = True

	while running:
		mouse_pos = pg.mouse.get_pos()
		mouse_x = mouse_pos[0]
		mouse_y = mouse_pos[1]


		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()

			if event.type == pg.MOUSEBUTTONDOWN:
				# 1 is the left mouse button, 2 is middle, 3 is right.
				if event.button == 1:
					if mouse_compare(new_game_button) == True:
						new_game()
					elif mouse_compare(high_score_button) == True:
						print("High Scores")
					elif mouse_compare(select_theme_button) == True:
						print("Select Theme")
					elif alive == False:
						if mouse_compare(game_over_button) == True:
							new_game()
						elif new_high_score == True:
							if mouse_compare(enter_name) == True:
								enter_name_active = True
							else:
								enter_name_active = False


			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT and moving != "right" and conditions() == True:
					start = True
					moving = "left"
					can_move = False

				elif event.key == pg.K_RIGHT and moving !="left" and conditions() == True :
					start = True
					moving = "right"
					can_move = False
					
				elif event.key == pg.K_UP and moving !="down" and conditions() == True :
					start = True
					moving = "up"
					can_move = False

				elif event.key == pg.K_DOWN and moving !="up" and conditions() == True :
					start = True
					moving = "down"
					can_move = False


				elif event.key == pg.K_SPACE:
					if new_high_score == False:
						if alive == False:
							new_game()

						elif paused == False:
							paused = True
							last_move = moving
							moving = "not"

						else:
							paused = False
							moving = last_move

						print("  pos: " + str(pos_list))
						print(" x, y: " + str((snake_x, snake_y)))


				elif enter_name_active == True:
					if event.key == pg.K_RETURN:
						print(name)
						name = ""
						new_game()
					elif event.key == pg.K_BACKSPACE:
						name = name[:-1]
					elif event.key == pg.K_SPACE:
						print("spaaaaaaaaaaaaace")
						name = name + " "
					else:
						if len(name) <= 20:
							name += event.unicode


				elif event.key == pg.K_p:
					score +=5

				elif event.key == pg.K_g:
					score = 100000
					run_special = True







		screen.fill(light_green)

		clock.tick(60)

		draw_taskbar()

		draw_l_hand_info(h_score, score, speed)

		# Draws new food
		if draw_new_food == True:
			valid_pos = False
			while not valid_pos: # Makes sure food doesn't spawn where the snake already is
				food = food_gen()
				food_x = food[0]
				food_y = food[1]
				food_x_c = food_x - food_radius # Converts food x and y to coords compatible with with snake x and y coords
				food_y_c = food_y - food_radius
				food_c = (food_x_c, food_y_c)
				if food_c not in pos_list:
					pg.draw.circle(screen, yellow, (food_x, food_y ), food_radius)
					valid_pos = True
					draw_new_food = False
					break
		else:
			pg.draw.circle(screen, yellow, (food_x, food_y), food_radius)



		if alive == True and paused == False:
			pos_list.append((snake_x, snake_y))
			pos_list_pos = 0
			removals = len(pos_list)-max_list
			while pos_list_pos < removals:
				try:
					pos_list.pop(pos_list_pos)

					pos_list_pos += 1
				except:
					break


		for pos_block in pos_list:
			pg.draw.rect(screen, red, (pos_block[0], pos_block[1], snake_size, snake_size))


		if (snake_x > food_x-(food_radius+snake_size) and snake_x < food_x+food_radius) and (snake_y > food_y-(food_radius+snake_size) and snake_y < food_y+food_radius): # Detects collision with food
			draw_new_food = True
			score += 1
			max_list += 5
		elif snake_x < 0 or snake_x > width-snake_size or snake_y > height-snake_size or snake_y < taskbar_out_height: # Detects if snake is outside edge of game
			game_over()
		elif (snake_x, snake_y) in pos_list[:-2]: # Detects if snake collides with itself
			game_over()
		elif run_special == True:
			game_over()
			

		# MOVE SNAKE
		if moving == "left" and alive == True:
			snake_x += -1*speed
			time.sleep(wait)
			can_move = True
			
		elif moving == "right" and alive == True:
			snake_x += speed
			time.sleep(wait)
			can_move = True
			
		elif moving == "up" and alive == True:
			snake_y += -1*speed
			time.sleep(wait)
			can_move = True
			
		elif moving == "down" and alive == True:
			snake_y += speed
			time.sleep(wait)
			can_move = True
			
		
		

		
		if special == True: #Draws the snake, based on every item in the pos/pause list
			segment = 0
			for pos_block in pos_list :
				pg.draw.rect(screen, red, (pos_block[0], pos_block[1], snake_size, snake_size))

				if segment % 2:
					pg.draw.rect(screen, red, (pos_block[0], pos_block[1], snake_size, snake_size))
				else:
					pg.draw.rect(screen, black, (pos_block[0], pos_block[1], snake_size, snake_size))
				segment += 1

		

		
		# print(str(int(clock.get_fps())))
		pg.display.update() 

new_game()

pg.QUIT()
