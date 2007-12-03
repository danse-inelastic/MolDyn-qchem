#!/usr/bin/env python
# =================================================================
#
# {LicenseText}
#
# =================================================================
#

# This is the GAMESS UI widget default settings (for energy).

ui={'comment':'','runtyp':0,'scftyp':0, 'icharg':0, 'mult':0, 'gbasis':0, 'ecm':0, 'dfttyp':0, 'gridsize':1, 'ncore':0,
        'conv':1, 'rmsdconv':1, 'iterations':50, 'memory':70, 'extrap':1, 'dirscf':1, 'damp':0, 'shift':0, 'diis':0,'soscf':0,'rstrct':0,
        'gbasisname':'AM1'}

# These are the GAMESS parameters.

# $CONTRL group, i.e. 
#   $CONTRL
#   runtyp=energy coord=unique scftyp=rhf icharg=1 mult=1 mplevl=0 
#   maxit=200 inttyp=pople icut=11 qmttol=1.0E-6
#   $END
contrl={'runtyp':'energy', 'coord':'unique', 'scftyp':'RHF', 'icharg':0, 'mult':1, 'mplevl':'0', 
        'maxit':50, 'icut':11, 'inttyp':'hondo', 'qmttol':'1.0E-6', 'dfttyp':0, 'nprint':9}
contrlGamess={'runtyp':'energy', 'coord':'unique', 'scftyp':'RHF', 'icharg':0, 'mult':1, 'mplevl':'0', 
        'maxit':50, 'icut':11, 'inttyp':'hondo', 'qmttol':'1.0E-6', 'nprint':9}
# Note: The 'dfttyp' keyword in the $CONTRL group is only valid for PC GAMESS.

# $CONTRL keywords and their optional values 
runtyp=['energy', 'optimize'] # RUNTYP
scftyp=['RHF', 'UHF', 'ROHF'] # SCFTYP
mplevl=[ 0, 0, '2'] # MPLEVL: None=0, DFT=0, MP2='2'
inttyp=['pople', 'pople', 'hondo'] # Set by EMC, None=POPLE, DFT=POPLE, MP2=HONDO
nprint=[-5,-2,7,8,9] # Not currently used. nprint is always 9 for now.

# $SCF group, i.e.
#   $SCF
#   conv=10E-05 coord=unique extrap=.T. dirscf=.T. damp=.F shift=.F. diis=.T. soscf=.F. rstrct=.F.
#   $END
scf={'nconv':1, 'extrap':'.T.', 'dirscf':'.T.', 'damp':'.F.', 'shift':'.F.', 'diis':'.T.',
     'soscf':'.F.','rstrct':'.F.'}
scfGamess={'conv':1,'extrap':'.T.', 'dirscf':'.T.', 'damp':'.F.', 'shift':'.F.', 'diis':'.T.',
     'soscf':'.F.','rstrct':'.F.'}
# Note: Keyword 'conv' is used by GAMESS, 'nconv' is used by PC GAMESS.

# CONV keyword and its optional values
conv=['10E-04','10E-05','10E-06','10E-07'] # Density Convergence

# Useful true or false tuple.
tf=['.F.', '.T.'] # True/False for SCF parameters

# $SYSTEM group, i.e.
#   $SYSTEM
#   timlim=1000 memory=70000000
#   $END
system={'timlim':1000, 'memory':70000000}

# $MP2 group, i.e.
#   $MP2
#   ncore=0
#   $END
# The $MP2 group is written only when the Electron Correlation Method = MP2.
# To include core electrons, we add the keyword NCORE=0.
# To exclude core electrons, we leave NCORE out of the $MP2 group altogether.
# So, with the checkbox not checked, ncore=0, and the NCORE keyword isn't written.
# With the checkbox checked, ncore='0' (string type), NCORE=0 is written.  
mp2={'ncore':0} # Core electrons for MP2
ncore=[0, '0'] # Core electrons: Not included=0, Included='0'. 

# Useful Electron Correlation Method variables.
ecm=['None', 'DFT', 'MP2'] 
DFT=1
MP2=2

