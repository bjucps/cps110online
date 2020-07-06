import sys
import os
import os.path

def findFile(file2find: str, startingDir: str):
    print(startingDir + "...")
    try:
        files = os.listdir(startingDir)

        for file in files:
            #print(file)
            fileFullPath = os.path.join(startingDir, file)
            if os.path.isdir(fileFullPath):
                # search directory
                findFile(file2find, fileFullPath)
            elif file.lower() == file2find.lower():
                print(" *** FOUND: " + startingDir + " " + file)            
    except:
        pass


if len(sys.argv) != 3:
    sys.stderr.write("Usage: python findfile.py <file2find> <startingDir>")
    exit(1)

file2find = sys.argv[1] 
startingDir = sys.argv[2] 

print('Searching for ', file2find, ' in ', startingDir)

findFile(file2find, startingDir)