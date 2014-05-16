




def menu(menu_items):

    numbers = range(1,len(menu_items)+1)
    selectors = ['%s' % n for n in numbers]

    def _unique_selector(name):
        for letter in name.lower():
            if letter not in selectors:
                selectors.append(letter)
                new_name = name.lower().replace(letter,'[%s]' % letter.upper(),1)
                return letter, new_name
            
        raise Exception("could not find unique selector")
    
    def _display_options():
        for i in numbers:
            key,new_name = _unique_selector(menu_items[i-1]['name'])
            menu_items[i-1]['key'] = key
            menu_items[i-1]['number'] = '%s' % (i)
            description = menu_items[i-1].get('description','')
            print "(%s)\t%s\t%s" % (i, new_name, description)
    _display_options()


    keys = dict([ (item['key'], item) for item in menu_items ])
    numbers = dict([ (item['number'], item) for item in menu_items ])
    names = dict([ (item['name'].lower(), item) for item in menu_items ])
        
    def _selection():           
        choice = raw_input(" please select >> ")
    
    
        if choice.lower() in keys:
            print keys[choice.lower()]['description']
        elif choice.lower() in numbers:
            print numbers[choice.lower()]['description']
        elif choice.lower() in names:
            print names[choice.lower()]['description']
        else:
            print "selection not valid"
            return _selection()

    _selection()
        