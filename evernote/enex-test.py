#!/usr/bin/python3
###########################################
# sax-test - example of using sax to parse
# evernote enex export file
###########################################

# from io import StringIO
import argparse
import xml.sax
# import pprint

infile = None
default_infile = "data/evernote-inbox.enex"


# sax handler for evernote enex data
class EnexSaxHandler(xml.sax.ContentHandler):

    # list of notes in enex file
    notes = []
    noteTitle = ""

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

    # Handle text data
    def characters(self, chars):
        # print("in characters()")
        if self.isInTitle:
            # print("Note text: " + chars)
            self.noteTitle += chars

    def __init__(self):
        # init instance vars
        self.isInTitle = False


def parseArgs():

    global infile

    # parse args
    argParser = argparse.ArgumentParser(
        description='xml file parser with sax')
    argParser.add_argument('-f', '--file', type=str, help='file to parse')
    args = argParser.parse_args()

    # set input file if on command line
    if (args.file is not None):
        infile = args.file


def main():
    parseArgs()

    # create a new content handler for the SAX parser
    handler = EnexSaxHandler()
    enexParser = xml.sax.make_parser()
    enexParser.setContentHandler(handler)

    if (infile is None):
        # use string for xml input
        xml.sax.parseString(testXml, handler)
    else:
        # read file for xml input
        enexParser.parse(infile)

    # print all note titles
    for note in handler.notes:
        print(note)


############
# test data
testXml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export4.dtd">
<en-export export-date="20211204T204723Z" application="Evernote" version="10.24.3">
    <note>
        <title>&quot;O Death&quot; Traditional Banjo Lesson</title>
        <content>
            <![CDATA[some banjo tabs]]>
    </content>
    </note>
    <note>
        <title>Accessing a Server through Relay | Plex Support</title>
        <content>
             <![CDATA[<p class='basicCardFront'>Excuse me.</p>]]>
        </content>
    </note>
     <note>
        <title>Last title in test enex</title>
        <content>
             <![CDATA[cdata for last title]]>
        </content>
    </note>
</en-export>
"""

if __name__ == "__main__":
    main()
