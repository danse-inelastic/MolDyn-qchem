# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = qchem
PACKAGE = qchem

BUILD_DIRS = \
	gamess \
	fireball \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	__init__.py \
	QChem.py \

export:: export-python-modules

# version
# $Id$

# End of file
