# codeblocks-project-generator
Searches current directory for all C/C++ source and header files, and rams them into a new CodeBlocks project

## Usage

Tested using Python 3.8

- Navigate to the root of your project's directory. Your project must have a `src/` folder (can be configured by editing script) with all your required source files contained inside
- Run `python3 main.py` or `python3 ../path/to/main.py` 
- A new CodeBlocks project will be produced in folder `codeblocks/`. Test to ensure everything went smoothly

## Rationale

The CMake CodeBlocks generators (eg. `CodeBlocks - Unix Makefiles`) produce CodeBlocks projects with absolute paths. This makes the outputted projects impossible to share with others, and sometimes its not acceptable to expect others to generate their own CodeBlocks project via CMake.

## Issues

- Non-code files (such as data files) are naively copied into binary dirs to make them accessible to executables. If you wanted to make some files ending in a source code extension (`.c`, `.cpp`, `.h` etc.) then you would have to copy them in manually. If you didn't want these files in your binary dir, you have to delete them manually (if it bothers you, just hedging that you *probably do* want these files available to your binaries)
- Default compiler is GCC, with few build arguments given. No way to generate for other compilers with this script right now
