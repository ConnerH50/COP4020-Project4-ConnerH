import sys
from transitions import Transitions

class LispMaker: 

    def __init__():
        print("")

    def __init__(self, stateNum, alphabet, stateTransitons, transitionArray, startState, acceptStates):
        print("")
        self.stateNum = stateNum
        self.alphabet = alphabet
        self.stateTransitons = stateTransitons
        self.transitionArray = transitionArray
        self.startState = startState
        self.acceptStates = acceptStates

    def writeFile(self):
        with open('part2.lsp', 'w') as fp:
            self.writeDemo(fp)
            self.writeFSAFun(fp)
            self.writeStates(fp)
            
    
    def writeDemo(self, fp):
        fp.write('(DEFUN demo()\n')
        fp.write('\t(setq fp (open "theString.txt" :direction :input))\n')
        fp.write('\t(setq list (read fp "done"))\n')
        fp.write('\t(princ "processing ")\n')
        fp.write('\t(princ list)\n')
        fp.write('\t(fsa list)\n')
        fp.write(')\n\n')
    
    def writeFSAFun(self, fp):
        fp.write('(DEFUN fsa(list)\n')
        fp.write('\t(cond \n')
        fp.write('\t\t((null list) (princ "String invalid"))\n')
        fp.write(f'\t\t(t(state{self.startState} list))\n')
        fp.write('\t)\n')
        fp.write(')\n\n')

    def writeStates(self, fp):
        for i in range(0, self.stateNum):
            fp.write(f'(DEFUN state{i}(list)\n')
            fp.write('\t(cond \n')

            if(self.checkAcceptState(i) == 1):
                fp.write(f'\t\t((null list) (princ "State {i} String Accepted!"))\n')
            else:
                fp.write(f'\t\t((null list) (princ "State {i} String Rejected!"))\n')

            self.writeTransitionCode(i, fp)

            fp.write('\t)\n')
            fp.write(')\n\n')

    def checkAcceptState(self, i):
        for acceptState in self.acceptStates:
                if(str(i) == acceptState):
                    return 1
        return 0

    def writeTransitionCode(self, i, fp):
        for transitions in self.transitionArray:
            if(i == transitions.getStartState()):
                fp.write(f'\t\t((equal \'{transitions.getTransitionChar()} (car list)) (state{transitions.getNextState()}(cdr list)))\n')