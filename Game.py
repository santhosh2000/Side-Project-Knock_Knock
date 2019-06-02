import random
import sys
import os
import time
import logging
# scriptpath = "..\Knock_Knock\Card.py"
# sys.path.append(os.path.abspath(scriptpath))
from Card import *
# scriptpath = "..\Knock_Knock\Deck.py"
# sys.path.append(os.path.abspath(scriptpath))
from Deck import *
# scriptpath = "..\Knock_Knock\Player.py"
# sys.path.append(os.path.abspath(scriptpath))
from Player import *
logger = logging.getLogger("Game")


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
        self.winner = False # Flag which denotes if the Game was won
        
    def dealHand(self):
        """
        Return a list of 7 cards from the top of the deck, and remove these
        from the deck.
        """
        for i in range(2):
            for p in self.playerList:
                p.addCard(self.deck.pop())
        self.openCards.append(self.deck.pop())
                
    def sizeOfDeck(self):
        return self.deck.size()
        
    def sizeOfOpenCards(self):
        return len(self.openCards)
    
    def gameId(self):
        return self.gameId

    
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
        
    def setWinner(self, player_id):
        logger.info('<Knock-Knock Player Object: player {}>'.format(player_id) + ' has won!')
        self.winner = True    
        self.endGame()
        
        
    def knockKnock(self, player_id):
        logger.info('<Knock-Knock Player Object: player {}>'.format(player_id) + 'is going to win!')        
        for p in self.playerList:
            if(p.getId() != player_id):
                logger.debug('<Knock-Knock Player Object: player {}>'.format(player_id) + 'is going to win!')                        

        
    def play(self):
        while(self.winner != True):
            for p in self.playerList:
                p.play(self)
                if self.winner :
                    break
                # if(p.play(self) == 2):
                    # self.setWinner(p)
                # elif (p.play(self) == 1):
                    # # for card in g.openCards:
                        # # print (card.__str__() + "\n")
                    # print('<Knock-Knock Player Object: player {}>'.format(p.getId()) + ' is in Knock-Knock!')

                
        
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
    formatter=' %(asctime)s : %(module)s: %(levelname)s: %(message)s'
    logging.basicConfig(handlers=[logging.FileHandler('Game.log','w','utf-8')], level=logging.DEBUG,format=formatter)
    p = Player("1","Santhosh")
    logger.debug(p)
    f = Player("1","Divya")
    logger.debug(f)
    g = Game()
    g.addPlayer(p)
    g.addPlayer(f)
    g.dealHand()
    logger.debug(p)
    logger.debug(f)
    g.sizeOfDeck()
    g.sizeOfOpenCards()
    logger.info('This is current open card' + str(g.openCard()))
    for card in g.openCards:
        logger.debug (card.__str__() + "\n")
    response = input(":)")
    g.play()
    response = input(":)")
    
    for card in g.openCards:
        logger.debug (card.__str__() + "\n")
    
    
    #print(_getColor)
        
if __name__ == "__main__":
    main()
    logger.debug("Game Testcases completed successfully!")

    
        

        
    
        
    

    
