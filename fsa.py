import sys
import tkinter as tk
#from guiMaker import GUIMaker
from transitions import Transitions
class FSA:

    def __init__(self, stateNum, alphabet, stateTransitons, startState, acceptStates):
        self.stateNum = stateNum
        self.alphabet = alphabet
        self.stateTransitons = stateTransitons
        self.startState = startState
        self.acceptStates = acceptStates
        self.currentState = int(self.startState)
        self.transitionArray = []
        #self.GUI = GUIMaker(self.getStateNum(), self.getAlphabet(), self.getStateTransitions(), self.getStartState(), self.getAcceptStates())
        self.transitionsValid = True

    def readInputFile(self, fileName):
        with open(fileName) as f:
            content = f.readline()
        self.input = content
        f.close()

    def makeTransitions(self):
        for transition in self.stateTransitons:
            transitionParameters = transition.split(':')

            if(((int(transitionParameters[0]) < 0) or (int(transitionParameters[0]) >= self.stateNum)) or ((int(transitionParameters[1]) < 0) or (int(transitionParameters[1]) >= self.stateNum))):
                self.transitionsValid = False

            self.transitionArray.append(Transitions(transitionParameters[0], transitionParameters[1], transitionParameters[2]))

    def showStateTransitions(self): 
        for i in range(0,len(self.stateTransitons)):
            print('State transition - ' + self.stateTransitons[i])

    def checkInAlpha(self, letter):
        for i in range(0, len(self.alphabet)):
            if(letter == self.alphabet[i]):
                return True
        return False

    def runFSA(self):
        self.makeTransitions()
        roundNum = 0

        for letter in self.input:
            roundNum = roundNum + 1
            if(self.checkInAlpha(letter) == False):
                print("Invalid letter. Input String %s is not accepted!" %self.getFileInput())
                return

            for i in range(0, len(self.transitionArray)):
                if(self.checkForValidState(self.transitionArray[i]) == False):
                    return
                if(self.checkforValidTransition(self.transitionArray[i], letter) == True):
                    break
            
        self.checkForAcceptState()
                
    def checkForAcceptState(self):

        if(self.transitionsValid == False):
            print("Invalid State or Transition, input %s is not accepted!" %self.getFileInput())
            return

        for state in self.getAcceptStates():
            if(self.currentState == int(state)):
                print("Input String %s accepted!" %self.getFileInput())
                return True
            else:
                pass
        print("Input String %s not accepted!" %self.getFileInput())
        return False

    def checkForValidState(self, transition):
        if(transition.isStateValid(self.stateNum) == False):
            return False
        return True

    def checkforValidTransition(self, transition, letter):
        if(transition.isTransitionValid(self.currentState, letter) == True):
            self.currentState = transition.getNextState()
            return True
        else:
            return False

    # def runGUIMaker(self):
    #     print("")
    #     # self.GUI.makeTransitions(self.transitionArray)
    #     # self.GUI.makeStates()
    #     # self.GUI.runGUI()

    def getStateNum(self):
        return self.stateNum

    def getAlphabet(self):
        return self.alphabet

    def getStateTransitions(self):
        return self.stateTransitons

    def getTransitionArray(self):
        return self.transitionArray

    def getStartState(self):
        return self.startState
    
    def getAcceptStates(self):
        return self.acceptStates

    def getFileInput(self):
        return self.input