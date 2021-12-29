# file all mp3 files in a path
##############################

import os

path = "/mnt/chromeos/MyFiles/Music/"

for currentpath, folders, files in os.walk(path):
    for file in files:
        if (file.endswith("txt") or file.endswith("mp3")):
            print(os.path.join(currentpath, file))
