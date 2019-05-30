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
scriptpath = "..\Knock_Knock\Player.py"
sys.path.append(os.path.abspath(scriptpath))
from Player import *



class Game():
    #playerIdentities = ('player1', 'player2', 'player3', 'player4')
    #computerNames = ('Santhosh', 'Divya', 'Sara', 'Mani')
    ID = 1
    def __init__(self):
        self.playerList = []  # 
        self.numPlayers = 0    
        self.gameId = 1
        self.openCards = []
        self.ID +=1
        self.deck = Deck()
        self.deck.shuffle()
        self.gameFlag = False
        
    def dealHand(self):
        """
        Return a list of 7 cards from the top of the deck, and remove these
        from the deck.
        """
        for i in range(7):
            for p in self.playerList:
                p.addCard(self.deck.pop())
        self.openCards.append(self.deck.pop())
                
    def sizeOfDeck(self):
        return self.deck.size()
        
    def sizeOfOpenCards(self):
        return len(self.openCards)
    
    
    def canBegin(self):
        return (self.numPlayers > 1)

    def addPlayer(self, player):
        self.playerList.append(player)
        self.numPlayers = len(self.playerList)

    def removePlayer(self, index):
        #index -= 1
        if(index in range(len(self.playerList))):
            del self.playerList[index]
            self.numPlayers = len(self.playerList)

    def endGame(self):
        self.numPlayers = 0
        self.playerList = []

    def getNumPlayers(self):
        return self.numPlayers
        
    def openCard(self):
        return self.openCards[-1]
        
    def addOpenCard(self,card):
        self.openCards.append(card)
        
    def play(self):
        while(self.gameFlag != True):
            for p in self.playerList:
                if (p.play(self.openCard()) == -1):
                    p.drawCard(self.deck.pop())
                elif (p.play(self.openCard()) == 1):
                    card = p.dropCard(self.openCard())
                    self.addOpenCard(card)
                    print('<Knock-Knock Player Object: player {}>'.format(p.player_id) + ' <in game {}>\n'.format(p.game_id) + ' is currently in Knock-Knock')    	
                elif (p.play(self.openCard()) == -2):
                    card = p.dropCard(self.openCard())
                    self.addOpenCard(card)
                else:
                    card = p.dropCard(self.openCard())
                    self.addOpenCard(card)
                    print('<Knock-Knock Player Object: player {}>'.format(p.player_id) + ' <in game {}>\n'.format(p.game_id) + ' has won!')
                    self.gameFlag = True
    	
                  
        self.endGame()     
                
        
    #def play(self):
        # if not canBegin():
           #print Error Message and return false
        #while winner hasn't been made , 
            #each player will play in turn: which will result in drawing or dropping card followed by win or just dropping card and telling Knock-Knock or skip                
				
        #while winner hasn't been made ,
            #continuous looping through the self.playerList[],
            #each Player Object has to choose between playing or dropping card
            #continuously update openCard list and append player dropped card to openCard list
        # check numPlayerCards before player puts down last card
        # if playerCard isMatch for open Card:
            # print ('Congratulations', Player_Id + "has won")
            # setWinner(playerIndex)
            # exit loop
        # else:
            # player draws card and game continues on to next player

        
        

def main():
    p = Player("1","Santhosh")
    print(p)
    f = Player("1","Divya")
    print(f)
    g = Game()
    g.addPlayer(p)
    g.addPlayer(f)
    g.dealHand()
    g.sizeOfDeck()
    g.sizeOfOpenCards()
    g.openCard()
    g.play()
    
    
    #print(_getColor)
        
if __name__ == "__main__":
    main()
    print("Game Testcases completed successfully!")

    
        

        
    
        
    

    
