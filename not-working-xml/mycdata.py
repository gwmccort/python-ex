# extract CDATA from xml with SAX example

# import xml.sax

from io import StringIO

# from lxml import etree

xmlStr = '''
<card>
  <front lang="english">
    <![CDATA[<p class='basicCardFront'>Excuse me.</p>]]>
  </front>
  <back lang="english" audio="resources/applications/flashcards/assets/perdon.mp3">
    <![CDATA[<img src="resources/applications/flashcards/assets/imagename.jpg"/><p class='basicCardBack'>Perdón.</p>]]>
  </back>
 </card>
'''


# class EnexLexHandler(xml.sax.LexicalHandler):
#     # handle cdata
#     def startCDATA(self):
#         print("startCDATA")

def main():
    print("in main...")

    stream = StringIO(xmlStr)
    print(stream)
    print("end: main")


if __name__ == "__main__":
    main()
