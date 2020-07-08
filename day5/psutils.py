from csv import reader
from pprint import pprint as pp
import pyexcel


def csv2xlsx(csv, xlsx):
    # print(reader(open(csv), delimiter=':'))
    rows = list(reader(open(csv), delimiter=':'))
    pyexcel.save_as(dest_file_name=xlsx, array=rows)


def read_sheet(filename):
    # pyexcel.get_book
    sheet = pyexcel.get_sheet(file_name=filename)
    for row in sheet:
        print(row)

if __name__ == '__main__':
    # csv2xlsx('passwd.txt', 'passwd.xlsx')
    read_sheet('passwd.xlsx')

    # @ 8: 15 PM IST
