#!/usr/bin/python3
###############################################################
# extract mime encoded multi-part mhtml
# from: https://tewarid.github.io/2019/06/04/extract-all-tabular-data-from-multipart-mime-documents.html
#
# TODO's:
# 1) only gets plain notebooks, non in a stack
# 2) get note count
#
# Notes:
# * need to expand stacks for enclosed notebooks to be visable
##############################################################

import email
from bs4 import BeautifulSoup

# inFile = "data/Notebooks-Evernote.mhtml"
inFile = "data/nen.mhtml"

with open(inFile) as inF, open("out.txt", "w") as outF:

    # use email to get each part of multi-part file
    message = email.message_from_file(inF)
    for part in message.walk():
        # html part
        if (part.get_content_type() == "text/html"):
            soup = BeautifulSoup(part.get_payload(
                decode=True), features="lxml")

            # db: out
            outF.write(soup.prettify())

            # each evernote notebook
            print("Notebooks:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            for nb in soup.findAll('span', attrs={'id': 'qa-NOTEBOOK_TITLE'}):
                print(nb.text)
                outF.write(nb.text)

                # get count TODO not working get's same count
                # print("count: {}".format(
                #     soup.findNext('span', attrs={'id': 'qa-NOTEBOOK_NOTE_COUNT'}).text))

            # # print(soup.prettify())
            # outF.write(soup.prettify())

            # stacks
            print("Stacks:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            for nb in soup.findAll('span', attrs={'id': 'qa-NOTEBOOK_STACK_TITLE'}):
                print(nb.text)
                outF.write(nb.text)
