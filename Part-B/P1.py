#!/usr/bin/python

import sys
# Define main() function


def main():

    n = 10
    # If an argument is present
    if (len(sys.argv) > 1):
        try:
            # Setting the argument to n and type casting to int
            n = int(sys.argv[1])
        except:
            # If error occurs, return exit code 1
            sys.exit(1)
    # if no argument is present set n to a default number
    else:
        n = 10

    try:
        # For loop to print the first n positive integers less than n
        for i in range(n):
            print(i)
        sys.exit(0)
    # Except block to avoid System exit
    except SystemExit:
        print("")
    except:
        sys.exit(1)


# Running the program
if __name__ == "__main__":
    main()
