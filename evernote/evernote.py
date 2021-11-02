# read evernote mhtml file w/o regExp
######################################

nbs = []                       # my evernote notebooks
linenum = 0
substr = "NOTEBOOK_TITLE"         # Substring to search for.
with open('data/evernote-notebooks.mhtml', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.find(substr) != -1:    # if match,
            nbs.append("Line " + str(linenum) + ": " + line.rstrip('\n'))
for err in nbs:
    print(err)
