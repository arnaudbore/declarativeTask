from cursesmenu import *
from cursesmenu.items import *
import sys
import os

# '1': Example
# '2': Matrix A
# '3': Rest
# '4': Show Config

# Create the menu
menu = CursesMenu("Declarative Task - Day One", 'Subject: ' + sys.argv[1])

dayOneExample = CommandItem(text='Example',
                            command="python src" + os.path.sep + "ld_example.py",
                            arguments='Example, ' + sys.argv[1],
                            menu=menu,
                            should_exit=False)

dayOneLearning = CommandItem(text="Matrix A",
                             command="python src" + os.path.sep + "ld_declarativeTask.py ",
                             arguments="Day One - Learning, " + sys.argv[1],
                             menu=menu,
                             should_exit=False)

dayOneRest = CommandItem(text='Rest',
                         command="python src" + os.path.sep + "ld_rest.py",
                         menu=menu,
                         should_exit=False)

dayOneConfig = CommandItem(text='Show config file',
                           command="python src" + os.path.sep + "ld_showConfigFile.py",
                           menu=menu,
                           should_exit=False)

menu.append_item(dayOneExample)
menu.append_item(dayOneLearning)
menu.append_item(dayOneRest)
menu.append_item(dayOneConfig)

menu.show()
