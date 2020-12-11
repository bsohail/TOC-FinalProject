#!/usr/bin/python

import sys


def main():

    n = 10
    if (len(sys.argv) > 1):
        try:
            n = int(sys.argv[1])
        except:
            print("Error: 1")
            sys.exit(1)

    else:
        n = 10

    try:
        for i in range(n):
            print(i)
        sys.exit(0)
    except SystemExit:
        print("")
    except:
        sys.exit(1)


if __name__ == "__main__":
    main()
