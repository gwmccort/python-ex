# extract CDATA from xml example
# uses dom & etree
# from: https://www.reddit.com/r/learnpython/comments/hhaiiu/parsing_xml_using_python_and_lxml_cdata_causing/

from io import StringIO
from lxml import etree

unparsed = '''
<card>
  <front lang="english">
    <![CDATA[<p class='basicCardFront'>Excuse me.</p>]]>
  </front>
  <back lang="english" audio="resources/applications/flashcards/assets/perdon.mp3">
    <![CDATA[<img src="resources/applications/flashcards/assets/imagename.jpg"/><p class='basicCardBack'>Perdón.</p>]]>
  </back>
 </card>
'''

stream = StringIO(unparsed)
parsed = etree.parse(stream)
for elt in parsed.xpath('//card/*[name()="front" or name()="back"]'):
    print(elt.text)
