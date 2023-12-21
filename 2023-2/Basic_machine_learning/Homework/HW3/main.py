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

    # input_size: 테스트 케이스 하나의 입력 노드의 개수를 의미한다.
    def __init__(self, input_size, hidden_layer_count, unit_size_for_each_layer, output_size, weight_init_std=0.01):
        self.params = {}
        self.hidden_layer_count = hidden_layer_count

        if hidden_layer_count >= 1:
            self.params['W0'] = weight_init_std * \
                                np.random.randn(input_size, unit_size_for_each_layer[0])

            last_key = 'W' + str(hidden_layer_count)

            self.params[last_key] = weight_init_std * \
                                    np.random.randn(unit_size_for_each_layer[hidden_layer_count-1], output_size)

            for index in range(1, hidden_layer_count, 1):
                key = 'W' + str(index)

                now_unit_count = unit_size_for_each_layer[index]
                prev_unit_count = input_size

                if index > 0:
                    prev_unit_count = unit_size_for_each_layer[index-1]

                self.params[key] = weight_init_std * \
                    np.random.randn(prev_unit_count, now_unit_count)

    def print_params(self):

        for index in range(self.hidden_layer_count+1):

            key = 'W' + str(index)

            print("{}: {}".format(key, self.params[key].shape))


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


ins = MNistWithNumpy(784, 2, [10, 20], 10)

ins.print_params()