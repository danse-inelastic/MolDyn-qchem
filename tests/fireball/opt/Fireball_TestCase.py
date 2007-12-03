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
from fireball.Fireball import Fireball
from os import sep,system
import unittest 
import danseGlob
import string

appName = "Fireball"
caseName = "fulltest"

import journal
debug = journal.debug( "%s-%s" % (appName, caseName) )

class FireballOpt_TestCase(unittest.TestCase):
    
    def setUp(self):
        """do tiO2 unit cell"""
        self.sample = Sample()
        self.sample.unitCell = [[4.58666, 0.0, 0.0], 
                                [0.0, 4.58666, 0.0], 
                                [0.0, 0.0, 2.95407]]
        atoms=[['Ti', 0.0, 0.0, 0.0],
        ['Ti', 2.29333,     2.29333,     1.477035],
        ['O',  1.397509435, 1.397509435, 0.0],
        ['O',  3.189150565, 3.189150565, 0.0],
        ['O',  3.690839435, .8958205646, 1.477035000],
        ['O',  .8958205646, 3.690839435, 1.477035000]]
        self.sample.atoms = atoms
        self.sample.initialTemp = 300.0*Units.K
        self.sample.basisSet='/home/brandon/Fdata3t_Os3.6_p4.1_Tis6.3_p6.8_d5.7/'
        
    def testFastQuench(self):
        opt = Fireball()
        opt.i.sample = self.sample
        opt.i.scftype = 'self-consistentHarris'
        opt.i.exchangeCorrelationTheory = 'mcweda'
        opt.i.engineExecutablePath = '/home/brandon/myFireball-bin/fireball.x'
        opt.i.trajectoryFilename = 'tio2Opt.xyz'
        opt.i.logFilename = 'tio2Opt.log'
        opt.optimize()

if __name__ == "__main__":
    suite2 = unittest.makeSuite(FireballOpt_TestCase)
    alltests = unittest.TestSuite((suite2))
    unittest.TextTestRunner(verbosity=2).run(alltests)

