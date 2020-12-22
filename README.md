# brainpy

Brainpy is my implementation of the esoteric programming language created in 1993 by Urban Müller, BrainF\*\*ck.

It is written purley in python as a interpreter, and is my first step towards understanding how programming languages, compilers and interpreters work.

This program is probably more complex than it needs to be. The purpose of this project was to teach myself about compilers so the full package is included, rather than a single file program. 

When giving input, only one character or sequence of numbers are allowed just like the original BrainF\*\*k program, this means that some programs won't work. When outputting, no new line is printed, if you want to print a new line then you will have to output the ascii value for \\n.

I plan to make a compiler version some time in the future.

# How to use
As long as you are in the same path as brain.py or you added brainpy to your global path, you can simply type (as an example, in windows) in a terminal
```
  C:\Users\user\desktop>brain.py <brainf**k file path>
```
and then the python brainpy interpreter will start up and print any output to the terminal.
