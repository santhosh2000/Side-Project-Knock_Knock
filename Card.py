import random
import sys
import os
import numbers



SUITS = [1,2,3,4] # 1-> hearts, 2-> diamonds, 3-> clubs 4-> spades
NUMBERS = [1,2,3,4,5,6,7,8,9,10,11,12,13]
SUITSYMBOLS = {1:"\u2665", 2:"\u2666",3:"\u2663",4:"\u2660"}
#SPECIALNUMBERS = list(range(11,14))
SPECIALSUITS = {11: 'J',12: 'Q',13: 'K',1: 'A'}
POWERUPS = [1,7,9,11]
#CARDREALS = NUMBERS + SPECIALSUITS.keys()


class Card:
	"""
		Each Card object has a valid suit and value.	
	"""
	"""
		suit: string
		value: string
		color: string
		drawable : int
		skip : int
		associate: int
		changePow: int
		"""

	def __init__(self, suit, value):
		try:			
			self._check(suit,value)
			self.suit = suit;
			self.skip = 0;
			self.changePow = 0;
			self.drawable = 0;
			self.associate = 0;
			self.value = value
			if(self.value == 7):
				self.drawable = 2
			elif (self.value == 9):
				self.associate = 1
			elif (self.value == 11):
				self.changePow = 1
			elif (self.value == 1):
				self.skip = 1
		except AttributeError:
			raise AttributeError('Player Card object should be created with a suit value ' + str(SUITS) + ' and a value [1-13]');
		

	def _check(self,suit,value):
		"""
			Raises exception if color, or value, or suit isn't valid
		"""
		if value not in NUMBERS:
			raise AttributeError('Player Card object should be created with a suit value ' + str(SUITS) + ' and a value [1-13]');
		if suit not in SUITS:
			raise AttributeError('Player Card object should be created with a suit value ' + str(SUITS) + ' and a value [1-13]');


	def printCard(self):
		if self.value in SPECIALSUITS:
			print("┌───────┐")
			print("| {:<2}    |".format(SPECIALSUITS[self.value]))
			print("|       |")
			print("|   {}   |".format(SUITSYMBOLS[self.suit]))
			print("|       |")
			print("|    {:>2} |".format(SPECIALSUITS[self.value]))
			print("└───────┘") 
		else:
			print("┌───────┐")
			print("| {:<2}    |".format(self.value))
			print("|       |")
			print("|   {}   |".format(SUITSYMBOLS[self.suit]))
			print("|       |")
			print("|    {:>2} |".format(self.value))
			print("└───────┘") 
	
	
	def getSuit(self):
		return self.suit
		
	def getValue(self):
		return self.value
		
	def getColor(self):
		return self.color
		
	def getDrawable(self):
		return self.drawable
		
	def getAssociate(self):
		return self.associate
		
	def getChangePow(self):
		return self.changePow
		
	def getSkip(self):
		return self.skip
		
	def __eq__(self,other):
		if self is None:
			return False
		return (self.suit == other.suit and self.value == other.value)	
		
	def isMatch(self,other):
	
		return (self.suit == other.suit or self.value == other.value)


		
	def isSpecial(self):
		return self.value == 7 or self.value == 9 or self.value == 11 or self.value == 1 
		
	def isPlayable(self,other):
		  return self.value == other.value or self.color == other.color

	def cardPrint(self):
		printstr = ""
		if self.value in SPECIALSUITS:
			printstr+="┌───────┐\n"
			printstr+="| {:<2}    |\n".format(SPECIALSUITS[self.value])
			printstr+="|       |\n"
			printstr+="|   {}   |\n".format(SUITSYMBOLS[self.suit])
			printstr+="|       |\n"
			printstr+="|    {:>2} |\n".format(SPECIALSUITS[self.value])
			printstr+="└───────┘\n"	
		else:
			printstr+="┌───────┐\n"
			printstr+="| {:<2}    |\n".format(self.value)
			printstr+="|       |\n"
			printstr+="|   {}   |\n".format(SUITSYMBOLS[self.suit])
			printstr+="|       |\n"
			printstr+="|    {:>2} |\n".format(self.value)
			printstr+="└───────┘\n"	
		print(printstr)
		
	def __str__(self):
		printstr = ""
		if self.value in SPECIALSUITS:
			printstr+="|{:<2}".format(SPECIALSUITS[self.value])
			printstr+="{}| ".format(SUITSYMBOLS[self.suit])
		else:
			printstr+="|{:<2}".format(self.value)
			printstr+="{}| ".format(SUITSYMBOLS[self.suit])
			
		# if self.value in SPECIALSUITS:
		    # return (str(SPECIALSUITS[self.value]) + ' ' + str(self.suit) + ' ')
		# else:
		    # return (str(self.value) + ' ' + str(self.suit) + ' ')	
		return printstr
		
def main():
	c = Card(1,13)
	print(c)
	d = Card( 4,12)
	print(d)
	e = Card(3,11)
	f = Card(1,13)
	g = Card(2,13)
	print(g)
	g = Card(2,2)
	print(g)
	print(c == d)
	print(c == e)
	print(c.isMatch(d))
	print(c.isSpecial())
	print(e.isSpecial())
	#print(_getColor)
		
if __name__ == "__main__":
	main()
	print("Card Testcases completed successfully!")
	
