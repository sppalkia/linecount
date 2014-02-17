This is a command line utilty to perform a line count over a directory.

To use, just cd to the directory you want to perform the line count on, and run:

./wordcount.py

There are a number of options available (which you can read about with ./wordcount.py --help):

--verbose prints the absolute paths of the files that are read
--all will count the lines of all files instead of the default filetype set
--filetypes will let you specify the file extensions to count. For example, if you wanted to count *.c and *.h files,
you could do something like:

./wordcount.lpy --filetypes=h,c
