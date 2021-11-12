# parse XML data using the SAX parser

# import requests
import xml.sax

# define the ContentHandler subclass for our content


class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.noteCount = 0
        self.isInNote = False

    # Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == "notebook":
            print("Notebook title: " + attrs['title'])
        elif tagName == "note":
            self.noteCount += 1
            self.isInNote = True

    # # Handle endElement
    # def endElement(self, tagName):
    #     if tagName == "title":
    #         self.isInTitle = False

    # Handle text data
    def characters(self, chars):
        if self.isInNote:
            print("Note text: " + chars)
            self.isInNote = False  # TODO is this right???

    # Handle startDocument
    def startDocument(self):
        print("About to start in startDocument()!")

    # Handle endDocument
    def endDocument(self):
        print("Finishing up in endDocument()!")


def main():
    # create a new content handler for the SAX parser
    handler = MyContentHandler()

    myxml = """
    <notebook title="notebook title">
    <note>note1</note>
    <note>note2</note>
    </notebook>
"""

    # call the parseString method on the XML text content received
    xml.sax.parseString(myxml, handler)

    # when we're done, print out some interesting results
    print("There were {0} notes elements".format(handler.noteCount))


if __name__ == "__main__":
    main()
