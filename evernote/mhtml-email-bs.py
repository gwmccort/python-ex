# extract mime encoded multi-part mhtml
# from: https://tewarid.github.io/2019/06/04/extract-all-tabular-data-from-multipart-mime-documents.html
#
# TODO: only gets plain notebooks, non in a stack
#################################################

import email
from bs4 import BeautifulSoup

inFile = "data/Notebooks-Evernote.mhtml"

with open(inFile) as inF, open("out.txt", "w") as outF:

    # use email to get each part of multi-part file
    message = email.message_from_file(inF)
    for part in message.walk():
        # html part
        if (part.get_content_type() == "text/html"):
            soup = BeautifulSoup(part.get_payload(
                decode=True), features="lxml")

            # each evernote notebook
            for nb in soup.findAll('span', attrs={'id': 'qa-NOTEBOOK_TITLE'}):
                print(nb.text)
                outF.write(mb.text)

            # # print(soup.prettify())
            # outF.write(soup.prettify())
