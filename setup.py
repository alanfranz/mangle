#!/usr/bin/env python

# Copyright (C) 2010  Alex Yatskov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
from setuptools import setup

setup(name='mangle',
      description='Mangle',
      version='20111118',
      author='FooSoft',
      license='GPL3',
      include_package_data=True,
      keywords='manga kindle',
      url='https://github.com/alanfranz/mangle',
      packages=['mangle', 'mangle.ui', 'mangle.img'],
     )
