##########################
# sax-test.py
##########################

# from io import StringIO
# import argparse
import xml.sax


class SaxHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.noteCount = 0
        self.isInNote = False
        self.isInTitle = False

    # Handle startElement
    def startElement(self, tagName, attrs):
        print("StartTag:" + tagName)

    # Handle endElement
    def endElement(self, tagName):
        print("EndTag:" + tagName)


def main():
    print("Start(main)...")

    # create a new content handler for the SAX parser
    handler = SaxHandler()
    xml.sax.parseString(testXml, handler)

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
