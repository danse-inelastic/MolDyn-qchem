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

#include "misc.h"
#include "libqchem/hello.h"


// copyright

char pyqchem_copyright__doc__[] = "";
char pyqchem_copyright__name__[] = "copyright";

static char pyqchem_copyright_note[] = 
    "qchem python module: Copyright (c) 1998-2005 Michael A.G. Aivazis";


PyObject * pyqchem_copyright(PyObject *, PyObject *)
{
    return Py_BuildValue("s", pyqchem_copyright_note);
}
    
// hello

char pyqchem_hello__doc__[] = "";
char pyqchem_hello__name__[] = "hello";

PyObject * pyqchem_hello(PyObject *, PyObject *)
{
    return Py_BuildValue("s", hello());
}
    
// version
// $Id$

// End of file
