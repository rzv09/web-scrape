"""
Graphes information on a csv
This one specifically graphes a car's mileage and price
author: Aaron Oshiro
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sbn
import pandas as pd


def graph_csv(file):
    sbn.set()
    csv_file = pd.read_csv(file)
    mileage = csv_file.Mileage.tolist()
    price = csv_file.Price.tolist()
    double_prices = []
    for thing in price:
        thing = thing.replace('$', '')
        thing = thing.replace(',', '')
        double_prices.append(float(thing))
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.yticks(np.arange(0, 50000, 5000))
    plt.xticks(np.arange(0, 360000, 50000))
    plt.title("Price over Mileage")
    plt.plot(mileage, double_prices, color='blue', linestyle='none', linewidth=1, marker='o', markerfacecolor='blue',
             markersize=3)
    plt.show()


def main():
    graph_csv('vehicle_info.csv')


if __name__ == '__main__':
    main()
