#!/usr/bin/python3
###########################################
# lxml-enex - example of using dom/lxml to parse
# evernote enex export file
#
# based on LIL Python XML JSON & web ch6
# lxml*.py
###########################################

from lxml import etree

infile = "data/evernote-inbox.enex"


def main():
    noteCount = 0
    titleCount = 0

    # get doc/dom from enex file
    root = etree.parse(infile)
    # doc = etree.fromstring(result.content)
    print(root)
    print(etree.tostring(root, pretty_print=True))

    # # Access the value of an attribute
    # print(doc.attrib['export-date'])

    # Iterate over note & get title
    for elem in root.findall('note'):
        titleEl = elem.find("title")
        print(titleEl.text)

    # Count the number of notes
    noteCount = len(root.findall("note"))
    titleCount = len(root.findall("note/title"))

    print("There were {0} note elements".format(noteCount))
    print("There were {0} title elements".format(titleCount))


if __name__ == "__main__":
    main()
