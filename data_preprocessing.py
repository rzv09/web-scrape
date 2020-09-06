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
    prices = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            current_vehicle_features = []
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
            else:
                # get year of manufacturing
                try:
                    year_of_man = int(row[1]) / 1000
                    # current_vehicle.append(int(row[1]))
                    # current_vehicle.append(int(row[2][1:]))
                    # current_vehicle.append(int(row[3]))
                except ValueError:
                    year_of_man = 0
                finally:
                    current_vehicle_features.append(year_of_man)
                # get price
                try:
                    price = int(row[2][1:]) / 1000
                except ValueError:
                    price = 0
                # get mileage
                try:
                    mileage = int(row[3]) / 10000
                except ValueError:
                    mileage = 0
                finally:
                    current_vehicle_features.append(mileage)

                # append to all vehicles
                vehicles.append(current_vehicle_features)
                prices.append(price)
            line_count += 1
    return vehicles, prices


def normalize_data(data):
    """
    assuming the list contains valid data that can be converted from str to int
    convert the python list to numpy array and normalize the data
    partitions the data into train and test arrays
    :param data: python list of valid str values
    :return: numpy array of normalized values
    """

    # 2/3 of all data is used for training
    train_data = numpy.array(data[:int(len(data)*0.66)], dtype='float64')
    # 1/3 of all data is used for testing
    test_data = numpy.array(data[int(len(data)*0.66):], dtype='float64')

    # use values computed on train data to normalize train and test data
    mean = train_data.mean(axis=0)
    train_data -= mean
    std = train_data.std(axis=0)
    train_data /= std

    test_data -= mean
    test_data /= std

    return train_data, test_data


def partition_targets(target_prices):
    """
    partitions the prices data into test_targets and train_targets
    :param target_prices: a list of target prices
    :return: train_targets, test_targets
    """
    train_targets = numpy.array(target_prices[:int(len(target_prices)*0.66)], dtype='float64')
    test_targets = numpy.array(target_prices[int(len(target_prices)*0.66):], dtype='float64')
    print(train_targets.shape)
    print(test_targets.shape)
    return train_targets, test_targets


def main():
    filename = 'vehicle_info.csv'
    vehicles, target_prices = read_csv(filename)
    print(vehicles)
    print(len(vehicles))
    train_data, test_data = normalize_data(vehicles)
    print(train_data[0])
    print(test_data.shape)
    partition_targets(target_prices)


if __name__ == '__main__':
    main()