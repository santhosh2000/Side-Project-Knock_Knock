import random
import sys
import os
import time
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

class Player:


	def __init__(self, game_id, player_id):
		if(player_id == None or game_id == None):
			raise AttributeError('Player object should be created with a valid game_id and player_id')			
		self.player_cards = []
		self.player_id = player_id
		self.game_id = game_id;
		self.winnerFlag = False;
			
		
	def getId(self):
		return self.player_id
		
	def getHand(self):
		return tostr(self.player_cards)
		
	def tostr(self):
		printstr = ""
		for card in self.player_cards:
			printstr += "%s\n"% card.__str__()
		return printstr

	def __str__(self):
		return '<Knock-Knock Player Object: player {}>'.format(self.player_id) + ' <in game {}>\n'.format(self.game_id) + self.tostr()
		
	def dropCard(self, openCard):
		index = 0
		if openCard is None:
			return None
		for card in self.player_cards:
			if(card.isMatch(openCard)):
				print('This is the matched card:' + str(card))
				return  self.player_cards.pop(index)
			index+=1



	def drawCard(self, card):
		if(card and card not in self.player_cards): 
			self.player_cards.append(card)
		return True


	def addCard(self, card):
		if(card and card not in self.player_cards): 
			self.player_cards.append(card)
		return True
		
	def play(self ,topCard):
			if self.dropCard(topCard) is None:
				return -1
			elif self.dropCard(topCard) and len(self.player_cards) == 1:				
				return 1
			elif self.dropCard(topCard) and len(self.player_cards) == 0:
				self.winnerFlag = True
				return 2
			else:
					return -2
			
				
		

		
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
	p = Player("1","Santhosh")
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
	h = Card(2,6)
	print(p.dropCard(h))
	print(p.dropCard(h))
	print(p.dropCard(h))
	i = Card(2,11)
	print(p.dropCard(i))

	#print(_getColor)
		
if __name__ == "__main__":
	main()
	print("Player Testcases completed successfully!")
		
	
		
	

	
