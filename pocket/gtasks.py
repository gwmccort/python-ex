#
# read pocket export html file
#

import json

def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print("title: " + theJSON["metadata"]["title"])

def main(): 
        
    # open the sample HTML file and read it
    f = open("Google-Tasks.json")
    if f.mode == "r":
        contents = f.read() # read the entire file
        printResults(contents)
    
    f.close()

if __name__ == "__main__":
  main();
