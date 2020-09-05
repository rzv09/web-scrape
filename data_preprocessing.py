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

    vehicles = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            current_vehicle = []
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
            else:
                # get year of manufacturing
                try:
                    year_of_man = int(row[1])
                    # current_vehicle.append(int(row[1]))
                    # current_vehicle.append(int(row[2][1:]))
                    # current_vehicle.append(int(row[3]))
                except ValueError:
                    year_of_man = 0
                finally:
                    current_vehicle.append(year_of_man)
                # get price
                try:
                    price = int(row[2][1:])
                except ValueError:
                    price = 0
                finally:
                    current_vehicle.append(price)
                # get mileage
                try:
                    mileage = int(row[3])
                except ValueError:
                    mileage = 0
                finally:
                    current_vehicle.append(mileage)

                # append to all vehicles
                vehicles.append(current_vehicle)
            line_count += 1
    return vehicles


def normalize_data(data):
    """
    assuming the list contains valid data that can be converted from str to int
    convert the python list to numpy array and normalize the data
    partitions the data into train and test arrays
    :param data: python list of valid str values
    :return: numpy array of normalized values
    """
    normalized_data = []

    for val in data:
        int_val = int(val[1:])/10000
        # print(int_val)
        normalized_data.append(int_val)

    # 2/3 of all data is used for training
    train_data = numpy.array(normalized_data[:int(len(normalized_data)*0.66)])
    # 1/3 of all data is used for testing
    test_data = numpy.array(normalized_data[int(len(normalized_data)*0.66):])

    # use values computed on train data to normalize train and test data
    mean = train_data.mean(axis=0)
    train_data -= mean
    std = train_data.std(axis=0)
    train_data /= std

    test_data -= mean
    test_data /= std

    return train_data, test_data

def main():
    filename = 'vehicle_info.csv'
    vehicles = read_csv(filename)
    print(vehicles)
    print(len(vehicles))
    # train_data, test_data = normalize_data(prices)
    # print(len(train_data))
    # print(len(test_data))

if __name__ == '__main__':
    main()