# $DFT group section (GAMESS only) ##############################
#
# The general form for the $DFT group is (keyword order does not matter):
#
#   $DFT
#    dfttyp=SLATER nrad=96 nthe=12 nphi=24 switch=3.0E-04
#   $END
#
# $DFT group keywords and their default values.
dft={'dfttyp':0, 'nrad':0}
# Note: In PC GAMESS, the $DFT group contains the grid size parameters 
# only, and the DFTTYP keyword is placed in the $CONTRL group.

# DFTTYP functions for GAMESS, specified by the DFTTYP keyword in the $DFT group.
# The PC GAMESS DFTTYP functions are different (see pcgms_dfttyp_items).
# The DFTTYP keyword values are the same without the '(x)' text.  The selected
# item is written to the $DFT group like this: dfttyp=SLATER
dfttyp_itemsGamess=['SLATER (E)','BECKE (E)','GILL (E)','PBE (E)','VWN (C)', \
    'LYP (C)', 'OP (C)', 'SVWN (E+C)', 'SLYP (E+C)', 'SOP (E+C)', 'BVWN (E+C)', \
    'BLYP (E+C)', 'BOP (E+C)', 'GVWN (E+C)', 'GLYP (E+C)', 'GOP (E+C)', \
    'PBEVWN (E+C)', 'PBELYP (E+C)', 'PBEOP (E+C)', 'BHHLYP (H)', 'B3LYP (H)']

# DFTTYP functions for PC GAMESS. These are different for GAMESS.
# The DFTTYP keyword values are the same without the '(x)' text.                
dfttyp_items = ['From Fireball Fdata','SLATER (E)','B88 (E)','GILL96 (E)','XPBE96 (E)','LYP (C)', \
    'VWN1RPA (C)','VWN5 (C)','PW91LDA (C)','CPBE96 (C)','CPW91 (C)', \
    'SLYP (E+C)','BLYP (E+C)','GLYP (E+C)','SVWN1RPA (E+C)', \
    'BVWN1RPA (E+C)','VWN5 (E+C)','BVWN5 (E+C)','PBE96 (E+C)', \
    'PBEPW91 (E+C)','B3LYP1 (H)','BELYP5 (H)','BHHLYP (H)','PBE0 (H)', \
    'PBE1PW91 (H)','B3PW91 (H)']

# The 5 DFT grid size parameters for:
#   - Coarse
#   - Default, 
#   - Fine
#   - Very Fine
#   - Very very fine.
# These are the $DFT grid size parameters for GAMESS.
gridsizeGamess= ['=48 nthe=12 nphi=24 switch=1.0E-03', \
                '96 nthe=12 nphi=24 switch=3.0E-04', \
                '96 nthe=24 nphi=48 switch=3.0E-04', \
                '96 nthe=36 nphi=72 switch=3.0E-04']#, \
                #'96 nthe=36 nphi=72 switch=3.0E-04']
# Note: the first number is the 'nrad' parm. 'nrad=' is printed by the prin1 method.
# The last one may need to be changed.
                
# These are the $DFT grid size parameters for PC GAMESS.
gridsize=['48 lmax=19', \
        '63 lmax=29', \
        '63 lmax=53', \
        '95 lmax=89', \
        '128 lmax=131']
# Note: the first number is the 'nrad' parm. 'nrad=' is printed by the prin1 method.

# $GUESS group, i.e.
#   $GUESS
#    guess=huckel
#   $END
guess={'guess':'huckel'}

# The GUESS keyword and its optional values
guess_keyword=['huckel', 'moread']
# Note: Writing the 'guess' keyword requires special case code in the prin1 method 
# since its group name is the same ('guess').
    
# $STATPT group, i.e.
#   $STATPT
#    hess=guess
#   $END
statpt={'hess':'guess', 'opttol':1}

# The HESS keyword and its optional values
hess=['guess', 'read']

# OPTTOL keyword and its optional values
opttol=[0.0001, 0.00001, 0.000001, 0.0000001] # RMSD Convergence

