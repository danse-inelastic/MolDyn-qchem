#!/usr/bin/env python
# =================================================================
#
# {LicenseText}
#
# =================================================================
#
from os import sep

class Group:
    '''takes care of writing a group to an input file and eventually saving input
and serializing it.'''
    
    def __init__(self, name, parms):
        self.name = name
        self.parameters = parms.keys()
        self.parameters.sort() # Sort parms.
        
        # WARNING: Bugs will be caused if any of ctlRec's own methods or 
        # instance variables had the same name as any of the parameter ('k') values.

        for k in self.parameters:
            self.__dict__[k] = parms[k]

    def write(self, f):
        '''Write group to input file'''
        f.write(" $"  + self.name + ' ')
        col = len(self.name) + 3
        for k in self.parameters:
            if not self.__dict__[k]: continue # Do not print null parms.
            phrase = k + '=' + str(self.__dict__[k])
            col += 1 + len(phrase)
            if col > 70: 
                col = len(phrase)
                f.write(sep)
            f.write(phrase + ' ')
        f.write('$END'+sep)
        
    pass # end of class 