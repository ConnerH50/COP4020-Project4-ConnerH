import sys

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
            
    
    def writeDemo(self, fp):
        fp.write('(DEFUN demo()\n')
        fp.write('\t(setq fp (open "theString.txt" :direction :input))\n')
        fp.write('\t(setq l (read fp "done"))\n')
        fp.write('\t(princ "processing ")\n')
        fp.write('\t(princ l)\n')
        fp.write('\t(fsa l)\n')
        fp.write(')\n')
    
    def writeFSAFun(self, fp):
        fp.write('(DEFUN fsa(l)')