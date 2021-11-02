#!/usr/bin/python3
import re


def main():
    print("Start: main")

    linenum = 0
    with open('data/logfile.txt', 'rt') as myfile:
        for line in myfile:
            linenum += 1
            print("Line " + str(linenum) + ": " + line)

    print("End: main")


if __name__ == "__main__":
    main()
