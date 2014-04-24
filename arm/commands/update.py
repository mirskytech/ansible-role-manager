from . import Command


class BaseCommand(Command):
    
    help = "this is a description of the update command"
    
    def __init__(self, parser):
        parser.description = self.help
        parser.add_argument('blah', help='name of the blah to update')
        parser.add_argument('-b','--bar', help='the bar parameter')
        
    def run(self, argv):
        print "running %s" % argv