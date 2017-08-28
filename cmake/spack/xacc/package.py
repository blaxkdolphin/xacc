##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install xacc
#
# You can edit this file again by typing:
#
#     spack edit xacc
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Xacc(CMakePackage):
    """XACC provides a plugin infrastructure for 
       programming, compiling, and executing quantum 
       kernels in a language and hardware agnostic manner."""

    homepage = "https://ornl-qci.github.io/xacc"

    version('develop', git='https://github.com/ornl-qci/xacc.git')

    variant('python', default=False,
            description='Turn on XACC Python support')
    variant('mpi', default=False, description='Turn on XACC MPI support')
    variant('tnqvm', default=False, description='Include TNQVM Accelerator')

    depends_on('cppmicroservices')
    depends_on('cpprestsdk')
    depends_on('boost+mpi+graph')
    depends_on('mpi', when='+mpi')
    depends_on('python', when='+python')
    depends_on('tnqvm', when='+tnqvm')
    
    def cmake_args(self):
        args = []
        return args