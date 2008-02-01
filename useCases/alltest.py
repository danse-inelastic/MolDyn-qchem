#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  
# 
#  <LicenseText>
# 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
from fireball.md.Fireball_TestCase import FireballMd_TestCase
from fireball.opt.Fireball_TestCase import FireballOpt_TestCase
from fireball.restart.Fireball_TestCase import FireballRestart_TestCase
from gamess.energy.Gamess_TestCase import GamessEnergy_TestCase
from gamess.md.Gamess_TestCase import GamessMd_TestCase
from gamess.opt.Gamess_TestCase import GamessOpt_TestCase

import unittest

if __name__ == "__main__":
    suite1 = unittest.makeSuite(FireballMd_TestCase)
    suite2 = unittest.makeSuite(FireballOpt_TestCase)
    suite3 = unittest.makeSuite(FireballRestart_TestCase)
    suite4 = unittest.makeSuite(GamessEnergy_TestCase)
    suite5 = unittest.makeSuite(GamessMd_TestCase)
    suite6 = unittest.makeSuite(GamessOpt_TestCase)
    alltests = unittest.TestSuite((suite1,suite3,suite4,suite5,suite6))
    alltests = unittest.TestSuite((suite1))
    unittest.TextTestRunner(verbosity=2).run(alltests)


# version
__id__ = "$Id: alltest.py 71 2005-04-07 23:07:02Z mmckerns $"

#  End of file 
