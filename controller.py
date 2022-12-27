import writeToCsv
from employees import Employees
import readFromCsv


def start_button():
    constant_number = input("Scanner your multipass: ")
    lst = readFromCsv.readerFromCsv('data.csv')
    flag = False
    for i in range(len(lst)):
        lst_new = lst[i]
        if lst_new[0] == constant_number:
            flag = True
            employee = Employees(lst_new[0], lst_new[1], lst_new[2], lst_new[3], lst_new[4])
            print(employee)
            writeToCsv.writerToCsv("gate5.csv", lst[i])
    if flag == False:
        print("Employee not found!")
