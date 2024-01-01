'''
Vishrutha Gopa
SNAKES AND LADDERS BOARD GAME
Python
'''

'''
FEATURES IMPLEMENTED:
1. Numbered Tiles: all squares numbered using a pygame.font
2. Exact Requirements: players can't move past the end of the board

EXTRA FEATURE THAT IS NECESSARY SO THE GAME WORKS: Snake Connections
Because the board game has 110 squares and uses two 6-sided dice, a player cannot win when they are on square 109. 
Since the minimum total dice roll is 2, the player would have to move past the end of the board, but this is no longer possible because I implemented the 'Exact Requirements' feature. 
The player would therefore be stuck on square 109. The game would never end if both players became stuck on this square.
To resolve this issue, I added a 'snake' that moves the player to a different square when they land on square 109.
'''

def create_board():
    ''' 
    Create the checkerboard with the numbered tiles and snake connections

	Params:
		n/a	  
	Return:
		n/a

    
    '''

	# Intialization
    current_colour = white_colour

	#Fill the screen with light yellow
    screen.fill((255, 255, 224))

	# Set the screen caption
    pygame.display.set_caption("Board Game")

	#Draw the checkerboard
    for i in range(0, h_in_squares+1):
        for j in range(0, w_in_squares+1): #why +1??

            pygame.draw.rect(screen, current_colour, (i * square_dim, j * square_dim, square_dim, square_dim))
			
			#Switch colours
            if current_colour == white_colour:
                current_colour = blue_colour
            else:
                current_colour = white_colour
	
    # Number all squares	
    number_tiles()
    
    # Drawing certain squares that returns players to other squares
    snake_tiles()

	#Update display
    pygame.display.update()	

def number_tiles():
    """
	Number all tiles using pygame.font    
    
	Params:
		n/a	  
	Return:
		n/a
	"""

	# Intialization
    square_numbering = 1

	# Load a font
    font = pygame.font.SysFont("verdana",10)

	
    for i in range(0, h_in_squares):
        for j in range(0, w_in_squares): 
			
			# Render text for square numbering
            text = font.render(str(square_numbering), True, (black_colour))
			
			# Draw text for square numbering
            screen.blit(text, (j * square_dim, i * square_dim))

			# Increment by 1	
            square_numbering += 1

	# Update display 
    pygame.display.update()	

def snake_tiles():
	'''
    Wrting text on certain squares that returns players to other squares
	Params:
		n/a	  
	Return:
        n/a

    '''
    
    # Load a font
	font = pygame.font.SysFont("verdana",7)

	# Render text
	snake1 = font.render("Move to sq.20", True, (red_colour))
	snake2 = font.render("Move to sq.35", True, (red_colour))
	snake3 = font.render("Move to sq.107", True, (red_colour))

	# Draw text on square 54 to make player move to square 20
	screen.blit(snake1, (3 * square_dim, 5 * square_dim+10))
    
	# Draw text on square 95 to make player move to square 35
	screen.blit(snake2, (4 * square_dim, 9 * square_dim+10))

	# Draw text on square 109 to make player move to square 107
	screen.blit(snake3, (8 * square_dim, 10 * square_dim+10))

    # Update display 
	pygame.display.update()	

def dice_roll():
	'''
    Roll the two 6-sided dice using the random library

	Params:
		n/a	  
	Return:
		totalRoll -- Sum of the two 6-sided dice

    '''	

    #Import random library
	import random

    # Calculate and print out the rolled number with its sum
	roll1 = random.randint(1,6)
	roll2 = random.randint(1,6)
	totalRoll = roll1 + roll2 
	print (f"Rolled: {roll1} + {roll2} = {totalRoll}")
	
    #Return the sum of the two dice rolls
	return totalRoll

