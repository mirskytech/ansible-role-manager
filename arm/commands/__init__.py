import sys
import argparse


class Command(object):
    
    help = ""
    
    def __init__(self):
        pass
        
    def run(self, argv):
        raise NotImplemented('please run method in subclass')
