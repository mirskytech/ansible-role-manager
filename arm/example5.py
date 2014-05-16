from arm.prompt import query_options, query_yes_no
from colorama import Fore, Back, Style


#import logging

#logger = logging.getLogger('arm')    

#logger.info('my arm message')
#logger.warning('my arm warning')


my_menu = [
    { 'id':'id1',
      'name':'Update',
      'description':'this is choice 1',
      'callback':lambda a: "called back: %s" % a
    },
    { 'id':'id2',
      'name':'Upgrade',
      'description':'this is choice 2',
      'callback':None
    },
    {
    'id':'id3',
    'name':'Quit',
    'description':'this is choice 3'
    }
]

print query_options(my_menu, question="action unclear\nwhich would you like to do", default='id1')

print query_yes_no('Ask these questions?',default='y')