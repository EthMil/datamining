def parse_input():
    import csv
    with open('data.csv', 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)

f = parse_input()
print(f)
