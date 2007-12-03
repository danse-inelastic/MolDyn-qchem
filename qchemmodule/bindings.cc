// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Michael A.G. Aivazis
//                        California Institute of Technology
//                        (C) 1998-2005  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <portinfo>
#include <Python.h>

#include "bindings.h"

#include "misc.h"          // miscellaneous methods

// the method table

struct PyMethodDef pyqchem_methods[] = {

    // dummy entry for testing
    {pyqchem_hello__name__, pyqchem_hello,
     METH_VARARGS, pyqchem_hello__doc__},

    {pyqchem_copyright__name__, pyqchem_copyright,
     METH_VARARGS, pyqchem_copyright__doc__},


// Sentinel
    {0, 0}
};

// version
// $Id$

// End of file
