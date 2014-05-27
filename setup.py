#!/usr/bin/env python

import os, re, sys
from distutils.version import LooseVersion
from distutils.core import setup
from setuptools import find_packages


VERSIONFILE="arm/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


dependencies = [
    'ansible',
    'requests',
    'gitpython==0.3.2.RC1',
    'semantic_version',
    'colorama',
    'hgapi',
]

links = [

]

# pycrypto is a dependency of ansible & git-python and has issues compiling on OSX with XCode 5.1 and above.
# display warning. need to set this before running setup for ansible-role-manager
# >> export ARCHFLAGS='-Wno-error=unused-command-line-argument-hard-error-in-future'
if 'install' in sys.argv:
    import subprocess
    try:
        p = subprocess.Popen(['xcodebuild','-version'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        ver_re = re.compile('(?P<version>\d(.\d){0,2})')
        ver_match = ver_re.search(out)
        if not os.environ.get('ARCHFLAGS',False) \
           and ver_match \
           and LooseVersion('5.1') <= LooseVersion(ver_match.groupdict()['version']):
            
            print "Warning :"
            print "\t`pycrypto` on OSX with XCode 5.1 and above will not compile without ARCHFLAGS being set."
            print "\tsee http://mirskytech.github.io/ansible-role-manager/installation.html"
    
    except OSError as e:
        # we're probably not running on OSX
        pass

with open('README.rst') as file:
    long_description = file.read()

setup(name='ansible-role-manager',
      version=verstr,
      description='A tool for installing and managing Ansible roles, playbooks & modules.',
      author='Andrew Mirsky',
      author_email='andrew@mirskytech.com',
      scripts=['bin/arm'],
      url='http://mirskytech.github.io/ansible-role-manager/',
      packages=find_packages(),
      include_package_data=True,
      install_requires=dependencies,
      dependency_links = links,
      long_description=long_description
     )



