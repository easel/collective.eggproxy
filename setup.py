# -*- coding: utf-8 -*-
# Copyright (C) 2008 Ingeniweb

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
This module contains the tool of collective.eggproxy
"""
import os
from setuptools import setup, find_packages

version = '0.4'

README = os.path.join(os.path.dirname(__file__),
          'collective', 'eggproxy', 'docs', 'README.txt')
CHANGES = os.path.join(os.path.dirname(__file__), 'CHANGES')

long_description = (
    open(README).read()
    + '\n'
    + open(CHANGES).read()
    + '\n\n'
    )

console_scripts = [
    'eggproxy_update = collective.eggproxy.update_script:updateCache',
    'eggproxy_run = collective.eggproxy.wsgi:standalone'
    ]



setup(name='collective.eggproxy',
      version=version,
      description="An egg index proxy",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='setuptools easy_install index proxy',
      author='Ingeniweb',
      author_email='support@ingeniweb.com',
      url='http://pypi.python.org/pypi/collective.eggproxy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      # uncomment this to be able to run tests with setup.py
      #test_suite = "collective.eggproxy.tests.test_eggproxydocs.test_suite",
      install_requires=[
          'setuptools',
          'PasteScript',
          # -*- Extra requirements: -*-
      ],
      tests_require=[],
      entry_points={
          'console_scripts': console_scripts,
          'paste.app_install': [
              'main = collective.eggproxy.wsgi:Installer',
              ],
          'paste.app_factory': [
              'main = collective.eggproxy.wsgi:app_factory',
              ],
          },
      )
