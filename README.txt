Purpose: 
This program creates a compiler using the ANTLR toolset. 

Requirements
    In order to run the program you must have Java and Python installed on your machine 

    Must Run this command to re-generate auto-generated antlr files: 
    antlr4 -Dlanguage=Python3 Lang.g4 -visitor -o gen


File contains 4 source code files that are non-antlr generated. 

main.py: 
the main program in the compiler. it is used to initialize all components, generate lexer and parser, create the parse tree, and interpret the code. 

interpreter.py: 
This file defines how each part of the parse tree is interpreted. This is where all interpretation of the source program occurs.

Lang.g4:
this is the antlr file to define the grammar accepted by the compiler. This must coorospond with functionality in interpreter.py.

test.lang
This file contains the source code that the interpreter will run.

gen directory: 
this directory is full of files created by antlr in order for it to correctly process the input code (Lexer, Parser, Visitor)