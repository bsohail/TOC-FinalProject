#!/usr/bin/python

import sys
import os
prog = "P2"
arg = "100"
if (len(sys.argv) > 1):
    try:
        prog = sys.argv[1]
        print(sys.argv[2])
        if (len(sys.argv) > 2):
            if (type(arg) == str):
                arg = sys.argv[2]
                rf = open(arg, "r")
                if rf.mode == "r":
                    arg = rf.read()
    except IndexError:
        arg = "100"
    except:
        sys.exit(1)
else:
    prog = "P2"
arguments = 'python3 ' + prog + ' ' + arg

exitCode = os.system(arguments)
if (exitCode):
    print("NO")
else:
    print("YES")
