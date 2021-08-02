#
# read evernote mtl export html file
#

# import the HTMLParser module
from html.parser import HTMLParser

# globals
tags = set()  # set of tags
links = {}  # dict of links & tags

# create a subclass of HTMLParser and override the handler methods


class MyHTMLParser(HTMLParser):
    # def handle_comment(self, data: str) -> None:
    #     print("got comment")
    #     pos = self.getpos()
    #     print("\tAt line:", pos[0])

    # overide start tag handler
    def handle_starttag(self, tag: str, attrs):

        # process 'a' tags
        if tag == "a":

            # loop thru attrs to find links & tags
            for a in attrs:

                # find links (ie href's)
                if (a[0] == "href"):
                    lnk = a[1]
                    links[lnk] = {}

                # find tags
                if (a[0] == "tags"):
                    ts = a[1]
                    if ts:
                        for t in ts.split(","):
                            tags.add(t)
                            links[lnk] = a[1]


def main():
    global tags

    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()

    # open the sample HTML file and read it
    f = open("evernote-inbox.mht")
    if f.mode == "r":
        contents = f.read()  # read the entire file
        parser.feed(contents)

    f.close()

    # print(links)

    # print(sorted(tags))

    print("end of main")


if __name__ == "__main__":
    main()
