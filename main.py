import glob
import pathlib

# check current path for any .cbp files
print(pathlib.Path().absolute())

targets = []
for file in glob.glob("*.cbp"):
    targets.append(file)
    print("Found file: " + file)

# for each .cbp file
for cbp in targets:
    print("yo")

# get current path

# open file with write perms

# iterate through, removing current path wherever found (leaving relative path)
