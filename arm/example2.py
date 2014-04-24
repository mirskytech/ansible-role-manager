from docopt import docopt
import sys




doc = '''Usage:
  my_program command --option <argument>
  my_program [<optional-argument>]
  my_program --another-option=<with-argument>
  my_program (--either-that-option | <or-this-argument>)
  my_program <repeating-argument> <repeating-argument>...
  
  
  
  
  
  '''


doc = '''
usage: main.py [-h] {init,install,update} ...

positional arguments:
  {init,install,update}
    init                install playbook command
    install             install playbook command
    update              this is a description of the update command
'''


def main():
    result = docopt(doc, sys.argv[1:])
    print result
    
    
main()