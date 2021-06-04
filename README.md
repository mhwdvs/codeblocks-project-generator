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

- Non-code files (such as data files) are not added to binary dirs, so data may not be accessible to your builds by default
- Default compiler is GCC, with few build arguments given. No way to generate for other compilers with this script right now
