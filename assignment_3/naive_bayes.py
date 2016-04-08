import random
import csv

def parse_input(file_name):
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list

def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]

def separateByClass(dataset):
    separated = {()}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[0] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

filename = 'carRandom.data'

dataset = parse_input(filename)
separated = separateByClass(dataset)
print('Separated instances: {0}').format(separated)
splitRatio = 0.33
train, test = splitDataset(dataset, splitRatio)
print('Split {0} rows into train with \n\n {1} \n\n\n\nand test with {2}').format(len(dataset), train, test)
