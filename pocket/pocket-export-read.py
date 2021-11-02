#
# read pocket export html file
#

# import the HTMLParser module
from html.parser import HTMLParser

# globals TODO: do i need these?
tags = set()  # set of tags
links = {}  # dict of links & tags
# class PocketEntry():
#     __link
#     __tags

#
# pocket bookmark entry
#


class PocketEntry():
    link = ""
    tags = []

    # def __init__(self):
    #     # null
    #     link = ""
    #     tags = []

    def __init__(self, link, tags):
        self.link = link

# subclass of HTMLParser and override the handler methods


class PocketExportParser(HTMLParser):

    name = "PocketExportParser"

    # all unique tags
    tags = set()

    # pocket bookmarks TODO: make a static variable?
    entries = []

    @staticmethod
    def getentries():
        return PocketExportParser.entries

    @staticmethod
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
                    # self.entries.append(entry)

                # print(entry)

                # find tags
                if (a[0] == "tags"):
                    ts = a[1]

                    # add to entry
                    entry.tags = ts

                    # TODO: is this needed?
                    self.entries.append(entry)

                    # add separate tag to class set
                    if ts:
                        for t in ts.split(","):
                            self.tags.add(t)

                if entry.link is not None:
                    self.entries.append(entry)


def main():
    # global tags

    # instantiate the parser and feed it some HTML
    parser = PocketExportParser()
    print(parser.name)

    # open the pocket export HTML file and read it
    f = open("data/pocket-export.html")
    if f.mode == "r":
        contents = f.read()  # read the entire file
        parser.feed(contents)
    f.close()

    # # TODO: fix class visibility of entries
    # for e in parser.entries:
    #     print(e.link)

    # write links to file
    lf = open("data/pocket-links.txt", "w")
    entries = PocketExportParser.getentries()
    for e in entries:
        lf.write(e.link + "\n")
    lf.close()

    # print(parser.entries)

    # print(links)

    # write tags to file
    # TODO: use method, don't just get class data
    tf = open("data/pocket-tags.txt", "w")
    for t in sorted(PocketExportParser.tags):
        tf.write(t + "\n")
    # print(sorted(tags))
    tf.close()

    print("end of main")


if __name__ == "__main__":
    main()
