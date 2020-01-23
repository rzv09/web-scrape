"""
this file produces graphics for data from vehicle_info.csv
also this thing doesn't work
!SLICE PRICES AND CAST TO AN INT INSTEAD OF STR!
author: Raman Zatsarenko
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_csv = pd.read_csv('vehicle_info.csv')
print(data_csv.info())


def plot_linear(data):
    """
    i don't know what happened here please for the love of god don't run it
    :param data:
    :return:
    """
    x = data[" Year"]
    y = data[" Price"]

    plt.scatter(y, x, marker="o", color='r')
    plt.show()

def plot_sns(data):
    cars = sns.load_dataset(data)
    #sns.scatterplot(x=" Year", y=" Price", data=cars)


def main():
    plot_linear(data_csv)
    # plot_sns(data_csv)


if __name__ == '__main__':
   main()
   # pass

#print(data_csv[" Year"])