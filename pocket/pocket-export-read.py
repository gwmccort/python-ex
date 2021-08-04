#
# read pocket export html file
#

# import the HTMLParser module
from html.parser import HTMLParser

# globals
tags = set()  # set of tags
links = {}  # dict of links & tags
# class PocketEntry():
#     __link
#     __tags


class PocketEntry():
    link = ""
    tags = []

    # def __init__(self):
    #     # null
    #     link = ""
    #     tags = []

    def __init__(self, link, tags):
        self.link = link

# create a subclass of HTMLParser and override the handler methods


class PocketExportParser(HTMLParser):

    # all unique tags
    tags = set()

    # pocket bookmarks TODO: make a static variable?
    entries = []

    @staticmethod
    def getentries():
        return PocketExportParser.entries

    def gettags(self):
        return tags

    # overide start tag handler
    def handle_starttag(self, tag: str, attrs):

        # process 'a' link tags
        if tag == "a":

            # TODO: do i need this?
            entry = PocketEntry(None, None)

            # loop thru attrs to find links & tags
            for a in attrs:

                # find links (ie href's)
                if (a[0] == "href"):
                    # lnk = a[1]
                    # links[lnk] = {}
                    entry.link = a[1]
                    self.entries.append(entry)

                # print(entry)

                # find tags
                if (a[0] == "tags"):
                    ts = a[1]
                    if ts:
                        for t in ts.split(","):
                            self.tags.add(t)


def main():
    global tags

    # instantiate the parser and feed it some HTML
    parser = PocketExportParser()

    # open the sample HTML file and read it
    f = open("pocket-export.html")
    if f.mode == "r":
        contents = f.read()  # read the entire file
        parser.feed(contents)

    f.close()

    # # TODO: fix class visibility of entries
    # for e in parser.entries:
    #     print(e.link)

    entries = PocketExportParser.getentries()
    for e in entries:
        print(e.link)

    # print(parser.entries)

    # print(links)

    # TODO: use method, don't just get class data
    for t in PocketExportParser.tags:
        print(t)
    # print(sorted(tags))

    print("end of main")


if __name__ == "__main__":
    main()
