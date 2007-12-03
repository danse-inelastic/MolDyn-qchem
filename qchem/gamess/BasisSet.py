#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
#                              
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from sample import Units
from os import sep
from pyre.components.Component import Component

class BasisSet(Component):
    '''This class serves as an interface for quantum chemistry engines.'''

    class Inventory(Component.Inventory):
        '''this is the inventory; the defaults are for the GAMESS engine'''
        import pyre.inventory as pinv  
        AM1 = pinv.str('AM1')
        PM3 = pinv.str('PM3')
        STO3G = pinv.str('STO-3G')