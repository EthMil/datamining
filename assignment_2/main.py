import csv

def parse_input(file_name):
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list

raw_input("input the name of the csv file you want to parse: ")
f = parse_input()
print(f)
