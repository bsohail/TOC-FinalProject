#!/usr/bin/python
import sys
import os

# Define main() function


def main():
    count = 0
    # Defining variables for user-entered arguments
    prog = ""
    arg = "P2.py"
    # Exit code of the program
    exitCode = 0
    # Defining a list to save the user-entered arguments
    a = []
    for x in sys.argv:
        a.append(x)
    # Length of the array 'a'
    argsn = len(a)
    # If arguments are present (i.e. Arguments are entered in the command line)
    if (len(sys.argv) > 1):
        try:
            # Saving the first argument in a variable
            prog = sys.argv[1]
            # If the second argument is present
            if (argsn >= 3):
                arg = sys.argv[2]
                # Checking if the 2nd argument is a txt file to read the file
                if(arg.endswith('.txt')):
                    # Reading the content of the file
                    rf = open(arg, "r")
                    if rf.mode == "r":
                        arg = rf.read()
                    rf.close()
                # The argument stays the same if no txt file is found
                else:
                    arg = sys.argv[2]
            # If the user does not enter the second argument
            else:
                # Setting 2nd argument to a default value
                arg = "P2.py"
            # system exits on code 0 if program runs successfully
            count += 1
            sys.exit(0)
        # Except block to avoid System exit
        except SystemExit:
            print("")
        except:
            sys.exit(1)
    else:
        sys.exit(1)
    # Print Statements to show the program is running
    print("Running.")
    print("Running..")
    print("Running...")

    # Running the program inside P2.py
    arguments = 'python3 ' + prog + ' ' + arg
    exitCode = os.system(arguments)

    # Checking the exit code and printing the output
    if (exitCode):
        print("NO")
    else:
        print("YES")


# Running the program
if __name__ == "__main__":
    main()
    sys.exit(0)
