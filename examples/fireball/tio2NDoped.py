#script to optimize the crystal structure of (NH2)2CO (urea)
from sample.Sample import Sample
from applications.QChemApp import QChemApp
import danseGlob
from os import sep
# set up the sample with atoms, periodicity, atomic interactions
sample = Sample()        
sample.i.unitCell = '''[[4.58666, 0.0, 0.0], 
                    [0.0, 4.58666, 0.0], 
                    [0.0, 0.0, 2.95407]]'''
sample.i.atoms='''[['Ti', 0.0, 0.0, 0.0],
['Ti', 2.29333,     2.29333,     1.477035],
['O',  1.397509435, 1.397509435, 0.0],
['O',  3.189150565, 3.189150565, 0.0],
['O',  3.690839435, .8958205646, 1.477035000],
['O',  .8958205646, 3.690839435, 1.477035000]]'''
sample.i.basisSet='/home/brandon/Fdata3t_Os3.6_p4.1_Tis6.3_p6.8_d5.7/'

# invoke the application and set its inventory
app = QChemApp()
qm = app.i.quantumEngine
qm.i.sample=sample
qm.i.scftype='self-consistentHarris'
qm.i.exchangeCorrelationTheory='mcweda'
qm.i.engineExecutablePath='/home/brandon/myFireball-bin/fireball.x'
qm.i.logFilename = 'tio2Natom.log'
app.run()

