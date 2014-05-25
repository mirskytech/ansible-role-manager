# ----------------------------------------------------------------------

# Playbook subdirectory which stores the role dependencies
# TODO : should be an option, which can be set in the ``.arm`` configuration file or on the cmd line

import os, itertools
import ConfigParser

class SettingsError(Exception):
    pass
        
        
class Settings(dict):

    config_parser = ConfigParser.ConfigParser()
    config_default = os.path.join(os.path.dirname(__file__),'defaults.ini')

    
    config_files = [
        os.path.realpath('~/.arm'),
    ]    
    
    def __init__(self):
        
        self.config_parser.readfp(open(self.config_default))        
        self.config_parser.read(self.config_files)
                
    def get(self, item, default=None):
        if hasattr(self, item):
            print item
            return self.__getattr__(item)
        return default
        
    def __getattr__(self, item):
        
        option, section = None, None
        print item
        if '.' in item:
            section,option = item.split('.')
            if self.config_parser.has_option(section,option):
                return self.config_parser.get(section,option)
        elif '__' in item:
            section,option = item.split('__')
        
        if section and self.config_parser.has_option(section,option):
            return self.config_parser.get(section, option)
        
        all_options = [self.config_parser.items(section) for section in self.config_parser.sections()]
        all_options = dict(itertools.chain.from_iterable(all_options))
        print all_options
            
        raise SettingsError("could not find section '%s' with option '%s'" % (section,option))
    
    def __getitem__(self,name):
        
        if '.' in name or '__' in name:
            return self.__getattr__(item)
        
        if name in self.config_parser.sections():
            return dict(self.config_parser.items(name))
    
    #def __hasattr__(self, name):
        #if super(Settings,self).__hasattr__(name):
            #return True
        #section,option = name.split('.')
        #return self.config_parser.has_option(section,option)
    
    
settings = Settings()
            
        
        