# $BASIS group, i.e.
#   $BASIS
#   gbasis=AM1 NGAUSS=0 NDFUNC=0 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.
#   $END
basis={'gbasis':'AM1'}

# gbasis choices
gbasisChoices=['Derive from Fdata',\
    'AM1', \
    'PM3', \
    "STO-3G", \
    "STO-6G", \
    "3-21G", \
    "3-21G*", \
    "6-31G", \
    "6-31G(d)", \
    "6-31G(d,p)", \
    "6-31+G(d)", \
    "6-31+G(d,p)", \
    "6-31++G(d)", \
    "6-31++G(d,p)", \
    "6-311G", \
    "6-311G(d)", \
    "6-311G(d,p)", \
    "6-311+G(d,p)", \
    "6-311++G(d,p)"]


# The GBASIS keyword and its optional values
gbasis=['AM1 NGAUSS=0 NDFUNC=0 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'PM3 NGAUSS=0 NDFUNC=0 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'STO NGAUSS=3 NDFUNC=0 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'STO NGAUSS=6 NDFUNC=0 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'N21 NGAUSS=3 NDFUNC=0 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'N21 NGAUSS=3 NDFUNC=1 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'N31 NGAUSS=6 NDFUNC=0 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'N31 NGAUSS=6 NDFUNC=1 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'N31 NGAUSS=6 NDFUNC=1 NPFUNC=1 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'N31 NGAUSS=6 NDFUNC=1 NPFUNC=0 NFFUNC=0 DIFFSP=.T. DIFFS=.F.', \
    'N31 NGAUSS=6 NDFUNC=1 NPFUNC=1 NFFUNC=0 DIFFSP=.T. DIFFS=.F.', \
    'N31 NGAUSS=6 NDFUNC=1 NPFUNC=0 NFFUNC=0 DIFFSP=.T. DIFFS=.T.', \
    'N31 NGAUSS=6 NDFUNC=1 NPFUNC=1 NFFUNC=0 DIFFSP=.T. DIFFS=.T.', \
    'N311 NGAUSS=6 NDFUNC=0 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'N311 NGAUSS=6 NDFUNC=1 NPFUNC=0 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 NFFUNC=0 DIFFSP=.F. DIFFS=.F.', \
    'N311 NGAUSS=6 NDFUNC=1 NPFUNC=0 NFFUNC=0 DIFFSP=.T. DIFFS=.F.', \
    'N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 NFFUNC=0 DIFFSP=.T. DIFFS=.F.', \
    'N311 NGAUSS=6 NDFUNC=1 NPFUNC=0 NFFUNC=0 DIFFSP=.T. DIFFS=.T.', \
    'N311 NGAUSS=6 NDFUNC=1 NPFUNC=1 NFFUNC=0 DIFFSP=.T. DIFFS=.T.']


from qchem.gamess.Group import Group

class GamessInputFile:
    '''class for the gamess input file'''
    
    def __init__(self):
        #self.name = name or "" # Parms set name, assumed to be a string by some code
        self.contrl = Group('CONTRL', contrl) # $CONTRL group object
        self.scf = Group('SCF', scf) # $SCF group object
        self.system = Group('SYSTEM', system) # $SYSTEM group object
        self.mp2 = Group('MP2', mp2) # $MP2 group object
        self.dft = Group('DFT', dft) # $DFT group object
        self.guess = Group('GUESS', guess) # $GUESS group object
        self.statpt = Group('STATPT', statpt) # $STATPT group object
        self.basis = Group('BASIS', basis) # $BASIS group object
        self.data = Group('DATA', data) # $DATDA group object
        
    def write(self):
        'Write all parms to input file'
        f = file('INPUT','w')
        self.contrl.write(f)
        self.scf.write(f)
        self.system.write(f)
        self.mp2.write(f)
        self.dft.write(f)
        self.guess.write(f)
        self.statpt.write(f)
#        self.force.write()
        self.basis.write(f)
        f.close()
        
        