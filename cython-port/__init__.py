#!/usr/bin/env python3
'''
CLI Front End
'''
import os, sys, logging, pickle
from pics2word import *
from .LogGen import set_up_logging
from .help import help

logger = logging.getLogger(__name__)

def remDictKey(d, key):
    '''Returns a new dictionary with a key-value pair removed'''
    logger.debug("removing %s from arg list dictionary" % key)
    new_d = d.copy()
    new_d.pop(key)
    return new_d

# Method to parse command line arguements into command-value pairs
def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            logging.debug("Adding %s as a value to %s command." % (argv[1], argv[0]))
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def LoadSave(IniArgs):
    if '-m' in IniArgs: 
        mod = IniArgs['-m']
        try:
            # Try to look for the file in the directory
            logger.info("Found module %s. Loading arg list." % mod)
            return pickle.load(open(mod+".p", "rb"))
        except:
            # If theres an error loading the file we assume the file does not exist so sets one up
            logger.info("Module %s not found. creating module called %s" % (mod,mod))
            myargs = remDictKey(IniArgs, '-m') # dont resave save function
            pickle.dump(myargs, open(mod+".p", "wb"))
            return myargs
    else:
        return IniArgs

def main():
    #Arglist passed as immutable for key to dict 
    set_up_logging(tuple(sys.argv))
    # Parse the arguments the either Load or save an arg template
    myargs = LoadSave(getopts(sys.argv))

    Doc = pics2word()  
    if '-h' in myargs:
        help(myargs['-h'])
    if '-P' in myargs:
        # Override the default path
        Doc.SetPath(myargs['-P'])
    if '-f' in myargs:
        # Set as table or default
        Doc.SetFormat(format=myargs['-f'])
    if '-T' in myargs:
        # Set a title to override the default
        Doc.SetTitle(title=myargs['-T'],date=myargs['-Td'])
    if '-pw' in myargs:
        # Override the default picture width
        Doc.SetPicWidth(float(myargs['-pw']))
    if '-ph' in myargs:
        # Override the default picture height
        Doc.SetPicHeight(float(myargs['-ph'])) 
    if '-tw' in myargs:
        if Doc.format[0] != 't' :
            raise ValueError("Must enable table format to format table width!")
        else:
            Doc.SetTableWidth(int(myargs['-tw']))
    
    # after all optional parameters have been changed and not asked for help, then write document.
    if '-h' not in myargs:
        Doc.WriteDoc()

if __name__ == '__main__':
    main()
