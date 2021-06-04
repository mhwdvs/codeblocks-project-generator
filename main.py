import glob
import pathlib
import fileinput

# get current path
path = pathlib.Path().absolute().__str__() + "/"
print("Current path: " + path)

# check current path for any .cbp files
targets = []
for file in glob.glob("*.cbp"):
    targets.append(file)
    print("Found file: " + file)

if len(targets) == 0:
    print("No codeblocks projects found :|")
    exit(1)

# for each .cbp file
for cbp in targets:
    print("Making file :" + cbp + " relative")

    # open file with write perms
    with fileinput.FileInput(cbp, inplace=True, backup='.bak') as file:
        # iterate through, removing current path wherever found (leaving relative path)
        for line in file:
            print(line.replace(path, ""), end='')

    print("Finished with file: " + cbp)


print("All done!")
