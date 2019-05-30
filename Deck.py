import random
import sys
import os
import time
scriptpath = "..\Knock_Knock\Card.py"
sys.path.append(os.path.abspath(scriptpath))
from Card import *


#SPECIALNUMBERS = list(range(11,14))
SPECIALSUITS = ['jack','queen','king','ace']
POWERUPS = [1,7,9,11]
CARDREALS = NUMBERS + SPECIALSUITS

class Deck:
	"""
		Each Deck object has Card objects with valid suits and values
	"""
	"""
		suit: string
		value: int
		color: string
		"""
	def __init__(self,shuffle = True):
		try:			
			self.cards = []
			self.numCards = 0
			self.__create()
			if( self.shuffle == True):
				self._shuffle()
		except AttributeError:
			raise AttributeError('Deck object should be created with a suit value ' + str(SUITS) + ' and a value [1-13]');
		
	def shuffle(self):
		random.shuffle(self.cards)
		
	def __create(self):
		self.cards = [Card(suit,value) for suit in SUITS for value in NUMBERS]
		self.numCards = int(len(self.cards))
		
	def isEmpty(self):
		return (self.numCards == 0)
		
	def __str__(self):
		printstr = ""
		for card in self.cards:
			printstr += "%s\n"% card.__str__()
		return printstr

	def size(self):	
		return self.numCards
		
	def pop(self):
		if not len(self.cards):
			self.shuffle()
		elif len(self.cards) == 0:
			raise AttributeError('Deck object should be created with cards first to pop');
		else:
			self.numCards-=1
		return self.cards.pop()
def main():
	d = Deck()
	print(d)
	d.shuffle()
	print(d)
	d.shuffle()
	print(d)
	print(d.size())
	print(d.isEmpty())
	
	print("** Popped card ***" + str(d.pop()))
	print(d)
	print (d.size())
	print (d.isEmpty())
	#print(_getColor)
		
if __name__ == "__main__":
	main()
	print("Deck Testcases completed successfully!")
		
	

	
