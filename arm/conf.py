# ----------------------------------------------------------------------

# Playbook subdirectory which stores the role dependencies
# TODO : should be an option, which can be set in the ``.arm`` configuration file or on the cmd line

import os, itertools
import ConfigParser
from util import get_playbook_root

class SettingsError(Exception):
    pass
        
        
        
# #######################################################################
        
        
class SettingsHelper(dict):
    
    """
    An object which contains settings from 'default.ini' and can be accessed by:

    - ``settings['section__variable']``
    - ``settings['section.variable']``
    - ``settings['section']['variable']``
    - ``settings.section.variable``
    - ``settings['section'].variable``
    - ``settings.variable``**
    
    
    **note: not reommended as variables with same name can appear in one or more sections
    
    
    """
    
    config_parser = None
    section = None
    
    def __init__(self, section, config_parser):
        self.section = section
        self.config_parser = config_parser
        
    def __getattr__(self, option):
        
        if self.config_parser.has_option(self.section, option):
            return self.config_parser.get(self.section, option)
        
        raise SettingsError("could not find option '%s' in section '%s'" % (option, self.section))
        
    def __getitem__(self, option):
        
        return self.__getattr__(option)
    
        
class Settings(dict):
    """
    Dictionary-like object which populates from config (.ini, .cfg) file format.
    Allows items to be accessed by:
    
    
    settings = Settings()
    
    settings.section__variable_name
    settings.
    
    Options:
       * **  ** : 
    """    

    config_parser = ConfigParser.ConfigParser()
    config_default = os.path.join(os.path.dirname(__file__),'defaults.ini')

    
    def __init__(self):

        self.config_files = []
        if get_playbook_root():
            self.config_files.append(os.path.join(get_playbook_root(), '.arm'))
        self.config_files.append(os.path.realpath('~/.arm'))

        self.config_parser.readfp(open(self.config_default))        
        self.config_parser.read(self.config_files)
        
        
                
    def get(self, item, default=None):
        if hasattr(self, item):
            return self.__getattr__(item)
        return default
        
    def __getattr__(self, name):
        
        option, section = None, None
        if '.' in name:
            section,option = name.split('.')
            if self.config_parser.has_option(section,option):
                return self.config_parser.get(section,option)
        elif '__' in name:
            section,option = name.split('__')
        
        if section and option and self.config_parser.has_option(section,option):
            return self.config_parser.get(section, option)

        if name in self.config_parser.sections():
            return SettingsHelper(name, self.config_parser)
        
        all_options = [self.config_parser.items(section) for section in self.config_parser.sections()]
        all_options = dict(itertools.chain.from_iterable(all_options))
        if name in all_options.keys():
            return all_options.get(name)
            
        raise SettingsError("could not find '%s'" % name)
    
    def __getitem__(self,name):
        
        if '.' in name or '__' in name:
            return self.__getattr__(name)
        
        if name in self.config_parser.sections():
            return SettingsHelper(name, self.config_parser)
    
settings = Settings()
            
        
        
