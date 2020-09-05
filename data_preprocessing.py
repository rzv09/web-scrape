"""
file: data_preprocessing.py
description: this file preprocesses the data so it can be fed to a nn
author: Raman Zatsarenko rzv090701@gmail.com
"""

import csv

def read_csv(filename):
    """
    appends data from a csv to an array
    the csv if predetermined to have 4 columns,
    prices are col = 2
    :param filename: filename, str
    :return: array of prices (int values)
    """

    prices = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
            else:
                prices.append(row[2])
            line_count += 1

    return prices


def main():
    filename = 'vehicle_info.csv'
    prices = read_csv(filename)
    print(prices)
    print(len(prices))


if __name__ == '__main__':
    main()