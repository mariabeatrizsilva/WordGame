import sys
import pygame
from argparse import ArgumentParser

from settings import Settings """ this file can contain overall setting of the game such as color scheme"""
from player import Player """this file will contain the class of the player object """ 
from xyz import XYZ
from XYZA import XYZA

class Main:
	"""This is the main class of the game. It is responsbile for running the game and contains/imports 
    		from other objects (the player, wordlist, etc)
    			 Attributes:
				difficululty (int) sets the level of difficulty for this game via an int value and based on that
				increases the speed of the target making it difficult to hit.
       			"""
#Arfa
	def __init__(self, difficulty):	
		"""This method creates an instane of the game and intializing the difficulty setting of the game. """
    		
		
  		pygame.init()
		self.settings = Settings(difficulty)

		# This code initializes the pygame library with the settings attribute of the screen
 		#from the Settings class. This code is used to set the screen's parameters height, width, etc 
		# the syntax was found using pygame codegrepper 
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width 
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("START THE GAME")
		self.bg_color = (220, 220, 230)
    
		# initializes the player and words(word list objects) (sprite object)
		self.player = Player(self)
		self.words = pygame.sprite.Group()
		self.target = Target(self)

	def _run_(self):
		""" determines based on events when we want to quit the game, and exit out of the game window, this code runs
  
  			side effects: pygame.quit shuts down pygame and sys.exit() shuts down the program """
     		
       		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self.keydown_events(event)
			elif event.type == pygame.KEYUP:
				self.keyup_events(event)

	def keydown_events(self, event):
    	 """responds to an event (key being pressed) 
      
      		Args:
        		event (int) a key being pressed
        	
         	Side effects:
          		changes the position of the Player""" 
            
        		
		if event.key == pygame.K_RIGHT:
			self.player.move_right = True
		elif event.key == pygame.K_LEFT:
			self.player.move_left = True 
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self.objectpositions()
		       
	def keyup_events(self, event):
		""" responds to an event (key being pressed) in this case, key up event
  	
   			Args:
      			event (int) represented by the keys being pressed """

		if event.key == pygame.K_RIGHT:
			self.splayerhip.move_right = False
		elif event.key == pygame.K_LEFT:
			self.player.move_left = False

		
	def start_game(self):
		"""Starts the main while loop of the game
  
		Side effects:
			calls methods of the Main class
  
		"""
		while True:
			self._run_()
			self.ship.update()
			self.target.update()
			self.update_objectpositions()
			self.update_screen()
 
	def update_objectsposition(self):
		"""updates the cannonball's position and deletes the cannonball from the 
  		cannonball list if it exits the screen
		
  		Side effects:
			Prints a message to the console if you successfully hit the target
			and removes a cannonball from the cannonballs attribute everytime
			you miss. 
   
		"""
		self.objectsposition.update()
		for cannonball in self.object_positions.copy():
				if cannonball.rect.bottom <= 0:
					self.objectposition.remove(update_objectsposition)
				
				elif cannonball.rect.bottom == self.target.rect.bottom and cannonball.rect.left > self.target.rect.left and cannonball.rect.right < self.target.rect.right:
					self.cannonballs.remove(CannonBall)
					print("You have hit the target you win!")
					sys.exit()
     		
	def fire_cannonball(self):
		"""initializes a new cannonball on the screen.
	
		Side effects:
			Prints a message if you run out of cannonballs without hitting
			the target. 
  
		"""	
		if len(self.cannonballs) < self.settings.cannonballs_allowed:
			new_cannonball = CannonBall(self)
			self.cannonballs.add(new_cannonball)
		else:
			print("You lose! You ran out of cannonballs")
			sys.exit()
		
	def update_screen(self):
		"""Redraws the screen with every pass through the loop
  
		"""
		self.screen.fill(self.settings.bg_color)
		self.target.blitme()
		self.ship.blitme()
		for cannonball in self.cannonballs.sprites():
			cannonball.draw_cannonball()

		pygame.display.flip()
  
def parse_args(arglist):
	"""Takes a difficulty from the user and sets the player and other object speed
		accordingly. (Parse command-line arguments)

	Args:
		arglist (list of str): arguments from the command line

	Returns:
		namespace: the parsed arguments
  
	"""
	parser = ArgumentParser()
	parser.add_argument("game_difficulty", help="Enter game difficulty (1, 2, 3, 4, 5)")
	return parser.parse_args(arglist)

def main(difficulty = 1):
	"""Creates an instance of the Main class

	Args:
		difficulty (int, optional): an integer from 1 to 5 setting the difficulty
  		of the game, defaults to 1.
	"""
	game = Main(difficulty)
	game.start_game()
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(int(args.game_difficulty))
