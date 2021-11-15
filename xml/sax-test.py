##########################
# sax-test.py
##########################

# from io import StringIO
# import argparse
import xml.sax

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


def main():
    print("Start(main)...")

    # stream = StringIO(testXml)
    # print(stream.read())

    # # create a new content handler for the SAX parser
    # handler = SaxHandler()
    # xml.sax.parseString(testXml, handler)

    print("End: main()")


if __name__ == "__main__":
    main()
