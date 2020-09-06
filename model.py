"""
file: model.py
description: this file contains implementation of a prediction model
based on linear regression algorithm using tensorflow
author: Raman Zatsarenko rzv090701@gmail.com
"""

from tensorflow.keras import models
from tensorflow.keras import layers
import numpy as np
import data_preprocessing


def build_model(train_data):
    """
    builds a small neural network with two hidden layers,
    each with 64 units
    :param train_data: train data, numpy array
    :return: prediction model
    """
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model


def k_fold_validation(train_data, test_data, train_targets):
    k = 4
    num_val_samples = len(train_data) // k
    num_epochs = 100
    all_scores = []

    for i in range(k):
        print("processing fold # ", i)
        val_data = train_data[i * num_val_samples : (i+1) * num_val_samples]
        val_targets = train_targets[i * num_val_samples : (i+1) * num_val_samples]

        partial_train_data = np.concatenate(
            [train_data[:i * num_val_samples],
             train_data[(i+1) * num_val_samples:]],
            axis=0)
        partial_train_targets = np.concatenate(
            [train_targets[:i * num_val_samples],
             train_targets[(i+1) * num_val_samples:]],
            axis=0
        )

        model = build_model(train_data)
        model.fit(partial_train_data, partial_train_targets, epochs=num_epochs, batch_size=1, verbose=1)
        # validation mean square error, validation mean abs error
        val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=1)
        all_scores.append(val_mae)

    return all_scores

def main():
    # data preprocessing
    filename = 'vehicle_info.csv'
    vehicles, target_prices = data_preprocessing.read_csv(filename)
    train_data, test_data = data_preprocessing.normalize_data(vehicles)
    train_targets, test_targets = data_preprocessing.partition_targets(target_prices)

    scores = k_fold_validation(train_data, test_data, train_targets)
    print(scores)

if __name__ == '__main__':
    main()