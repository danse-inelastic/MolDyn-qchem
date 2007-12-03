from pyregui.pyreui import mainTemplate
from pyregui.guitoolkit import wx
from QChemApp import QChemApp


def qChem():
    mainTemplate(wx, '/home/jbk/DANSE/qchem/applications/QChemApp.py')
    
    

    
    
if __name__=='__main__': qChem()