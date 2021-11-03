#!/usr/bin/python3
############################################################
# parse evernote saved mhtml file and extract notebook list.
# Uses regurlar expressions
# TODO:
#   * file splits on NOTEBOOK_TITLE tag, need to figure out
############################################################

import re
import argparse

default_file = 'data/evernote-notebooks.mhtml'

# pare arguments
parser = argparse.ArgumentParser(
    description='Find Evernote notebooks from mhtml file')
parser.add_argument('-f', '--file', type=str, help='file to parse',
                    default=default_file)
parser.add_argument('--bar', nargs='+',
                    help='one of the bars to be frobbled')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

args = parser.parse_args()

print("Start...")

# set input file
# if args.file:
#     infile = args.file
# else:
#     infile = 'data/evernote-notebooks.mhtml'
infile = args.file

with open(infile, 'rt') as myfile:
    linenum = 0
    pattern = ".*NOTEBOOK_TITLE\">(.*)</span>.*"

    for line in myfile:
        linenum += 1
        result = re.match(pattern, line)

        if result:
            # print("Search successful: " + line)
            # print("Search successful: " + str(linenum))
            # print("result.group() : ", result.group())
            # print("result.group(1) : ", result.group(1))
            print("notebook: " + result.group(1))
        # else:
        #     print("\tSearch unsuccessful.")


print("END")

# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")

# # print all the lines
# for line in myfile:
#     linenum += 1
#     print("Line " + str(linenum) + ": " + line)


# with open('logfile.txt', 'rt') as myfile:
#     for line in myfile:
#         linenum += 1
#         if pattern.search(line) != None:      # If a match is found
#             errors.append((linenum, line.rstrip('\n')))

# line = "Cats are smarter than dogs"

# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
