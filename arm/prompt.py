import colorama




def query_options(menu_items, default=None):

    numbers = range(1,len(menu_items)+1)
    selectors = ['%s' % n for n in numbers]

    def _unique_selector(name):
        for letter in name.lower():
            if letter not in selectors:
                selectors.append(letter)

                coloring = {
                    'style': colorama.Style.BRIGHT,
                    'message': letter.upper(),
                    'reset': colorama.Style.RESET_ALL
                }
                
                c = '%(style)s%(message)s%(reset)s' % coloring
                new_name = name.lower().replace(letter,c,1)
                
                return letter, new_name
            
        raise Exception("could not find unique selector")
    
    def _display_options():
        for i in numbers:
            key,new_name = _unique_selector(menu_items[i-1]['name'])
            menu_items[i-1]['key'] = key
            menu_items[i-1]['number'] = '%s' % (i)
            description = menu_items[i-1].get('description','')
            print "(%s)\t" % i + new_name + "\t%s" % description
    _display_options()

    ids = dict([ (item['id'], item) for item in menu_items ])
    keys = dict([ (item['key'], item) for item in menu_items ])
    numbers = dict([ (item['number'], item) for item in menu_items ])
    names = dict([ (item['name'].lower(), item) for item in menu_items ])
        
    tests = (keys,numbers,names)
        
        
    def _selection():           
        if default:
            choice = raw_input(" please select [%s] >> " % ids[default]['name'])
        else:
            choice = raw_input(" please select >> ")
    
        choice = choice.strip().lower()

        if not choice and default:
            return ids[default]
        
        if not choice:
            print "please make a selection"
            _selection()
    
        for test in tests:
            if choice in test:
                print test[choice]['description']
                return test[choice]

        print "selection not valid"
        return _selection()

    return _selection()


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.
    
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":"yes",   "y":"yes",  "ye":"yes",
             "no":"no",     "n":"no"}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while 1:
        print question + prompt
        choice = raw_input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            print "Please respond with 'yes' or 'no'"
            
