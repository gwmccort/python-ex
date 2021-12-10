# open two files at a time
# from: https://www.kite.com/python/answers/how-to-open-multiple-files-using-with-in-python
###############################

with open("test.txt") as inF, open("out.txt", "w") as outF:
    l = inF.readline()
    outF.write(l)
    print(l)
