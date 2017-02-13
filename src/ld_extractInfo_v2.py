import sys
import ast

from config import dataFolder
from expyriment.misc import data_preprocessing

import numpy as np

agg = data_preprocessing.Aggregator(data_folder=dataFolder,
                                    file_name=sys.argv[1])

print 'Variable computed: '
data = {}
for variable in agg.variables:
    data[variable] = agg.get_variable_data(variable)

indexBlocks = np.unique(data['NBlock'])

for block in indexBlocks:
    print 'Block {}'.format(block)
    correctAnswers = np.logical_and(data['Picture']==data['Answers'], data['NBlock']==block)
    wrongAnswers = np.logical_and(data['Picture']!=data['Answers'], data['NBlock']==block)
    correctRT = [int(i) for i in data['RT'][correctAnswers]]
    print 'Correct answers: {}'.format(len(correctRT))
    print 'Mean correct RT: {} ms'.format(np.mean(correctRT))


# Read Header
header = data_preprocessing.read_datafile(dataFolder + sys.argv[1], only_header_and_variable_names=True)
header = header[3].split('\n#e ')

# Get Matrix
matrixPictures = ast.literal_eval(header[header.index('Positions pictures:')+1].split('\n')[0].split('\n')[0])
print '############################'
print 'Last Block'
print ''
print 'Pictures found:'
print 'Name     Position'
names = []
for idx, val in enumerate(correctAnswers):
    if val:
        print data['Answers'][idx][0], matrixPictures.index(data['Answers'][idx])
        names.append(data['Answers'][idx][0])

aList = [ word for word in names if word[0]=='a']
cList = [ word for word in names if word[0]=='c']
fList = [ word for word in names if word[0]=='f']
vList = [ word for word in names if word[0]=='v']

print '############################'
print 'Category animals: ' + str(len(aList))
print 'Category clothes: ' + str(len(cList))
print 'Category fruits: ' + str(len(fList))
print 'Category vehicules: ' + str(len(vList))


