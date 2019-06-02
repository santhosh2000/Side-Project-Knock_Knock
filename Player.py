import random
import sys
import os
import time
import logging
scriptpath = "..\Knock_Knock\Card.py"
sys.path.append(os.path.abspath(scriptpath))
from Card import *
scriptpath = "..\Knock_Knock\Deck.py"
sys.path.append(os.path.abspath(scriptpath))
from Deck import *
from Game import *

SUITS = ['hearts','diamonds','spades','clubs']
NUMBERS = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
#SPECIALNUMBERS = list(range(11,14))
SPECIALSUITS = ['jack','queen','king','ace']
POWERUPS = [1,7,9,11]
CARDREALS = NUMBERS + SPECIALSUITS
logger = logging.getLogger("Player")

class Player:


	def __init__(self, game_id, player_id):
		if(player_id == None or game_id == None):
			raise AttributeError('Player object should be created with a valid game_id and player_id')
		# assert(not isinstance(game_id,int),'Player: Game_Id should be an int')
		# assert(not isinstance(player_id,str),'Player: Player_Id should be a string')
		self.player_cards = []
		self.player_id = player_id
		self.game_id = game_id;
		self.winnerFlag = False;
			
		
	def getId(self):
		return self.player_id
		
	def getLen(self):
		return len(self.player_cards)
		

	
	def printHand(self):
		printstr = ""
		for card in self.player_cards:
			printstr += "%s "% card.__str__()
		return printstr	
		


	def __str__(self):
		return '<Knock-Knock Player Object: player {}>'.format(self.player_id) + ' <in game {}>\n'.format(self.game_id) + self.printHand()
		
	def dropCard(self,game):
		index = 0
		isFound = False
		if(game.openCard() is None):
			raise AttributeError('Card is Empty')
		
		for card in self.player_cards:
			if(card.isMatch(game.openCard())):
				logger.debug('This is the matched card:' + str(card) + 'belonging to: ' + self.player_id)
				game.addOpenCard(card)
				self.player_cards.pop(index)				
				isFound = True
				return isFound
				
			index+=1
		logger.debug('There is no matched card for ' + str(card) + 'with ' + self.player_id)		
		return isFound



	def drawCard(self, card):
		if(card and card not in self.player_cards): 
			self.player_cards.append(card)
		return True


	def addCard(self, card):
		if(card and card not in self.player_cards): 
			self.player_cards.append(card)
		return True
		
	def play(self,game):
		match = self.dropCard(game)
		if (not match):
			self.drawCard(game.deck.pop())
			return match   	
		else:
			# if Knock-Knock: broadcast Knock-Knock
			if(self.getLen() == 1):
				game.knockKnock(self.player_id)				
			# else if no card: win (set Winner at Game Level)
			elif (self.getLen() == 0):
				game.setWinner(self.player_id)	
			# else: no ops
			else:
				pass
			return match
				
		

		
	 # power of EQU operator in Python
	def drawCard1(self, card):
		if(not card): 
			return False
		
		for c in self.player_cards:
			if c == card:			
				return False
			
		self.player_cards.append(card)
		return True			
		
	# def dropCard(self):
		# if(canPlay(self,
		
def main():
	p = Player(1,"Santhosh")
	print(p)

	d = Card(2,12)
	p.drawCard(d)
	#print(d)
	e = Card(3,11)
	p.drawCard(e)
	#print(e)
	f = Card(1,13)
	p.drawCard(f)
	g = Card(2,13)
	p.drawCard(g)
	print(p)
	
	deck = Deck()	
	p.drawCard(deck.pop())
	p.drawCard(deck.pop())
	p.drawCard(deck.pop())
	print(p)
	# h = Card(2,6)
	# print(p.dropCard(h))
	# print(p.dropCard(h))
	# print(p.dropCard(h))
	# i = Card(2,11)
	# print(p.dropCard(i))

	#print(_getColor)
		
if __name__ == "__main__":
	main()
	print("Player Testcases completed successfully!")
		
	
		
	

	
