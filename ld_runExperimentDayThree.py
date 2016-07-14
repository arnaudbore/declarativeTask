from cursesmenu import *
from cursesmenu.items import *
import sys, os

cwd = os.getcwd()

# '1': Test Matrix A
# '2': Matrix B
# '3': Rest
# '4': Show Config

# Create the menu
menu = CursesMenu("Declarative Task - Day One", 'Subject: ' + sys.argv[1])

dayThreeTestMatrixA = CommandItem(text="Test Matrix A",
                                  command="PYTHONPATH=$PYTHONPATH:{} python src".format(cwd) + os.path.sep + "ld_declarativeTask.py ",
                                  arguments="Day Three - Test Learning, " + sys.argv[1],
                                  menu=menu,
                                  should_exit=False)

dayThreeTestMatrixB = CommandItem(text="Test Matrix B",
                                  command="PYTHONPATH=$PYTHONPATH:{} python src".format(cwd) + os.path.sep + "ld_declarativeTask.py ",
                                  arguments="Day Three - Test Interference, " + sys.argv[1],
                                  menu=menu,
                                  should_exit=False)

dayThreeRest = CommandItem(text='Rest',
                         command="PYTHONPATH=$PYTHONPATH:{} python src".format(cwd) + os.path.sep + "ld_rest.py",
                         menu=menu,
                         should_exit=False)

dayThreeConfig = CommandItem(text='Show config file',
                           command="PYTHONPATH=$PYTHONPATH:{} python src".format(cwd) + os.path.sep + "ld_showConfigFile.py",
                           menu=menu,
                           should_exit=False)

dayThreeRecognition = CommandItem(text="Recognition",
                                  command="PYTHONPATH=$PYTHONPATH:{} python src".format(cwd) + os.path.sep + "ld_recognition.py ",
                                  arguments="Day Three - Recognition, " + sys.argv[1],
                                  menu=menu,
                                  should_exit=False)

menu.append_item(dayThreeTestMatrixA)
if sys.argv[2] == 'True':
    menu.append_item(dayThreeTestMatrixB)

menu.append_item(dayThreeRecognition)

menu.append_item(dayThreeRest)
menu.append_item(dayThreeConfig)

menu.show()
