import os
import shutil
import logging
import yaml

logging.basicConfig(
    filename="cleanup.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%b-%d-%y %H:%M:%S"
)

delFileCount = 0
delDirCount = 0
delFiles = []
delDirs = []

def deleteFiles(dir):
    os.chdir(dir)
    fileCount = str(len(os.listdir()))
    confirm = input("Are you sure you want to delete " + fileCount + " files from " + dir + "? Y or N? ")
    if confirm == "Y":    
        global delFileCount
        global delDirCount
        for name in os.listdir():
            logging.info(name)
            if os.path.isdir(name):
                delDirs.append(name)
                shutil.rmtree(name)
                delDirCount += 1
            else:
                delFiles.append(name)
                os.remove(name)
                delFileCount += 1
    else:
        print("File cleanup has been cancelled.")


yaml_file_path = "paths.yml"

with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

paths = data['paths']


for path in paths:
    deleteFiles(path)

print("File cleanup finished. \n Files deleted: " + str(delFileCount) + "\n Directories deleted: " + str(delDirCount))