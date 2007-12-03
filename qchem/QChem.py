#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
#                              
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from sample.Sample import Sample
installDir='/home/brandon/DANSE'
from pyre.components.Component import Component
from qchem.gamess.GamessInputFile import dfttyp_items

class QChem(Component):
    '''This class serves as an interface for quantum chemistry engines.'''

    class Inventory(Component.Inventory):
        '''this is the inventory; the defaults are for the GAMESS engine'''
        import pyre.inventory as inv  
        comment=inv.str('Comment',default='Quantum Chemistry Run')
        comment.meta['tip'] = "comment for this calculation"
        correlationTheory = inv.str('Correlation Theory',default='Hartree Fock')
        correlationTheory.meta['tip'] = '''level of correlation'''
        correlationTheory.validator = inv.choice(['Hartree Fock', 'DFT', 'Moller-Plesset'])
        dftType = inv.str('DFT Type', default=dfttyp_items[0])
        dftType.meta['tip'] = '''type of dft used'''
        dftType.validator = inv.choice(dfttyp_items)
        directCalc = inv.bool('Direct Calculation', default=False)
        directCalc.meta['tip'] = '''run the calculation in RAM and avoid hard disk usage for integral storage'''
        dumpFrequency = inv.float('dumpFrequency (ps)', default=0.001)
        dumpFrequency.meta['tip'] = '''frequency at which a restart file is written'''
        electronDensityConvergence = inv.str('Electron Density Convergence', default='10E-04')
        electronDensityConvergence.meta['tip'] = """accuracy of the electron density convergence for the calculation (CONV)"""
        ensemble= inv.str('Ensemble', default='NVE')
        ensemble.meta['tip'] = 'thermodynamic ensemble'
        ensemble.validator = inv.choice(['NVE','NVT'])
        equilibrationTime = inv.float('Equilibration Time (ps)', default=0.0)
        equilibrationTime.meta['tip'] = 'equilibration time of the simulation (ps)'
        exchangeCorrelationTheory = inv.str('Exchange Correlation Theory',default='Grid (Gamess)')
        exchangeCorrelationTheory.meta['tip'] = 'the type of approximation used in expanding xc functional'
        exchangeCorrelationTheory.validator = inv.choice(['Grid (Gamess)','Horsfield (Fireball)','Sankey-Niklewski (Fireball)','Mcweda (Fireball)'])
        gradientConvergence = inv.float('Gradient Convergence', default = 0.0001)
        gradientConvergence.meta['tip']="""Gradient convergence tolerance (OPTTOL), in Hartree/Bohr. Convergence of a geometry search requires the largest component of the gradient to be less than this value, and the root mean square gradient less than 1/3 of this value"""
        gridSpacing = inv.str('Grid Spacing (Gamess)',default='Default')
        gridSpacing.meta['tip'] = """the grid spacing for the DFT calculation."""
        gridSpacing.validator = inv.choice(['Coarse', 'Default', 'Fine','Very Fine'])
        icharge=inv.float('Overall Charge',default=0.0)
        icharge.meta['tip']='''overall charge on the system'''
        includeCoreElectrons = inv.bool('Include Core Electrons', default=False) 
        includeCoreElectrons = """whether or not to include core electrons in the MP2 calculation"""
#        inputDeckName = inv.str('Input Filename', default = 'gulp.gin')
#        inputDeckName.meta['tip'] = '''input file for md executable'''
#        integrator = inv.str('Integrator', default='velocity-verlet')
#        integrator.meta['tip'] = 'type of integrator'
#        integrator.validator = inv.choice(['predictor-corrector','velocity-verlet'])
        logFilename = inv.str('Log Filename', default='Qchem.log')
        logFilename.meta['tip'] = 'name of log file for md run'
        maxScfIterations = inv.int('Max Scf Iterations', default = 50)
        maxScfIterations.meta['tip'] = """Maximum number of SCF iteration cycles"""
        memory=inv.float('Memory', default=None)
        memory.meta['tip']="""System memory reserved for calculation"""
        productionTime = inv.float('Production Time (ps)', default=1.0)
        productionTime.meta['tip'] = 'production time of the simulation (ps)'
        restartFilename = inv.str('Restart Filename', default = 'Qchem.res')
        restartFilename.meta['tip'] = '''restart file for second run'''
        runtype=inv.str('Run Type', default='Energy')
        runtype.validator = inv.choice(['Energy','Optimize','Md'])
        runtype.meta['tip'] = 'type of quantum chemistry run'
        runtype.meta['importance'] = 200
        sample = inv.facility('Sample', default=Sample())
        sample.meta['tip'] = 'sample containing system information'
        sample.meta['importance'] = 100
        sampleFrequency = inv.float('Property Sampling Frequency (fs)', default=5.0)
        sampleFrequency.meta['tip'] = '''frequency at which sampled properties are written to trajectory and log file'''
        scftype=inv.str('SCF Type', default='RHF (Gamess)') 
        scftype.meta['tip']='type of self-consistency'
        scftype.validator = inv.choice(['RHF (Gamess)','UHF (Gamess)', 'ROHF (Gamess)','Harris (Fireball)','Self-Consistent Harris (Fireball)','Extended-Hubbard (Fireball)'])
        thermostatParameter = inv.str('Thermostat Parameter', default = '0.005')
        thermostatParameter.meta['tip'] = '''thermostat parameter to keep fluctuations relatively small'''     
        title = inv.str('Title', default='')
        title.meta['tip'] = 'title of the calculation'  
        timeStep = inv.float('Time Step (fs)', default=0.5)
        timeStep.meta['tip'] = 'integration time step'
        trajectoryFilename = inv.str('Trajectory Filename', default='Qchem.xyz')
        trajectoryFilename.meta['tip'] = 'name of trajectory file'
#        trajectoryType = inv.str('trajectoryType', default = 'xyz')
#        trajectoryType.meta['tip'] = '''type of trajectory file'''
        unpairedElectrons=inv.int('Unpaired Electrons', default=0)
        unpairedElectrons.meta['tip']="""N + 1, where N is the number of unpaired electrons (MULT)."""
        usePreviousCoordinates = inv.bool('Use Previous Coordinates', default=False)
        usePreviousCoordinates = """start from the coordinates of a previous run. Requires that both the molecule and basis set be identical.  Useful for restarted calculations and starting orbitals for electron correlation methods."""
        usePreviousGradient = inv.bool('Use Previous Gradient', default=False)
        usePreviousGradient.meta['tip'] = """start from a gradient from a previous run.  Only works for identical molecules."""
                        
    def __init__(self,name='QChem'):
        Component.__init__(self, name, facility=None)
        self.i=self.inventory
    
    def equilibrationSteps(self):
        if self.i.timeStep==0:
            raise Exception, 'please set the time step to a nonzero value'
        else:
            return int(self.i.equilibrationTime/self.i.timeStep)
    
    def productionSteps(self):
        if self.i.timeStep==0:
            raise Exception, 'please set the time step to a nonzero value'
        else:
            return int(self.i.productionTime/self.i.timeStep)
        
    def execute(self):
        raise NotImplementedError("class %r must override 'integrate'" % self.__class__.__name__)

#    def energy(self):
#        raise NotImplementedError("class %r must override 'integrate'" % self.__class__.__name__)
#
#    def optimize(self):
#        raise NotImplementedError("class %r must override 'integrate'" % self.__class__.__name__)
#
#    def integrate(self):
#        raise NotImplementedError("class %r must override 'integrate'" % self.__class__.__name__)

# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Mon Apr 16 12:44:30 2007

# End of file 