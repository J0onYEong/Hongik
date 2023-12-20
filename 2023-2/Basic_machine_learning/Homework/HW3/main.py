import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import pickle

from PIL import Image
from mnist_data import load_mnist

class MNistWithNumpy:

    def __init__(self):
        (self.__x_test, self.__y_test) = load_test_data()
        self.__network = load_trained_network()

    def __forward(self, x, layer_count, unit_count_for_layer):
        net = self.__network

        W1, W2, W3 = net['W1'], net['W2'], net['W3']
        b1, b2, b3 = net['b1'], net['b2'], net['b3']

        modified_w1 = W1[:, :unit_count_for_layer[0]]
        modified_w2 = W2[:unit_count_for_layer[0], :unit_count_for_layer[1]]
        modified_w3 = W3[:unit_count_for_layer[1], :]

        modified_b1 = b1[:unit_count_for_layer[0]]
        modified_b2 = b2[:unit_count_for_layer[1]]
        modified_b3 = b3

        if layer_count == 1:
            w1 = W1[:, :10]
            b1 = b1[:10]
            a1 = np.dot(x, w1) + b1
            y = softmax(a1)
            return y
        elif layer_count == 2:
            a1 = np.dot(x, modified_w1) + modified_b1
            z1 = sigmoid(a1)

            w2 = modified_w2[:, :10]
            b2 = b2[:10]

            a2 = np.dot(z1, modified_w2) + modified_b2
            y = softmax(a2)
            return y

        a1 = np.dot(x, modified_w1) + modified_b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, modified_w2) + modified_b2
        z2 = sigmoid(a2)
        a3 = np.dot(z2, modified_w3) + modified_b3
        y = softmax(a3)
        return y

    def __calculate_accuracy(self,  batch_size, layer_coun=3, unit_count_for_layer=[50, 100, 10]):
        accuracy_count = 0

        x_data = self.__x_test
        y_data = self.__y_test

        for i in range(0, len(x_data), batch_size):
            x_batch = x_data[i:i + batch_size]
            y_batch = self.__forward(x_batch, layer_coun, unit_count_for_layer)
            predicted_labels = np.argmax(y_batch, axis=1)
            accuracy_count += np.sum(predicted_labels == y_data[i:i + batch_size])

        accuracy = float(accuracy_count) / len(x_data)
        return accuracy

    def find_best_fit(self):

        best_batch_size = 1
        best_unit_count = [1, 1, 10]
        best_layer_count = 1
        best_accuracy = 0.0

        for batch_size in range(10, 1001, 30):
            for layer_count in range(1, 4, 1):
                for first_unit_count in range(1, 52, 5):
                    for second_unit_count in range(1, 102, 10):
                        temp_unit_count = [first_unit_count, second_unit_count, 10]
                        temp_accuracy = self.__calculate_accuracy(batch_size, layer_count, temp_unit_count)

                        if temp_accuracy >= best_accuracy:
                            print("update batch_size: ", batch_size)
                            print("update best_layer_count: ", layer_count)
                            print("update unit_count: ", temp_unit_count)
                            print("update 정확도: ", temp_accuracy)
                            best_batch_size = batch_size
                            best_layer_count = layer_count
                            best_unit_count = temp_unit_count
                            best_accuracy = temp_accuracy

        print("최적 batch_size: ", best_batch_size)
        print("최적 best_layer_count: ", best_layer_count)
        print("최적 unit_count: ", best_unit_count)
        print("최고 정확도: ", best_accuracy)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(output_layer_values):
    max_value = np.max(output_layer_values)
    exp_olv = np.exp(output_layer_values - max_value)
    sum_olv = np.sum(exp_olv)
    y = exp_olv / sum_olv

    return y


def load_trained_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def load_test_data():
    (_, _), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


ins = MNistWithNumpy()

ins.find_best_fit()