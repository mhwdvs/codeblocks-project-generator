# codeblocks-relative-paths
Processes a CodeBlocks project file, converting any absolute paths to relative paths.

The CMake CodeBlocks generators (eg. `CodeBlocks - Unix Makefiles`) produce CodeBlocks projects with absolute paths. This makes the outputted projects impossible to share with others, and some people (rightfully) refuse to generate their own CodeBlocks project via CMake when requesting a CodeBlocks project for submission.

This project aims to use python to convert all of these absolute paths to relative paths, which should make the CodeBlocks project portable again!
