import os, shutil, sys, re
from . import Command
from arm.util import get_playbook_root
import argparse, os
from git import Repo

class BaseCommand(Command):
        
    help = "remove a role"    
    
    def __init__(self, parser):
        parser.description = self.help
        #parser.add_argument('command_name', nargs='?', help='name of command to get help')
        parser.add_argument('-u','--unlink',action='store_true', help="remove link but leave in library")

        
    def run(self, argv):
        
        
        
        import subprocess
        try:
            p = subprocess.Popen(['xcodebuild','-version'], stdout=subprocess.PIPE)
            out, err = p.communicate()
            ver_re = re.compile('(?P<version>\d(.\d){0,2})')
            ver_match = ver_re.search(out)
            if not os.environ.get('ARCHFLAGS',False) \
               and ver_match \
               and LooseVersion('5.1') <= LooseVersion(ver_match.groupdict()['version']):
                print "Warning : `pycrypto` on OSX with XCode >= 5.1 will not compile without ARCHFLAGS being set. see docs."
        except OSError as e:
            # we're probably not running on OSX
            pass
        
        _root = get_playbook_root(os.getcwd())
        _roles_directory = os.path.join(_root, 'roles')
       
        #for root, dir, files in os.walk(os.path.join(_root, 'library_roles/')):
            #for f in files:
                #print "r: %s/%s" % (root, f)
           
                
        

        
        
