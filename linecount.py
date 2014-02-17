#!/usr/bin/python

import os
import os.path
import sys

from optparse import OptionParser

# There are the files whose line count is taken into account
default_filetypes = [ "m", "h", "hh", "c", "mm", "cpp", "java", "py", "scala"]

def linecount(top_directory = '.', filetypes = None, verbose = False):
    """
    Count the number of lines in a directory. By default, 
    prints the following filetypes:
    .m, .h, .hh, .c, .mm, .cpp, .java, .py, .scala

    If filetypes is not None, only files with the given extensions
    will be counted.
    """

    if not os.path.exists(top_directory):
        sys.exit("{0}: not a valid directory".format(top_directory))

    if verbose is None:
        verbose = False

    variables = {'filetypes' : filetypes}
    def should_skip(filename):
        if variables['filetypes'] is None:
            return False

        for filetype in variables['filetypes']:
            if filename.endswith(filetype):
                return False

        return True


    top_directory = os.path.abspath(top_directory)
    count = 0

    for dirpath, dirnames, filenames in os.walk(top_directory):
        for filename in filenames:

            if should_skip(filename):
                continue

            fullpath = dirpath + '/' + filename
            if verbose:
                print fullpath
            lines = 0
            try:
                with open(fullpath) as f:
                    lines = 0
                    for  line in enumerate(f):
                        lines += 1
                lines += 1
            except IOError as e:
                sys.exit("Encountered an Error: {0}".format(str(e)))

            count += lines

    return count


if __name__ == "__main__":

    parser = OptionParser(usage = "usage: %prog [-v] [-a] | [-f LIST]")

    parser.add_option("-a", "--all", dest="all_files", action="store_true", \
                              help="Count all files.")

    filetypes_help = "Specify filetypes in a comma-seperated list. \
            Default filetypes are: {0}".format(default_filetypes)
    parser.add_option("-f", "--filetypes", dest="filetypes", type="string", \
                              help=filetypes_help, metavar="LIST")

    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", \
                              help="Make some noise")

    (options, args) = parser.parse_args()

    filetypes = default_filetypes
    if options.filetypes is not None:
        if options.all_files:
            parser.error("cannot specify both --filetypes and --all")
            sys.exit(1)
        else:
            filetypes = options.filetypes.split(',')
    elif options.all_files:
        filetypes = None

    if options.verbose:
        print "Filetypes: {0}".format(filetypes)

    directory = os.getcwd()
    if len(args) > 0:
        directory = args[0]
        
    print linecount(directory, filetypes, options.verbose)
