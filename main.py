import glob
import pathlib
import shutil
import os
import ntpath


def relative_path(absolute_path, absolute_file_path):
    return os.path.relpath(absolute_file_path, absolute_path)


def search_file_recursive(search_term):
    print("Searching for: " + search_term)
    res = []
    for file in glob.glob(search_term, recursive=True):
        res.append(file)
        print("Found file: " + file)
    return res


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def main():
    # check current path for any .cbp files
    path = pathlib.Path().absolute().__str__() + "/"
    dest_folder = "codeblocks/"
    src_folder = "src/"
    src_file_extensions = ["c", "cpp", "h", "cc", "hpp", "hh"]
    print("Current working dir: " + path)
    print("Source dir: " + src_folder)
    print("Dest dir: " + dest_folder + "\n")

    # remove old project if it exists
    dirpath = pathlib.Path(dest_folder)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    # codeblocks project file
    cbp_begin = """\
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<CodeBlocks_project_file>
    <FileVersion major="1" minor="6" />
    <Project>
        <Option title="test-project" />
        <Option pch_mode="2" />
        <Option compiler="gcc" />
        <Build>
            <Target title="Debug">
                <Option output="bin/Debug/test-project" prefix_auto="1" extension_auto="1" />
                <Option object_output="obj/Debug/" />
                <Option type="1" />
                <Option compiler="gcc" />
                <Compiler>
                    <Add option="-g" />
                    <Add directory="include" />
                </Compiler>
            </Target>
            <Target title="Release">
                <Option output="bin/Release/test-project" prefix_auto="1" extension_auto="1" />
                <Option object_output="obj/Release/" />
                <Option type="1" />
                <Option compiler="gcc" />
                <Compiler>
                    <Add option="-O2" />
                    <Add directory="include" />
                </Compiler>
                <Linker>
                    <Add option="-s" />
                </Linker>
            </Target>
        </Build>
        <Compiler>
            <Add option="-Wall" />
            <Add option="-fexceptions" />
        </Compiler>
    """
    cbp_end = """\
        <Extensions />
    </Project>
</CodeBlocks_project_file>
    """

    # copy all files in source dir to codeblocks dir
    source_files = search_file_recursive(path + "**/" + src_folder + "*")

    # copy all file paths into codeblocks project file
    print("")
    os.makedirs(os.path.dirname(dest_folder), exist_ok=True)
    cbp_units = []
    for file in source_files:
        rel_path = relative_path(path, file)
        print("Copying file \n" + file + " to \n" + dest_folder + rel_path + "\n")
        os.makedirs(os.path.dirname(dest_folder + rel_path), exist_ok=True)
        shutil.copy(file, dest_folder + rel_path)
        cbp_units.append("<Unit filename=\"" + rel_path + "\"/>\n")

    # copy non-code files into binary dirs (to make data files available to binaries)
    print("Copying non-code files to binary dirs!\n")
    for file in source_files:
        if not file.split(".")[1] in src_file_extensions:
            rel_path = relative_path(path, file)
            print("Copying file \n" + file + " to \n" + dest_folder + "bin/Debug/" + rel_path + "\n")
            print("Copying file \n" + file + " to \n" + dest_folder + "bin/Release/" + rel_path + "\n")
            os.makedirs(os.path.dirname(dest_folder + "bin/Debug/" + rel_path), exist_ok=True)
            os.makedirs(os.path.dirname(dest_folder + "bin/Release/" + rel_path), exist_ok=True)
            shutil.copy(file, dest_folder + "bin/Debug/" + rel_path)
            shutil.copy(file, dest_folder + "bin/Release/" + rel_path)

    # write cbp file
    with open(dest_folder + "main.cbp", 'w') as file:
        file.write(cbp_begin)
        for line in cbp_units:
            file.write(line)
        file.write(cbp_end)


main()
