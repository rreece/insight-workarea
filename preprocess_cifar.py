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

import argparse, sys, time
import pickle

import keras


#------------------------------------------------------------------------------
# options
#------------------------------------------------------------------------------
def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles',  default=None, nargs='*',
            help='Input files.')
    parser.add_argument('-v', '--verbose',  default=False,  action='store_true',
            help="Some toggle option.")
#    parser.add_argument('-i', '--input',  default=None,
#            help="Path to directory of datasets")
    parser.add_argument('-t', '--type',  default='cifar10',
            help="Name of output file.")   
    return parser.parse_args()


#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------
def main():
    ops = options()
    _type = ops.type

    if _type == 'cifar10':
        from keras.datasets import cifar10
        (x_train, y_train), (x_test, y_test) = cifar10.load_data()
        print(x_train.shape) # (50000, 32, 32, 3)
        print(x_test.shape)  # (10000, 32, 32, 3)
        print(y_train) 
        stuff = dict()
        stuff['data'] = x_train
        stuff['labels'] = y_train
        pickle.dump(stuff, open("cifar-10-train.p", "wb"))
        del stuff
        stuff = dict()
        stuff['data'] = x_test
        stuff['labels'] = y_test
        pickle.dump(stuff, open("cifar-10-test.p", "wb"))

    elif _type == 'cifar100':
        from keras.datasets import cifar100
        (x_train, y_train), (x_test, y_test) = cifar100.load_data(label_mode='fine')
        print(x_train.shape) # (50000, 32, 32, 3)
        print(x_test.shape)  # (10000, 32, 32, 3)
        print(y_train) 
        stuff = dict()
        stuff['data'] = x_train
        stuff['labels'] = y_train
        pickle.dump(stuff, open("cifar-100-train.p", "wb"))
        del stuff
        stuff = dict()
        stuff['data'] = x_test
        stuff['labels'] = y_test
        pickle.dump(stuff, open("cifar-100-test.p", "wb"))

    elif _type == 'cifar10_local':
        ## official cifar-10
        assert len(ops.infiles) == 1
        infile = ops.infiles[0]
        f = open(infile, 'rb')
        d = pickle.load(f, encoding='bytes')
        print(d.keys())
        x = d[b'data']
        print(x.shape) # (10000, 3072)

    elif _type == 'jimmy':
        ## Jimmy's files
        assert len(ops.infiles) == 1
        infile = ops.infiles[0]
        f = open(infile, 'rb')
        d = pickle.load(f, encoding='bytes')
        x = d['data']
        print(x.shape) # (50000, 3, 32, 32)
        y = d['labels']
        print(y.shape) # (50000, 1)
        print(y)

    elif _type == 'my':
        ## my processed files
        assert len(ops.infiles) == 1
        infile = ops.infiles[0]
        f = open(infile, 'rb')
        d = pickle.load(f, encoding='bytes')
        x = d['data']
        print(x.shape)
        y = d['labels']
        print(y.shape)
        print(y)



#------------------------------------------------------------------------------
# free functions
#------------------------------------------------------------------------------


#______________________________________________________________________________
def fatal(message=''):
    sys.exit("Fatal error in %s: %s" % (__file__, message))


#______________________________________________________________________________
def tprint(s, log=None):
    line = '[%s] %s' % (time.strftime('%Y-%m-%d:%H:%M:%S'), s)
    print(line)
    if log:
        log.write(line + '\n')
        log.flush()


#------------------------------------------------------------------------------
if __name__ == '__main__': main()

