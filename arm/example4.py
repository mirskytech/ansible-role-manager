#!/usr/bin/env python
#!/usr/bin/python
import sys, os

menu_actions = {}
user_menu_items = []


def add_userItem(item):
  returnitem = "item " + item + " created..."
  return returnitem

def show_settings():
  os.system('clear')

  print "\nEdit"
  print "Default Settings"
  print "\nBack"
  choice = raw_input(" >>  ")
  if choice.lower() == 'back':
    main_menu()
  else:
    decision(choice)
  return

def quit():
  raise SystemExit()

def s_edit():
  os.system('clear')
  print "\nCreate"
  print "Modify"
  print "\nBack\n"
  choice = raw_input(" >>  ")
  if choice.lower() == 'back':
    show_settings()
  else:
    decision(choice)
  return

def s_default():
  os.system('clear')
  choice = raw_input("(**All user created menus will be erased**)\nAre you sure? (YES / NO)  or Back\n >>  ")
  if choice.lower() == 'back':
    show_settings()
  elif choice.lower() == 'yes':
    print 'all settings have been set to default'
    del user_menu_items[:]  # removing all items from user menu
    show_settings()
  elif choice.lower() == 'no':
    show_settings()
  return

def e_create():
  go = True
  addeditem = []
  global user_menu_items
  while go:      
    badinput = False
    if badinput == True:
      print "That's not a selection. Please try again..."
    else:
      os.system('clear')
      if addeditem != '':
        z = 0
        for i in addeditem:
          print(addeditem[z])
          z += 1
      if not user_menu_items:
        print
      print "\n**Menu Items**"
      z = 0
      for i in user_menu_items:
        print(user_menu_items[z])
        z += 1
      choice = raw_input("\nCreate New Item? (YES / NO)\n >>  ")
    if choice.lower() == 'yes':
      additem = raw_input("\n\nSpecify Name of New Menu Item: ")
      addeditem.append(add_userItem(additem))
      user_menu_items.append(additem)
    else:
      if choice.lower() == 'no':
        go = False
      else: 
        badinput = True
  s_edit()
  return

def e_modify():
  os.system('clear')
  print "Rename"
  print "Delete"
  print "Move Item"
  print "\nBack\n"
  choice = raw_input("Choose an action: ")
  return choice

def m_rename():
  os.system('clear')
  print "\nBack\n"
  choice = raw_input("Enter a new name: ")
  return choice

def m_delete():
  os.system('clear')
  print "\nBack\n"
  choice = raw_input("Select Menu Item to Delete: ")
  return choice

def m_move():
  os.system('clear')
  print "\nBack\n"
  choice = raw_input("Specify new location: ")
  return choice

def goback():
  os.system('clear')
  print "\nBack\n"
  decision('')
  return

def user_menu():
  z = 0
  for i in user_menu_items:
    print(user_menu_items[z])
    z += 1
  return

def main_menu():
  os.system('clear')
  user_menu()
  print "\nSettings"
  print "Quit"
  choice = raw_input(" >>  ")
  decision(choice)
  return

def decision(decision):
  dec = decision.lower()
  if dec == '':
    menu_actions['main menu']()
  else:  
    try:
      menu_actions[dec]()
    except KeyError:
      print "invalid selection, please try again.\n"
      menu_actions['main menu']()
  return

menu_actions = {
  'main': main_menu,
  'settings': show_settings,
  'quit': quit,
  'edit': s_edit,
  'default': s_default,
  'create': e_create,
  'modify': e_modify,
  'rename': m_rename,
  'delete': m_delete,
  'move': m_move,
  'back' : goback
  }

main_menu()