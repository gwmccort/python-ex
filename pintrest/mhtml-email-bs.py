# extract mime encoded multi-part mhtml
# from: https://tewarid.github.io/2019/06/04/extract-all-tabular-data-from-multipart-mime-documents.html
##############

import email
from bs4 import BeautifulSoup


# <span bovo9yxgu57pb="" class='3D"QCVqN3c=' huwodg8e8kheogqvocpc="" id='3D"qa-NOTEBOOK_TITLE"'>
#  IFTTT
# </span>


# with open("pinterest.mhtml") as fp:
with open("Notebooks-Evernote.mhtml") as fp:
    with open("out.txt", "w") as of:
        message = email.message_from_file(fp)
        for part in message.walk():
            # print(part.get_content_type())
            if (part.get_content_type() == "text/html"):
                soup = BeautifulSoup(part.get_payload(decode=False))
                # print(soup.prettify())
                of.write(soup.prettify())
                # TODO get title of pintrest post
                of.write("--------------------gwm---------------")
