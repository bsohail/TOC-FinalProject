#!/usr/bin/python
import sys
import os


def main():

    prog = ""
    arg = "P2.py"
    exitCode = 0
    a = []
    for it in sys.argv:
        a.append(it)
    argsn = len(a)

    if (len(sys.argv) > 1):
        try:
            prog = sys.argv[1]
            if (argsn >= 3):
                arg = sys.argv[2]
                if(arg.endswith('.txt')):
                    rf = open(arg, "r")
                    if rf.mode == "r":
                        arg = rf.read()
                    rf.close()
                else:
                    arg = sys.argv[2]
            else:
                print("Only one argument present")
                arg = "P2.py"
            sys.exit(0)
        except SystemExit:
            print("")
        except:
            sys.exit(1)
    else:
        pass
    print(arg)
    arguments = 'python3 ' + prog + ' ' + arg

    exitCode = os.system(arguments)

    if (exitCode):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
