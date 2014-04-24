#!/usr/bin/env python

import os, subprocess

os.environ['ATESTVARIABLE'] = 'myrandomvalue'
value = subprocess.check_output('echo $ATESTVARIABLE', shell=True)
assert 'value' in value
print value
print os.environ
