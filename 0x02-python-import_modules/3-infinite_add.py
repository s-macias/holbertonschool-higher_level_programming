#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    sum = 0
    for i in range(0, ac):
        sum += int(sys.argv[i])
    print("{:d}".format(sum))
