#!/usr/bin/env python
"""
NAME
    preprocess_cifar.py - short description

SYNOPSIS
    preprocess_cifar.py [-h] [-o OUTPUT] infiles [infiles ...]

DESCRIPTION
    Write a longer description.

OPTIONS
    -h, --help
        Prints this manual and exits.
        
    -o OUTFILE
        Specifies the output filename (out.bib by default).

AUTHOR
    Ryan Reece  <ryan.reece@cern.ch>

2018-01-17
"""

#------------------------------------------------------------------------------
# imports
#------------------------------------------------------------------------------

## std
import argparse, sys, time

## local modules


#------------------------------------------------------------------------------
# options
#------------------------------------------------------------------------------
def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles',  default=None, nargs='+',
            help='Input text files of APA references.')
    parser.add_argument('-v', '--verbose',  default=False,  action='store_true',
            help="Some toggle option.")
#    parser.add_argument('-i', '--input',  default=None,
#            help="Path to directory of datasets")
    parser.add_argument('-o', '--output',  default='out.bib',
            help="Name of output file.")   
    return parser.parse_args()


#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------
def main():
    ops = options()

    print ops


#------------------------------------------------------------------------------
# free functions
#------------------------------------------------------------------------------


#______________________________________________________________________________
def fatal(message=''):
    sys.exit("Fatal error in %s: %s" % (__file__, message))


#______________________________________________________________________________
def tprint(s, log=None):
    line = '[%s] %s' % (time.strftime('%Y-%m-%d:%H:%M:%S'), s)
    print line
    if log:
        log.write(line + '\n')
        log.flush()


#------------------------------------------------------------------------------
if __name__ == '__main__': main()

