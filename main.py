#Conner Hendricks COP4020 Project 4
import sys
from fileReader import FileReader
from fsa import FSA
from lispMaker import LispMaker

reader = FileReader(sys.argv[1])
reader.run()

fsa = FSA(reader.getStateNum(), reader.getAlphabet(), reader.getTransitionStates(), reader.getStartState(), reader.getAcceptStates())

fsa.makeTransitions()

fsa.runLispMaker()