# codeblocks-project-generator
Searches current directory for all C/C++ source and header files, and rams them into a new CodeBlocks project

## Usage

Tested using Python 3.8

- Navigate to the root of your project's directory
- Run `python3 main.py` or `python3 ../path/to/main.py` 
- A new CodeBlocks project will be produced in folder `codeblocks/`. Test to ensure everything went smoothly

## Rationale

The CMake CodeBlocks generators (eg. `CodeBlocks - Unix Makefiles`) produce CodeBlocks projects with absolute paths. This makes the outputted projects impossible to share with others, and sometimes its not acceptable to expect others to generate their own CodeBlocks project via CMake.

## Issues

- Currently doesn't add any non-code files into the CodeBlocks project, so data files, config files etc. May need to copied in manually
- Default compiler is GCC, with few build arguments given. No way to generate for other compilers with this script right now
