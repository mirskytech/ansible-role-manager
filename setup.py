#!/usr/bin/env python

import re
import os

from distutils.core import setup
from setuptools import find_packages


VERSIONFILE="ansible-role-manager/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


dependencies = [
    'ansible',
    'sphinx_bootstrap_theme',
    'sphixextension_fancybox',
]

links = [

]

setup(name='ansible-role-manager',
      version=verstr,
      description='Manager it install, uninstall and update Ansible roles',
      author='Andrew Mirsky',
      author_email='andrew@mirsky.net',
      scripts=['bin/arm'],
      url='http://ajmirsky.github.io/ansible-role-manager/',
      packages=find_packages(),
      include_package_data=True,
      install_requires=dependencies,
      dependency_links = links,
     )



