#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Brandon Keith
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from sample.Sample import Sample
from sample import Units
from gamess.Gamess import Gamess
from os import sep,system,chdir
import unittest 
#import danseGlob
import string

appName = "Gamess"
caseName = "fulltest"

import journal
debug = journal.debug( "%s-%s" % (appName, caseName) )

class GamessEnergy_TestCase(unittest.TestCase):
    '''run test cases on energy calculation capabilities'''
    
    def setUp(self):
        """do methylene"""
        self.sample = Sample()
        atoms=[['C', 0.0, 0.0, 0.0],
        ['Ti', 2.29333,     2.29333,     1.477035],
        ['O',  1.397509435, 1.397509435, 0.0],
        ['O',  3.189150565, 3.189150565, 0.0],
        ['O',  3.690839435, .8958205646, 1.477035000],
        ['O',  .8958205646, 3.690839435, 1.477035000]]
        self.sample.atoms = atoms
        self.sample.initialTemp = 300.0*Units.K
        self.sample.basisSet='/home/brandon/Fdata3t_Os3.6_p4.1_Tis6.3_p6.8_d5.7/'

    def testGamessEnergy(self):
        en = Gamess(self.sample)
        en.i.engineExecutablePath = '/home/brandon/pcgamess/gamess'
        en.i.workingDirectory='/home/brandon/DANSE/qchem/tests/gamess/energy'
        en.i.logFilename='gamess.log'
        en.execute()

if __name__ == "__main__":
    suite1 = unittest.makeSuite(GamessEnergy_TestCase)
    alltests = unittest.TestSuite((suite1))
    unittest.TextTestRunner(verbosity=2).run(alltests)

