#
# read google bookmarks export html file
#

# import the HTMLParser module
# from html import parser
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


# class PocketEntry():
#     link = ""
#     tags = []

#     # def __init__(self):
#     #     # null
#     #     link = ""
#     #     tags = []

#     def __init__(self, link, tags):
#         self.link = link

# create a subclass of HTMLParser and override the handler methods


class BookmarksExportParser(HTMLParser):
    # unique bookmark links
    myLinks = set()

    # all unique tags
    tags = set()
    # tags2 = set()

    # bookmarks links TODO: make a static variable?
    # bookmarks = []
    # bookmarks = set()

    # @staticmethod
    # def getBookmarks():
    #     return tags2

    @staticmethod
    def gettags(self):
        return tags

    # overide start tag handler
    def handle_starttag(self, tag: str, attrs):

        # process 'a' link tags
        if tag == "a":

            # TODO: do i need this?
            # entry = PocketEntry(None, None)

            # loop thru attrs to find links & tags
            for a in attrs:

                # find links (ie href's)
                if (a[0] == "href"):
                    print("link:" + a[1])
                    BookmarksExportParser.myLinks.add(a[1])
                    # bookmarks.append(a[11])
                    # lnk = a[1]
                    # links[lnk] = {}
                    # entry.link = a[1]
                    # self.entries.append(entry)

                # print(entry)

                # # find tags
                # if (a[0] == "tags"):
                #     ts = a[1]

                #     # add to entry
                #     entry.tags = ts

                #     # TODO: is this needed?
                #     self.entries.append(entry)

                #     # add separate tag to class set
                #     if ts:
                #         for t in ts.split(","):
                #             self.tags.add(t)

                # if entry.link is not None:
                #     self.entries.append(entry)


def main():
    # whay do i need this???
    global tags

    # instantiate the parser and feed it some HTML
    parser = BookmarksExportParser()

    # open HTML file and read it
    f = open("data/GoogleBookmarks.html")
    if f.mode == "r":
        contents = f.read()  # read the entire file
        parser.feed(contents)

    f.close()

    # access class var
    print(parser.myLinks)

# # TODO: fix class visibility of entries
# for e in parser.entries:
#     print(e.link)

# entries = BookmarksExportParser.getentries()
# for e in entries:
#     print(e.link)

# print(parser.entries)

# # exit()

# # print(links)

# # TODO: use method, don't just get class data
# for t in PocketExportParser.tags:
#     print(t)
# # print(sorted(tags))


if __name__ == "__main__":
    main()
