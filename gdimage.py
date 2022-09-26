import sys
from basefunc import *

loadFuncList()
if len(sys.argv) == 1:
    printHelp()
else:
    for i in paraSplit(sys.argv):
        cmd = '%s(*%s)' % (paraMap[i[0]], i[1:])
        exec(cmd)