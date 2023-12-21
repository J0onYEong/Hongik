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
    # 매개변수
    #   - input_size : 입력층의 노드수를 의미한다.
    #   - hidden_layer_count : 은닉층의 개수를 의미한다.
    #   - unit_size_for_each_layer : 각각의 은닉층의 노드수를 의미한다.
    #   - output_size : 출력층의 노드수를 의미한다.
    def __init__(self, input_size, hidden_layer_count, unit_size_for_each_layer, output_size, weight_init_std=0.01):
        self.params = {}
        self.hidden_layer_count = hidden_layer_count

        if hidden_layer_count >= 1:
            self.params['W0'] = weight_init_std * \
                                np.random.randn(input_size, unit_size_for_each_layer[0])
            self.params['B0'] = np.zeros(unit_size_for_each_layer[0])

            last_weight_key = 'W' + str(hidden_layer_count)
            last_bias_key = 'B' + str(hidden_layer_count)

            self.params[last_weight_key] = weight_init_std * \
                                    np.random.randn(unit_size_for_each_layer[hidden_layer_count-1], output_size)
            self.params[last_bias_key] = np.zeros(output_size)

            for index in range(1, hidden_layer_count, 1):
                weight_key = 'W' + str(index)
                bias_key = 'B' + str(index)

                now_unit_count = unit_size_for_each_layer[index]
                prev_unit_count = input_size

                if index > 0:
                    prev_unit_count = unit_size_for_each_layer[index-1]

                self.params[weight_key] = weight_init_std * \
                    np.random.randn(prev_unit_count, now_unit_count)

                self.params[bias_key] = np.zeros(now_unit_count)

    # 매개변수를 바탕으로 생성된 가중치 배열의 차원을 출력한다.
    def print_params(self):

        for index in range(self.hidden_layer_count+1):

            weight_key = 'W' + str(index)
            bias_key = 'B' + str(index)

            print("{}: {}".format(weight_key, self.params[weight_key].shape))
            print("{}: {}".format(bias_key, self.params[bias_key].shape))


    def predict(self, x):

        temp_weight = self.params['W0']
        temp_bias = self.params['B0']
        temp_a = np.dot(x, temp_weight) + temp_bias
        temp_z = sigmoid(temp_a)

        for index in range(1, self.hidden_layer_count+1, 1):
            weight_key = 'W' + str(index)
            bias_key = 'B' + str(index)

            temp_weight = self.params[weight_key]
            temp_bias = self.params[bias_key]

            temp_a = np.dot(temp_z, temp_weight) + temp_bias

            if index != self.hidden_layer_count:
                temp_z = sigmoid(temp_a)
                continue

            temp_z = softmax(temp_a)

        print(temp_z)



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


ins = MNistWithNumpy(5, 2, [10, 20], 10)

ins.print_params()