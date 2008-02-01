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

class FireballEnergy_TestCase(unittest.TestCase):
    '''test its energy capabilities'''
    def setUp(self):
        """do 10-base pair DNA"""
        self.sample = Sample()
        self.sample.unitCell = [[100.0, 0.0, 0.0], 
                                [0.0, 100.0, 0.0], 
                                [0.0, 0.0, 100.0]]
        # get atoms from file
        atoms=[]
        f=file('gcb.0072.xyz','r')
        numAtoms=int(f.readline().strip())
        f.readline()
        for i in range(numAtoms):
            sym,x,y,z=f.readline().split()
            atoms.append([sym,x,y,z])
        self.sample.atoms = atoms
        self.sample.initialTemp = 0.0*Units.K
        self.sample.basisSet='/home/brandon/fireballWork/'+\
        'Fdata9_Hs4.2_9DMOL_Cs4.4_p4.8_Ns4.0_p4.5_Os3.6_p4.1_Ps4.9_p5.4'

    def testEnergy(self):
        en = Fireball()
        en.i.sample=self.sample
        en.i.engineExecutablePath = '/home/brandon/myFireball-bin/fireball.x'
        en.i.trajectoryFilename='tio2Opt.xyz'
        en.i.logFilename='tio2Opt.log'
        en.energy()



if __name__ == "__main__":
    suite1 = unittest.makeSuite(FireballEnergy_TestCase)
    alltests = unittest.TestSuite((suite1))
    unittest.TextTestRunner(verbosity=2).run(alltests)

