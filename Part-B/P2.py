#!/usr/bin/python

import sys
import os
prog = ""
arg = "P2.py"
exitCode = 0
print("program")
if (len(sys.argv) > 1):
    try:
        prog = sys.argv[1]
        # print(sys.argv[2])
        print("Only one argument present")
        if (sys.argv[2]):
            arg = sys.argv[2]
            if(arg.endswith('.txt')):
                print("Inside")
                rf = open(arg, "r")
                if rf.mode == "r":
                    arg = rf.read()
                    # print(arg)
                rf.close()
            else:
                arg = sys.argv[2]
        else:
            counter = 1
            arg = "P2.py"
    except IndexError:
        print("")
    except:
        sys.exit(1)
else:
    pass
print(arg)
arguments = 'python3 ' + prog + ' ' + arg
exitCode = os.system(arguments)
print(exitCode)
if (exitCode):
    print("NO")
else:
    print("YES")
