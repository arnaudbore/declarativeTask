import sys
import os
import numpy as np
from expyriment.misc import data_preprocessing
from ld_utils import extractCorrectAnswers
from ld_utils import correctCards, wrongCards
subjectFolder = sys.argv[1]
subjectFolder = os.getcwd() + os.path.sep  + subjectFolder + os.path.sep + 'Data' + os.path.sep

verbose = True

allFiles = os.listdir(subjectFolder)

declarativeFiles = []

for iFile in allFiles:
    if 'ld_recognition' in iFile:
        recognitionFile = iFile
    elif 'ld_declarativeTask' in iFile:
        declarativeFiles.append(iFile)


class Days(object):

    def __init__(self):
        self.header = ''
        self.ifile = ''
        self.data = []
        self.correctCards = correctCards()
        self.wrongCards = wrongCards()
        self.matrix = []

isInterference = False
dayOneTestLearning = Days()
dayTwoTestLearning = Days()
dayThreeTestLearning = Days()
dayTwoTestInterference = Days()
dayThreeTestInterference = Days()
dayThreeRecognition = Days()

testFiles = []

for iFile in allFiles:
    header = data_preprocessing.read_datafile(subjectFolder + iFile, only_header_and_variable_names=True)
    header = header[3].split('\n#e ')

    for field in header:
        #if "DayOne-TestLearning" in field and "Experiment" in field:
        #    print 'DayOne-TestLearning'
        #    dayOneTestLearning.header = header
        #    dayOneTestLearning.ifile = iFile
        #    dayOneTestLearning.data, dayOneTestLearning.correctCards, dayOneTestLearning.wrongCards, dayOneTestLearning.matrix = extractCorrectAnswers(subjectFolder, iFile)
        #    break
        #elif "DayTwo-TestLearning" in field and "Experiment" in field:
        #    print 'DayTwo-TestLearning'
        #    dayTwoTestLearning.header = header
        #    dayTwoTestLearning.ifile = iFile
        #    dayTwoTestLearning.data, dayTwoTestLearning.correctCards, dayTwoTestLearning.wrongCards, dayTwoTestLearning.matrix = extractCorrectAnswers(subjectFolder, iFile)
        #    break
        #elif "DayThree-TestLearning" in field and "Experiment" in field:
        #    print 'DayThree-TestLearning'
        #    dayThreeTestLearning.header = header
        #    dayThreeTestLearning.ifile = iFile
        #    dayThreeTestLearning.data, dayThreeTestLearning.correctCards, dayThreeTestLearning.wrongCards, dayThreeTestLearning.matrix = extractCorrectAnswers(subjectFolder, iFile)
        #    break
        if "DayTwo-TestInterference" in field and "Experiment" in field:
            print 'DayTwo-TestInterference'
            dayTwoTestInterference.header = header
            dayTwoTestInterference.ifile = iFile
            isInterference = True
            dayTwoTestInterference.data, dayTwoTestInterference.correctCards, dayTwoTestInterference.wrongCards, dayTwoTestInterference.matrix = extractCorrectAnswers(subjectFolder, iFile)
            break
        #elif "DayThree-TestInterference" in field and "Experiment" in field:
        #    print 'DayThree-TestInterference'
        #    dayThreeTestInterference.header = header
        #    dayThreeTestInterference.ifile = iFile
        #    dayThreeTestInterference.data, dayThreeTestInterference.correctCards, dayThreeTestInterference.wrongCards, dayThreeTestInterference.matrix = extractCorrectAnswers(subjectFolder, iFile)
        #    break
        #elif "recognition" in iFile:
        #    print 'recognition'
        #    dayThreeRecognition.header = header
        #    dayThreeRecognition.ifile = iFile
        #    break

unionConsolidation =  set(dayOneTestLearning.correctCards.name).intersection(dayTwoTestLearning.correctCards.name)
unionReConsolidation = set(dayTwoTestLearning.correctCards.name).intersection(dayThreeTestLearning.correctCards.name)

