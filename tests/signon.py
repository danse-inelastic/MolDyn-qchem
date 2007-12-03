#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 

if __name__ == "__main__":

    import qchem
    from qchem import qchem as qchemmodule

    print "copyright information:"
    print "   ", qchem.copyright()
    print "   ", qchemmodule.copyright()

    print
    print "module information:"
    print "    file:", qchemmodule.__file__
    print "    doc:", qchemmodule.__doc__
    print "    contents:", dir(qchemmodule)

    print
    print qchemmodule.hello()

# version
__id__ = "$Id$"

#  End of file 
