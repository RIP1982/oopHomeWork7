import csv
import os.path
from datetime import datetime
import readFromCsv


def writerToCsv(name, lst):
    lst1 = readFromCsv.readerFromCsv(name)
    if os.path.getsize(name) == 0:
        with open(name, 'w', encoding='UTF8', newline='') as csvfile:
            current_datetime = datetime.now()
            lst.append(current_datetime)
            writer = csv.writer(csvfile)
            writer.writerow(lst)
    else:
        with open(name, 'w', encoding='UTF8', newline='') as csvfile:
            current_datetime = datetime.now()
            lst.append(current_datetime)
            lst1.append(lst)
            writer = csv.writer(csvfile)
            for i in range(len(lst1)):
                writer.writerow(lst1[i])
    csvfile.close()


