#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Brandon Keith
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from qchem.fireball.Fireball import Fireball
#from gamess.Gamess import Gamess #wait until Gamess is fully functional
from os import sep
from pyre.applications.Script import Script
from molDynamics.GeneralSettings import GeneralSettings

class QChemApp(Script):
    '''Driver for the quantum chemistry engines'''
    class Inventory(Script.Inventory):
        import pyre.inventory as pinv 
<<<<<<< .mine
        quantumEngine = pinv.facility('quantumEngine', default=Fireball())
=======
        quantumEngine = pinv.facility('quantumEngine', default=Fireball())
#        quantumEngine = pinv.facility('quantumEngine', default='fireball')
>>>>>>> .r21
        quantumEngine.meta['tip'] = 'which quantum engine to use'
<<<<<<< .mine
#        quantumEngine.meta['known_plugins'] = ['fireball','gamess']
=======
#        quantumEngine.meta['known_plugins'] = ['fireball','gamess']
        generalSettings = pinv.facility('General Settings', default = GeneralSettings())
        generalSettings.meta['tip'] = 'working directory, engine executable path, etc.'
>>>>>>> .r21

    def __init__(self,name='QChemApp'):
        Script.__init__(self, name)
        self.i=self.inventory
        
    def main(self, *args, **kwds):
        self.i.quantumEngine.execute()

# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Tue Jun  5 15:04:48 2007

# End of file 
