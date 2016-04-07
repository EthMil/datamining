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
    print(len(copy))
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]

# def separateByClass(dataset):
#     separated = {}
#     for i in range(len(dataset)):
#         vector = dataset[i]
#         if (vector[0] not in separated):

filename = 'carRandom1.data'

dataset = parse_input(filename)
splitRatio = 0.67
train, test = splitDataset(dataset, splitRatio)
# print('Split {0} rows into train with \n\n {1} \n\n\n\nand test with {2}').format(len(dataset), train, test)
