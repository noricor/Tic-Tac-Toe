#!/usr/bin/env python

"""
A very basic Tic-Tac-Toe solver

This very basic program makes use of the Minimax algorithm to find the best move
"""

################################################################################  
# Imports

import copy
from collections import deque

################################################################################  
# Constant definitions

PLY_DEPTH = 6

################################################################################  
# Function definitions

class GameState:

    def __init__(self, state, player):
        self._state = state             
        self._player = player
                
    def getNextStates(self, player):        
        if self.isFinal():
            return []           
        next_states = []
        for i in range(0,9):
            if self._state[i] == ' ':
                next_state = copy.deepcopy(self._state)             
                next_state[i] = player                      
                next_states.append(GameState(next_state, player))       
        return next_states
                
    def getPlayer(self):
        return self._player

    def isDraw(self, player):
        return (self.isWinn(player)==False) and (self.isLoose(player)==False) and (self.isFinal()==True)
        
    def isWinn(self, player):
        winner = self.hasWinner()
        if winner == player:
            return True
        return False

    def isLoose(self, player):
        winner = self.hasWinner()
        if winner!=None and winner!=player: 
            return True
        return False
        
    def isFinal(self):  
        if self.hasWinner():
            return True 
        for i in self._state:
            if i == " ":
                return False                
        return True 
        
    def getScore(self, player):
        if self.isWinn(player):
            return 5
        elif self.isDraw(player):
            return 0
        elif self.isLoose(player):
            return -5
        else:
            return 0
                
    def hasWinner(self):
        if (self._state[0]=='X' or self._state[0]=='O') and self._state[0]==self._state[1]==self._state[2]:
            return self._state[0]
        elif (self._state[3]=='X' or self._state[3]=='O') and self._state[3]==self._state[4]==self._state[5]:
            return self._state[3]
        elif (self._state[6]=='X' or self._state[6]=='O') and self._state[6]==self._state[7]==self._state[8]:
            return self._state[6]
        elif (self._state[0]=='X' or self._state[0]=='O') and self._state[0]==self._state[3]==self._state[6]:
            return self._state[0]   
        elif (self._state[1]=='X' or self._state[1]=='O') and self._state[1]==self._state[4]==self._state[7]:
            return self._state[1]   
        elif (self._state[2]=='X' or self._state[2]=='O') and self._state[2]==self._state[5]==self._state[8]:
            return self._state[2]   
        elif (self._state[0]=='X' or self._state[0]=='O') and self._state[0]==self._state[4]==self._state[8]:
            return self._state[0]   
        elif (self._state[2]=='X' or self._state[2]=='O') and self._state[2]==self._state[4]==self._state[6]:
            return self._state[2]   
        else:
            return None

    def printState(self):
        print ""
        print "Player: ", self._player, ", Winner: ", self.hasWinner()
        print "-------------"
        print "|", self._state[0], "|", self._state[1], "|", self._state[2], "|"
        print "-------------"
        print "|", self._state[3], "|", self._state[4], "|", self._state[5], "|"
        print "-------------"
        print "|", self._state[6], "|", self._state[7], "|", self._state[8], "|"
        print "-------------"               

        
def bestMove(state, player, opponent):
    original_player = player
    move, score = minimax(state, PLY_DEPTH, player, opponent, original_player)
    return move

def minimax(state, ply, player, opponent, original_player):
    best = (None, None)
    if ply==0 or state.isFinal():
        score = state.getScore(original_player)
        return [None, score]
    for next_state in state.getNextStates(player):
        move, score = minimax(next_state, ply-1, opponent, player, original_player)
        if player == original_player:
            if best[1]==None or score > best[1]:
                best = (next_state, score)
        else:
            if best[1]==None or score < best[1]:
                best = (next_state, score)              
    return best


################################################################################
# Main program starts here

state = GameState(['X',' ',' ', ' ','X',' ', ' ',' ','O'], 'X')

while True: 

    state.printState()

    opponent = state.getPlayer()
    player = ('O' if opponent=='X' else 'X')

    state = bestMove(state, player, opponent)
    if state == None:
        break   

