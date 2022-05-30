import csv

def read(file_name):
    data = []
    with open(file_name, 'r') as input_file:
        csv_reader = csv.reader(input_file)

        for line in csv_reader:
            data.append(list(line))
    return data
