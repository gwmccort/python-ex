#!/usr/bin/python3
########################################################
# Extract data from multipart mime documents
#   (trying evernote)
# source: https://tewarid.github.io/2019/06/04/extract-all-tabular-data-from-multipart-mime-documents.html
#########################################################

import email
from bs4 import BeautifulSoup
# from html_table_extractor.extractor import Extractor

file = "../evernote/data/Notebooks - Evernote (1).mhtml"

print("START:")

with open(file) as fp:

    # get parts of mhtml
    message = email.message_from_file(fp)

    for part in message.walk():
        # print('walking')
        # print(part.get_content_type())

        # get html types
        if (part.get_content_type() == "text/html"):
            # print('found text/html..................')
            # print(part.get_payload(decode=False))

            # parse html with bs
            soup = BeautifulSoup(part.get_payload(decode=False), 'lxml')
            # print(soup.prettify())
            # TODO: doesn't seem to be right content

            for nb in soup.findAll('span', attrs={'id': '3D"qa-NOTEBOOK_TITLE"'}):
                print(nb.text)

                # THIS DOESN"T WORK
                # extractor = Extractor(table)
                # extractor.parse()
                # print(extractor.return_list())


print("END:")
