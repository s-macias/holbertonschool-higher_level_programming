#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    if ac == 0:
        print("{:d} arguments.".format(ac))
    elif ac == 1:
        print("{:d} argument:\n{:d}: {:s}".format(ac, ac, sys.argv[1]))
    else:
        print("{:d} arguments:".format(ac))
    for i in range(0, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
