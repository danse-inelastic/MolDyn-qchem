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
from danseGlob.SimCommon import SimCommon
import string

appName = "Fireball"
caseName = "fulltest"

import journal
debug = journal.debug( "%s-%s" % (appName, caseName) )


class FireballRestart_TestCase(unittest.TestCase):
    
    def setUp(self):
        """do argon"""
        argonConfiguration = file('argon.conf')
        lx, ly, lz = map(string.atof, string.split(argonConfiguration.readline()))
        self.sample = Sample('periodic')
        self.sample.unitCell = [[lx, 0.0, 0.0], [0.0, ly, 0.0], [0.0, 0.0, lz]]
        atoms = []
        while 1:
            line = argonConfiguration.readline()
            if not line: break
            x, y, z = map(string.atof, string.split(line))
            atoms.append(['Ar', x, y, z])
        self.sample.atoms = atoms
        self.sample.initialTemp = 300.0*Units.K
        twoAtom=TwoAtomPotential('Ar','Ar')
        twoAtom.assignInteraction('lennardJonesMmtk')
        #self.sample.forcefieldParameters = twoAtom.getPotential('lennardJonesMmtk')
        self.sample.forcefields=[]
        self.sample.forcefields.append(twoAtom)
        
    def testRestart(self):
        # first do a short md run
        md = Gulp(self.sample)
        md.i.ensemble = 'nve'
        md.i.timestep = 0.5*Units.fs
        md.i.equilibrationTime = 0.005*Units.ps
        md.i.productionTime = 0.01*Units.ps
        md.i.inputDeck='shortArgonNVE.gin'
        md.i.trajectoryFilename='shortArgonNVE.xyz'
        md.i.logFilename='shortArgonNVE.log'
        md.i.restartFilename='shortArgonNVE.res'
        md.integrate()
        # restart from it
        restartMd = Gulp(self.sample)
        restartMd.i.inputDeck='shortArgonNVE.res'
        restartMd.i.logFilename='shortArgonNVE.log'
        restartMd.restartIntegrate()


if __name__ == "__main__":
    suite3 = unittest.makeSuite(FireballRestart_TestCase)
    alltests = unittest.TestSuite((suite3))
    unittest.TextTestRunner(verbosity=2).run(alltests)

