from cursesmenu import *
from cursesmenu.items import *
import sys, os

cwd = os.getcwd()

# '1': Test Matrix A
# '2': Matrix B
# '3': Rest
# '4': Show Config

# Create the menu
menu = CursesMenu("Declarative Task - Day Two", 'Subject: ' + sys.argv[1])

dayTwoTestMatrixA = CommandItem(text="Test Matrix A",
                                command="PYTHONPATH=$PYTHONPATH:{} python src".format(cwd) + os.path.sep + "ld_declarativeTask.py ",
                                arguments="Day Two - Test, " + sys.argv[1],
                                menu=menu,
                                should_exit=False)

dayTwoInterference = CommandItem(text="Matrix B",
                                 command="PYTHONPATH=$PYTHONPATH:{} python src".format(cwd) + os.path.sep + "ld_declarativeTask.py ",
                                 arguments="Day Two - Interference, " + sys.argv[1],
                                 menu=menu,
                                 should_exit=False)

dayTwoRest = CommandItem(text='Rest',
                         command="PYTHONPATH=$PYTHONPATH:{} python src".format(cwd) + os.path.sep + "ld_rest.py",
                         menu=menu,
                         should_exit=False)

dayTwoConfig = CommandItem(text='Show config file',
                           command="PYTHONPATH=$PYTHONPATH:{} python src".format(cwd) + os.path.sep + "ld_showConfigFile.py",
                           menu=menu,
                           should_exit=False)

menu.append_item(dayTwoTestMatrixA)
if sys.argv[2] == 'True':
    menu.append_item(dayTwoInterference)

menu.append_item(dayTwoRest)
menu.append_item(dayTwoConfig)

menu.show()