newConsolidation = set(dayTwoTestLearning.correctCards.name).difference(dayOneTestLearning.correctCards.name)
newReConsolidation = set(dayThreeTestLearning.correctCards.name).difference(dayTwoTestLearning.correctCards.name)

if verbose:
    print '##################################'
    print 'Day One - Test'
    print str(len(dayOneTestLearning.correctCards.name)) + ' Images learned'
    print str(len(dayOneTestLearning.correctCards.animals)) + '/9 animals learned'
    print str(len(dayOneTestLearning.correctCards.clothes)) + '/9 clothes learned'
    print str(len(dayOneTestLearning.correctCards.vehicules)) + '/9 vehicules learned'
    print str(len(dayOneTestLearning.correctCards.fruits)) + '/9 fruits learned'

    print '##################################'
    print 'Day Two - Test'
    print str(len(dayTwoTestLearning.correctCards.name)) + ' Images recovered'
    print str(len(dayTwoTestLearning.correctCards.animals)) + '/9 animals recovered'
    print str(len(dayTwoTestLearning.correctCards.clothes)) + '/9 clothes recovered'
    print str(len(dayTwoTestLearning.correctCards.vehicules)) + '/9 vehicules recovered'
    print str(len(dayTwoTestLearning.correctCards.fruits)) + '/9 fruits recovered'

    print '##################################'
    print 'Day Three - Test'
    print str(len(dayThreeTestLearning.correctCards.name)) + ' Images recovered'
    print str(len(dayThreeTestLearning.correctCards.animals)) + '/9 animals recovered'
    print str(len(dayThreeTestLearning.correctCards.clothes)) + '/9 clothes recovered'
    print str(len(dayThreeTestLearning.correctCards.vehicules)) + '/9 vehicules recovered'
    print str(len(dayThreeTestLearning.correctCards.fruits)) + '/9 fruits recovered'

    print '##################################'
    print 'Summary Consolidation'
    print str(len(unionConsolidation)) + ' Images consolidated'

    if not newConsolidation:
        print '0 new Images consolidated'
    else:
        print str(len(newConsolidation)) + ' new Images consolidated'

    print '##################################'
    print 'Summary Reconsolidation'
    print str(len(unionReConsolidation)) + ' Images reconsolidated'
    if not newReConsolidation:
        print '0 new Images reconsolidated'
    else:
        print str(len(newReConsolidation)) + ' new Images reconsolidated'


    if isInterference:
        print '##################################'
        print 'Day Two - Interference'
        print str(len(dayTwoTestInterference.correctCards.name)) + ' Images recovered'
        print str(len(dayTwoTestInterference.correctCards.animals)) + '/9 animals recovered'
        print str(len(dayTwoTestInterference.correctCards.clothes)) + '/9 clothes recovered'
        print str(len(dayTwoTestInterference.correctCards.vehicules)) + '/9 vehicules recovered'
        print str(len(dayTwoTestInterference.correctCards.fruits)) + '/9 fruits recovered'

        print '##################################'
        print 'Day Three - Interference'
        print str(len(dayThreeTestInterference.correctCards.name)) + ' Images recovered'
        print str(len(dayThreeTestInterference.correctCards.animals)) + '/9 animals recovered'
        print str(len(dayThreeTestInterference.correctCards.clothes)) + '/9 clothes recovered'
        print str(len(dayThreeTestInterference.correctCards.vehicules)) + '/9 vehicules recovered'
        print str(len(dayThreeTestInterference.correctCards.fruits)) + '/9 fruits recovered'

        unionConsolidationInterference =  set(dayTwoTestInterference.correctCards.name).intersection(dayThreeTestInterference.correctCards.name)
        newConsolidationInterference = set(dayThreeTestInterference.correctCards.name).difference(dayTwoTestInterference.correctCards.name)

        print '##################################'
        print 'Summary Consolidation Interference'
        print str(len(unionConsolidationInterference)) + ' Images consolidated'
        if not newReConsolidation:
            print '0 new Images reconsolidated'
        else:
            print str(len(newConsolidationInterference)) + ' new Images consolidated'





















