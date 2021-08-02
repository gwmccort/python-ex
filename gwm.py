#
# read a text file
#

def main():

    print("start of main()")

    # open file
    # f = open("textfile.txt","w+")
    f = open("textfile.txt", "r")

    # # write some lines of data to the file
    # for i in range(10):
    #     f.write("This is line %d\r\n" % (i+1))

    # # Open the file back up and read the contents
    f = open("textfile.txt", "r")
    if f.mode == 'r':  # check to make sure that the file was opened
        # use the read() function to read the entire file
        contents = f.read()
        print(contents)

    #   fl = f.readlines() # readlines reads the individual lines into a list
    # for x in fl:
    #   print (x)

    # close the file when done
    f.close()


if __name__ == "__main__":
    main()