def x_and_y_values (player_square, token):
    '''
    Calculating the x and y values based on the square the player is on
	Params:
		player_square   -- Number of player's square
        token           -- Current player's turn
	Return:
        Position of x and y value of the current player
    '''

    #Calculating the row and column a player is on
    row = ((player_square -1) // 10)
    column = ((player_square -1) % 10)

    #Calculating the player's x and y values
    player_x = (column *50) 
    player_y = (row *50) + 25

    # Position of x value changes depending on players so the tokens do not overlap eachother entirely
    if (token == "Player Purple"):
        return player_x+30, player_y
    elif(token == "Player Green"):
        return player_x+15, player_y

def draw_players(player1_square, player2_square):
    '''
    Drawing the player's token (circle)

	Params:
		player1_square  -- Current square of player 1
        player2_square  -- Current square of player 2
	Return:
        n/a
    '''     
    #Radius of player tokens
    radius = square_dim//2 - 12

    #Draw purple token (player 1)
    pygame.draw.circle(screen, purple_colour, (x_and_y_values(player1_square,"Player Purple")), radius)

    #Draw green token (player 2)
    pygame.draw.circle(screen, green_colour, (x_and_y_values(player2_square, "Player Green")), radius)


# Import the pygame and sys library
import pygame
import sys

# Initialize the pygame 
pygame.init()

# Size of the board (even and then odd??)
w_in_squares = 10
h_in_squares = 11

# Size of a square
square_dim = 50

# Create the screen
screen = pygame.display.set_mode((w_in_squares*square_dim, h_in_squares*square_dim))

# RGB colours
white_colour = (240, 246, 244)
black_colour = (0, 0, 0)
blue_colour = (192, 215, 229)
red_colour = (255,0,0)
purple_colour = (153, 50, 204)
green_colour = (46, 139, 87)

# Current player turn intialization
current_turn = "Player Purple"

# Create the board by calling the function
create_board()

#Initial square number of players
player1_square = 1
player2_square = 1

# Player tokens at intial starting position
draw_players(player1_square, player2_square)

#Update and pause the screen
pygame.display.update()
pygame.time.delay(3000)

print ("Player 1 is purple and Player 2 is green \n")

while (True):
    print(current_turn)
    roll = dice_roll()

    # Redraw the board to remove the old positions of the player's tokens
    create_board()

    # When current turn is purple's
    if(current_turn == "Player Purple"):

        #Add the roll to the player's square
        player1_square += roll
        print(f"Moved to square: {player1_square}")

        #Player cannot can't move past the end of the board
        if player1_square > 110:
            player1_square -= roll
            print("COULD NOT MOVE THAT FAR! TRY AGAIN NEXT TURN")

        #Snake connections feature: when player moves to certain squares, it is returned to other squares
        if (player1_square == 54 or player1_square == 95 or player1_square == 109):
            
            # Draw the tokens of the players before moved by the snake connection then delay and redraw board and then new player token
            draw_players(player1_square, player2_square)
            pygame.display.update()
            pygame.time.delay(4000)
            create_board()
            
            if player1_square == 54:
                player1_square = 20
            if player1_square == 95:
                player1_square = 35
            if player1_square == 109:
                player1_square = 107
            print(f"'Snake' moves player to square {player1_square}")

        # Draw the tokens of the players
        draw_players(player1_square, player2_square)

        #Alternate turns
        current_turn = "Player Green"
    

    # When current turn is green's
    else:
        
        #Add the roll to the player's square
        player2_square += roll
        print(f"Moved to square: {player2_square}")

        #Player cannot can't move past the end of the board
        if player2_square > 110:
            player2_square -= roll
            print("COULD NOT MOVE THAT FAR! TRY AGAIN NEXT TURN")
        
        #Snake connections feature: when player moves to certain squares, it is returned to other squares
        if (player2_square == 54 or player2_square == 95 or player2_square == 109):
            
            # Draw the tokens of the players before moved by the snake connection then delay and redraw board
            draw_players(player1_square, player2_square)
            pygame.display.update()
            pygame.time.delay(4000)
            create_board()

            if player2_square == 54:
                player2_square = 20
            if player2_square == 95:
                player2_square = 35
            if player2_square == 109:
                player2_square = 107
            print(f"'Snake' moves player to square {player2_square}")

        # Draw the tokens of the players
        draw_players(player1_square, player2_square)

        #Alternate turns
        current_turn = "Player Purple"


    if(player1_square == 110 or player2_square == 110):
        print("WON! YAY!")
        break

    #Update display
    pygame.display.update()
    pygame.time.delay(3000)
    print()

#Update display
pygame.display.update()

# Keep pygame window open until the user chooses to closes it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
