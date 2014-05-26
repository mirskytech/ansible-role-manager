import sys
import argparse
from abc import ABCMeta, abstractmethod

# ----------------------------------------------------------------------

class CommandException(Exception):
    pass

# ----------------------------------------------------------------------

class Command(object):
    '''
    Abstract class which is used to implement the execution of an ``arm`` command.
    
    Name of subclass is used as command name. ``help`` property should be set to describe this command.
    '''    
    
    __metaclass__ = ABCMeta    

    help = ""

    @abstractmethod
    def __init__(self, parser):
        pass
        
    @abstractmethod
    def run(self, argv):
        pass


