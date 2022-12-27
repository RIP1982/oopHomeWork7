import csv


def readerFromCsv(name):
    with open(name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quoting=csv.QUOTE_ALL)
        employee_data = list()
        for row in reader:
            employee_data.append(row)
        csvfile.close()
    return employee_data
