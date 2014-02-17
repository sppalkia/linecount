linecount
---
linecount is a command line utility to count the number of lines in a directory.

To use, just cd to the directory you want to perform the line count on, and run:

    $ ./linecount.py

There are a number of options available (which you can read about with ./wordcount.py --help):

`--verbose` prints the absolute paths of the files that are read.

`--all` will count the lines of all files instead of the default filetype set.

`--filetypes` will let you specify the file extensions to count. For example, if you wanted to count *.c and *.h files,
you could do something like:

    $ ./linecount.py --filetypes=h,c
