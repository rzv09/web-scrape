"""
file: data_preprocessing.py
description: this file preprocesses the data so it can be fed to a nn
author: Raman Zatsarenko rzv090701@gmail.com
"""

import csv
import numpy

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


def normalize_data(data):
    """
    assuming the list contains valid data that can be converted from str to int
    convert the python list to numpy array and normalize the data
    :param data: python list of valid str values
    :return: numpy array of normalized values
    """
    normalized_data = numpy.empty([], float)

    for val in data:
        int_val = int(val[1:])/10000
        numpy.append(normalized_data, int_val)
    return normalized_data

def main():
    filename = 'vehicle_info.csv'
    prices = read_csv(filename)
    print(prices)
    print(len(prices))
    normalized_data = normalize_data(prices)
    print(normalized_data)


if __name__ == '__main__':
    main()