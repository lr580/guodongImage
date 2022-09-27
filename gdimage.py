import sys
from basefunc import *

loadFuncList()
if len(sys.argv) == 1:
    printHelp()
else:
    for i in paraSplit(sys.argv):
        funName = paraMap[i[0]]
        exec('from mod.%s import %s' % (funName, funName))
        exec('%s(*%s)' % (funName, i[1:]))
