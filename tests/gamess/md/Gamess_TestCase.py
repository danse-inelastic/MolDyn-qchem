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
from os import sep,system,chdir
import unittest 
import danseGlob
import string

appName = "Fireball"
caseName = "fulltest"

import journal
debug = journal.debug( "%s-%s" % (appName, caseName) )

class FireballMD_TestCase(unittest.TestCase):
    '''run test cases on md capabilities'''
    def setUp(self):
        """do tiO2 unit cell"""
        self.sample = Sample('periodic')
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

    def testFireballNVE(self):
        chdir('nve')
        try:
            md = Fireball(self.sample)
            md.i.engineExecutablePath = '/home/brandon/myFireball-bin/fireball.x'
            md.i.ensemble = 'nve'
            md.i.timestep = 0.5
            md.i.equilibrationTime = 0.0
            md.i.productionTime = 1.0*Units.fs
            md.i.trajectoryFilename='tio2NVE.xyz'
            md.i.logFilename='tio2NVE.log'
            md.integrate()
        finally:
            chdir('..')

    def testFireballNVT(self):
        chdir('nvt')
        try:
            self.sample.temperature=200.0*Units.K
            md = Fireball(self.sample)
            md.i.engineExecutablePath = '/home/brandon/myFireball-bin/fireball.x'
            md.i.ensemble = 'nvt'
            md.i.timestep = 0.5
            md.i.equilibrationTime = 0.0*Units.ps
            md.i.productionTime = 1.0*Units.fs
            md.i.trajectoryFilename='tio2NVT.xyz'
            md.i.logFilename='tio2NVT.log'
            md.integrate()
        finally:
            chdir('..')


if __name__ == "__main__":
    suite1 = unittest.makeSuite(FireballMD_TestCase)
    alltests = unittest.TestSuite((suite1))
    unittest.TextTestRunner(verbosity=2).run(alltests)

