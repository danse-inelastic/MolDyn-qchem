#!/usr/bin/env python
# =================================================================
#
# {LicenseText}
#
# =================================================================
#
from qchem.QChem import QChem
from os import system, linesep
#from SimCommon import SimCommon #use this to put global settings like working directory, installation directories, etc.
  
class Cpmd(QChem):#,SimCommon):
    """Cpmd engine for QChem interface.  
    
This class maps the DANSE data structures to Cpmd's input deck"""

    class Inventory(QChem.Inventory):
        import pyre.inventory as inv
#        basisSet = inv.str('Basis Set', default=gbasisChoices[0])
#        basisSet.meta['tip'] = """type of basis set used in the calculation"""
#        basisSet.validator = inv.choice(gbasisChoices)
        cutoff = inv.str('Basis set cutoff (Rydberg)', default='70')
        cutoff.meta['tip'] = '''plane wave basis set cutoff'''
        functional = inv.str('DFT Functional', default='BLYP')
        functional.meta['tip'] = '''type of dft functional to use'''
  
    def __init__(self):
        QChem.__init__(self)
        self.i=self.inventory
        self.i.productionSteps=1
        self.inputFile
        
    def _configure(self):
        QChem._configure(self)
        
    def _defaults(self):
        QChem._defaults(self)
    
    def printWarnings(self):
        pass
   
    def writeInfo(self):
        '''writes out the run info'''
        return '&INFO'+linesep+' '+self.i.title+linesep+'&END'+linesep+linesep

    def writeCpmd(self):
        '''writes the main cpmd section'''
        lines=''
        runTypeTranslate={'Energy':'OPTIMIZE WAVEFUNCTION', 'Optimize':'OPTIMIZE GEOMETRY', 'Md':'MOLECULAR DYNAMICS'}
        lines+=runTypeTranslate[self.i.runType]+linesep
        return '&CPMD'+linesep+lines+linesep+'&END'+linesep+linesep

    def writeSystem(self):
        '''writes the system information'''
        lines=''
        # write the cell vectors
        uc=self.i.sample.i.atomicStructure.i.unitCell
        lines+=' CELL VECTORS '+linesep+' '+uc.a+linesep+' '+uc.b+linesep+' '+uc.c+linesep
        lines+=' CUTOFF'+linesep+self.i.cutoff+linesep
        return '&SYSTEM'+linesep+' ANGSTROM'+linesep+lines+linesep+'&END'+linesep+linesep
    
    def writeDft(self):
        '''writes the dft information'''
        lines=''
        lines+=' FUNCTIONAL '+linesep+self.i.functional+linesep
        return '&DFT'+linesep+lines+linesep+'&END'+linesep+linesep
    
    def writeAtoms(self):
        '''writes the atomic information'''
        aip=self.i.atomicInputPanel
        coordinatesBySpecies = aip.getCoordinatesBySpecies()
        psuedoPotentialsBySpecies = aip.getPseudoPotentialsBySpecies()
        numSpecies=aip.getNumSpecies()
        lines=''
        for i in range(numSpecies):
            lines+=psuedoPotentialsBySpecies[i]
            
        uc=self.i.sample.i.atomicStructure.i.atoms
        lines+=' CELL VECTORS '+linesep+' '+uc.a+linesep+' '+uc.b+linesep+' '+uc.c+linesep
        lines+=' CUTOFF'+linesep+' '+self.i.cutoff+linesep
        return '&ATOMS'+linesep+' ANGSTROM'+linesep+lines+linesep+'&END'+linesep+linesep
           
    def writeBas(self):
        '''writes out the run info'''
        atoms=eval(self.i.sample.i.atoms)
        bas=file('fireball.bas','w')
        print >>bas, str(len(atoms))
        for atom in atoms:
            print >>bas, self.periodicTable.index(atom[0])+1,atom[1],atom[2],atom[3]
        bas.close()
        
    def writeLvsFile(self):
        '''writes out the lattice vectors to a *.lvs file'''
        unitCell=eval(self.i.sample.i.unitCell)
        lvs=file('fireball.lvs','w')
        for dim in unitCell:
            print >>lvs, dim[0],dim[1],dim[2]
        lvs.close()

    def writeScriptInput(self):
        '''write script.input'''
        #first initialize temperature if it isn't already set
        if self.i.sample.i.temperature==None:
            self.i.sample.i.temperature=0
        f=file('script.input','w')
        fileContents = "fireball.bas                                basis file\n"\
        +"fireball.lvs                                lattice vector filename\n"\
        +"automatic                                   kpt preference\n"\
        +"1,"+str(self.productionSteps())+"                                   initstep,finalstep\n"\
        +str(self.i.timeStep)+"                                       time step (fs)\n"\
        +"fire.xv                                        xv file name\n"\
        +"fire.ac                                        ac file name\n"\
        +str(self.i.sample.i.temperature)+"                                    tavg, initial temperature\n"\
        +str(self.i.sample.i.temperature)+"                                    end temperature\n"   
        f.write(fileContents)
        f.close()
        
    def writeOptionsInput(self,md=True,opt=False):
        '''writes fireball's options.input file'''
        f=file('options.input','w')
        if self.i.scftype=='Self-Consistent Harris (Fireball)':
            functionalTheory="1"
        elif self.i.scftype=='Harris (Fireball)':
            functionalTheory="0"
        elif self.i.scftype=='Extended-Hubbard (Fireball)':
            functionalTheory="2"
        else:
            functionalTheory="-1" #obviously wrong
        ispin="0"
        if self.i.exchangeCorrelationTheory=='Horsfield (Fireball)':
            exchangeCorrelationTheory="0"
        elif self.i.exchangeCorrelationTheory=='Sankey-Niklewski (Fireball)':
            exchangeCorrelationTheory="1"
        elif self.i.exchangeCorrelationTheory=='Mcweda (Fireball)':
            exchangeCorrelationTheory="2"
        else:
            exchangeCorrelationTheory="-1" #obviously wrong
        max_scf_iterations="20"
        iqout="1"
        qstate="0"
        if opt:
            quench="-3"
        else:
            quench="0"
        if md:            
            if self.i.ensemble=='nve': ensemble="0"
            if self.i.ensemble=='nvt': ensemble="1"
        else:
            ensemble="0"
        ibarrier="0"
        centerOfMass="1"
        angularMomentum="1"
        initialVelocity="1"
        fixCharges="0"
        fixNeighbors="0"
        icluster="0"
        iordern="0"
        iumbrella="0"
        vanDerWaals="0"
        gauss="0"
        iimage="0"
        fileContents = functionalTheory \
            + "                    itheory (0=Harris, 1=DOGS, 2=Ext-hubbard)\n" \
            + ispin \
            + "                    ispin\n" \
            + exchangeCorrelationTheory \
            + "                    itheory_xc (0=HXC, 1=SNXC, 2=OLSXC)\n" \
            + max_scf_iterations \
            + "                   max_scf_iterationis (irrelevant for Harris)\n" \
            + iqout \
            + "                    iqout (Lowdin = 1, Mulliken = 2)\n" \
            + qstate \
            + "                  qstate\n" \
            + quench \
            + "                    iquench\n" \
            + ensemble \
            + "                    iensemble\n" \
            + ibarrier \
            + "                    ibarrier\n" \
            + centerOfMass \
            + " " \
            + angularMomentum \
            + " " \
            + initialVelocity \
            + " 1              The big 4 constraints\n" \
            + fixCharges \
            + "                    ifixcharges\n" \
            + fixNeighbors \
            + "                    ifixneigh\n" \
            + icluster \
            + "                    icluster (0=Periodic, 1=Cluster)\n" \
            + iordern \
            + "                    iordern\n" \
            + iumbrella \
            + "                    iumbrella\n" \
            + vanDerWaals \
            + "                    ivdw (Van der Waals)\n" \
            + gauss \
            + "                    igauss (Gaussian Approach)\n" \
            + iimage \
            + "                    iimage (Reimage atoms)\n" \
            + "0                    ipathintegral\n"  \
            + "0                    idynmat (Dynamic Matrix)\n" \
            + "0                    iexfield\n" \
            + "0                    ithermoint\n" \
            + "0                    ireducekpts\n" \
            + "0                       iendTemp\n"
        f.write(fileContents)
        f.close()
        
    def writeFdataOptional(self):
        '''writes Fdata.optional to stdout'''
        f=file('Fdata.optional','w')
        f.write(self.i.sample.i.basisSet) 
        f.close()           
    
    def writeOutputInput(self):
        '''writes options.output to stdout'''
        f=file('output.input','w')
        fileContents = "0                               iwrtcdcoefs (coefficients for wavefunctions)\n"\
                    +"0                               iwrtcharges (writes out Lowdin or Mulliken)\n"\
                    +"0                               iwrtdensity (write out density matrix)\n"\
                    +"1                               iwrteigen (writes out the energy eigenvalues)\n"\
                    +"0                               iwrtefermi (write out fermi occupations)\n"\
                    +"0                               iwrtfpieces (writes out force components)\n"\
                    +"0                               iwrthampiece (write pieces of H matrix)\n"\
                    +"0                               iwrtcomponents (write components of ebs energy)\n"\
                    +"0                               iwrtneigh (write out neighbor map)\n"\
                    +"0                               iwrtneigh_com (write out common neighbor map)\n"\
                    +"1                               iwrtxyz (write out xyz movie file)\n"\
                    +"0                               iwrtdos (write out dos files)\n"\
                    +"0                               iwrthop (write out hopping values for STM)\n"\
                    +"0                               iwrtatom (write out the Atomo_i files)\n"\
                    +"0                               iwrtpop (write out population file)\n"\
                    +"0                               iwrtHS (write out H & S file)\n"\
                    +"0                               iwrtvel (write out VELOCITY.dat file)\n"
        f.write(fileContents)
        f.close()
        
    def writeQuenchOptional(self):
        '''writes the quench.optional file containing quenching info'''
        f=file('quench.optional','w')
        tempwanted = "0.0"; taurelax = "50."
        fileContents = "0.001                   energy tolerance\n"\
                    +"0.05                     force tolerance\n"\
                    +tempwanted+"                      Temperature wanted\n"\
                    +taurelax+"                     taurelax for simulated annealing\n";
        f.write(fileContents)
        f.close()

    def setMdDefaults(self):
        '''set defaults for an md run'''
        self.i.timeStep=0.25
        self.i.equilibriumTime=0.0
        self.i.productionTime=25
    
    def setOptDefaults(self):
        '''set defaults for an optimization'''
        self.i.timeStep=0.25
        self.i.equilibriumTime=0.0
        self.i.productionTime=25
        
    def setEnergyDefaults(self):
        '''set defaults for an energy calc'''
        self.i.timeStep=0.25
        self.i.equilibriumTime=0.0
        self.i.productionTime=0.0

    def integrate(self):
        '''integrates an MD trajectory forward in time'''
        self.printWarnings()   
        self.setMdDefaults()     
        self.writeBasFile()
        self.writeLvsFile()
        self.writeFdataOptional()
        self.writeScriptInput()
        self.writeOptionsInput(md=True, opt=False)
        self.writeOutputInput()
        self.writeQuenchOptional()
        system(self.i.engineExecutablePath+' > '+self.i.logFilename+' 2>&1')
        
    def optimize(self):
        '''optimize a unit cell'''
        self.printWarnings()
        self.setOptDefaults()
        self.writeBasFile()
        self.writeLvsFile()
        self.writeFdataOptional()
        self.writeScriptInput()
        self.writeOptionsInput(md=False, opt=True)
        self.writeOutputInput()
        self.writeQuenchOptional()
        system(self.i.engineExecutablePath+' > '+self.i.logFilename+' 2>&1')
        
    def energy(self):
        '''calculate the energy of a system'''
        self.printWarnings()   
        self.setEnergyDefaults()     
        self.writeBasFile()
        self.writeLvsFile()
        self.writeFdataOptional()
        self.writeScriptInput()
        self.writeOptionsInput(md=False, opt=False)
        self.writeOutputInput()
        self.writeQuenchOptional()
        system(self.i.engineExecutablePath+' > '+self.i.logFilename+' 2>&1')
        
    def execute(self):
        '''execute the fireball run'''
        if self.i.runtype=='energy':
            self.energy()
        elif self.i.runtype=='optimize':
            self.optimize()
        elif self.i.runtype=='md':
            self.md()
  
# version
__id__ = "$Id$"
 
# End of file