#!/usr/bin/python3
############################################################
# parse evernote enex file
#
# # TODO: get CDATA
############################################################

import xml.sax
import argparse

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
default_infile = "data/evernote-inbox.enex"

# class EnexLexHandler(xml.sax.handler.LexicalHandler):
#     # handle cdata
#     def startCDATA(self):
#         print("startCDATA")


class EnexContentHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.noteCount = 0
        self.isInNote = False
        self.isInTitle = False

    # Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == "note":
            self.isInNote = True
            # print("Notebook title: " + attrs['title'])
        elif tagName == "title":
            self.isInTitle = True

    # Handle endElement
    def endElement(self, tagName):
        if tagName == "title":
            self.isInTitle = False
        elif tagName == "note":
            self.isInNote = False

    # Handle text data
    def characters(self, chars):
        # print("in characters()")
        if self.isInTitle:
            print("Note text: " + chars)
            self.isInNote = False  # TODO is this right???

    # Handle startDocument
    def startDocument(self):
        print("About to start in startDocument()!")

    # Handle endDocument
    def endDocument(self):
        print("Finishing up in endDocument()!")


# main function
def main():
    print("Start(main)...")

    # parse args
    argParser = argparse.ArgumentParser(
        description='Evernote enex file parser')
    argParser.add_argument('-f', '--file', type=str, help='file to parse',
                           default=default_infile)
    # parser.add_argument('--bar', nargs='+',
    #                     help='one of the bars to be frobbled')
    args = argParser.parse_args()
    infile = args.file

    # # create a new content handler for the SAX parser
    # handler = EnexContentHandler()
    # # call the parseString method on the XML text content received
    # xml.sax.parseString(testXml, handler)

    # try to handle cdata
    xmlParser = xml.sax.make_parser()
    xmlHandler = EnexContentHandler()
    xmlParser.setContentHandler(xmlHandler)
    xmlParser.parse()


if __name__ == "__main__":
    main()
