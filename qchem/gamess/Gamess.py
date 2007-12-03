#!/usr/bin/env python
# =================================================================
#
# {LicenseText}
#
# =================================================================
#
from qchem.QChem import QChem
from os import system, chdir
from gamess.GamessInputFile import GamessInputFile

class Gamess(QChem):
    '''implements the QChem interface using the Gamess engine'''
    
    class Inventory(QChem.Inventory):
        import pyre.inventory as inv  
        basisSet = inv.str('Basis Set', default=gbasisChoices[0])
        basisSet.meta['tip'] = """type of basis set used in the calculation"""
        basisSet.validator = inv.choice(gbasisChoices)
    
    
    def __init__(self, sample):
        QChem.__init__(self)
        g=GamessInputFile()
        
    def setInputParameters(self):
        '''translates values of inventory to appropriate input data file statements'''
        self.i.
        self.i.
        
    def execute(self):
        '''calculate the energy'''
        chdir(self.i.workingDirectory)

        g.write()
        system(self.i.engineExecutablePath)
        
        
    