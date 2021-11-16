#!/usr/bin/python3
##########################
# sax-test.py
##########################

# from io import StringIO
import argparse
import xml.sax
import pprint

infile = None
default_infile = "data/sample.xml"


class SaxHandler(xml.sax.ContentHandler):

    # list of notes in enex file
    notes = []
    noteTitle = ""

    def __init__(self):
        # init instance vars
        self.isInTitle = False

    # Handle startElement
    def startElement(self, tagName, attrs):
        # print("StartTag:" + tagName)

        if tagName == "title":
            # print("Title:" + tagName)
            self.isInTitle = True
            self.noteTitle = ""

    # Handle endElement
    def endElement(self, tagName):
        # print("EndTag:" + tagName)

        if tagName == "title":
            # print("endElement: setting isInTitle to False")
            self.isInTitle = False
            self.notes.append(self.noteTitle)
            print(self.noteTitle)  # TODO: add to a list & getter

    # Handle text data

    def characters(self, chars):
        # print("in characters()")
        if self.isInTitle:
            # print("Note text: " + chars)
            self.noteTitle += chars


def parseArgs():
    print("in parseArgs")

    global infile

    # parse args
    argParser = argparse.ArgumentParser(
        description='xml file parser with sax')
    argParser.add_argument('-f', '--file', type=str, help='file to parse')
    args = argParser.parse_args()

    # set input file if on command line
    if (args.file is not None):
        print("setting infile to arg")
        infile = args.file


def main():
    print("Start(main)...")

    parseArgs()

    # create a new content handler for the SAX parser
    handler = SaxHandler()
    if (infile is None):
        # use a string for xml input
        xml.sax.parseString(testXml, handler)
        # xml.sax.parse(testXml, handler) #TODO: can i just use parse????
    else:
        # use given file as xml input
        xml.sax.parse(infile, handler)

    print("End: main()")


############
# test data
testXml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export4.dtd">
<notebook>
    <note>
        <title>note title 1</title>
    </note>
    <note>
        <title>note title 2</title>
    </note>
    <![CDATA[<p class='basicCardFront'>Excuse me.</p>]]>
</notebook>
"""

if __name__ == "__main__":
    main()
