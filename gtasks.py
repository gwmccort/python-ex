#
# read google tasks jason export via take-out
#

import json

def printResults(data):
    theJSON = json.loads(data)

    # print("kind: " + theJSON["kind"])

    # print(theJSON["items"])
    for tl in theJSON["items"]:
        if tl:
            print("\ntask list title: " + tl["title"])
            # print(tl)

            # get task list task names/titles
            if "items" in tl:
                # print(tl["items"])
                for i in tl["items"]:
                    if (i["status"] != "completed"):
                        print("\ttitle: " + i["title"] + " status: " + i["status"])

def main(): 
        
    # open the sample HTML file and read it
    f = open("Google-Tasks.json")
    if f.mode == "r":
        contents = f.read() # read the entire file
        printResults(contents)
    
    f.close()

if __name__ == "__main__":
  main();
