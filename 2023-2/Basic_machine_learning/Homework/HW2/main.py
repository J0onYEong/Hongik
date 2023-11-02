# Importing necessary libraries
import math
import sys, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from PIL import Image
from mnist_data import *

sys.path.append(os.pardir)

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()
    # image를 unsigned int로

# KNN class
class KNN():
    def __init__(self, x_train, y_train, x_test, y_test):
        self._x_train = x_train
        self._y_train = y_train
        self._x_test = x_test
        self._y_test = y_test

    def caculate_distacne(self, img1, img2):
        temp = 0.0
        for i in range(len(img1)):
            temp += math.pow(int(img1[i])-int(img2[i]), 2)
        result = math.sqrt(temp)
        return result

    def find_nearest_neighbors(self, target_img, k):
        distance_list = []
        for index in range(len(self._x_train)):
            element = (index, self.caculate_distacne(target_img, self._x_train[index]))
            distance_list.append(element)
        distance_list.sort(key=lambda item: item[1])
        return distance_list[:k]

    def weighted_vote(self, neighbors):
        vote_result = [0 for _ in range(10)]
        for neighbor in neighbors:
            label_train_set = self._y_train[neighbor[0]]
            weighted_value = 1 / neighbor[1]
            vote_result[label_train_set] += weighted_value

        result_label = 0
        label_weight = 0.0
        for lab in range(10):
            if label_weight < vote_result[lab]:
                result_label = lab
                label_weight = vote_result[lab]
        return result_label

    def run(self):
        accuracy_list = []
        k_list = [k for k in range(21, 30, 2)]

        max_accuracy = 0
        optimal_k = 0
        for k in k_list:
            predict_list = []
            print(k)
            for i in range(len(self._x_test)):
                print("test인덱스: {}".format(i))
                target = self._x_test[i]
                neighbors = self.find_nearest_neighbors(target, k=k)
                test_result = self.weighted_vote(neighbors)
                predict_list.append(test_result)
            accuracy=np.mean(self._y_test == np.array(predict_list))
            # 정화도가 가장높은 최적의 k값을 저장
            if accuracy > max_accuracy:
                max_accuracy = accuracy
                optimal_k = k
            accuracy_list.append(accuracy)

        plt.plot(k_list, accuracy_list, 'bs-')
        plt.xlabel = 'k-neighbor'
        plt.ylabel = 'accuracy'
        plt.show()
        print("최적의 k값은 {}".format(optimal_k))

# LogisticRegression Class
class LogisticRegression():
    def __init__(self, lr, epoch, x_train, y_train, x_test, y_test):
        self._lr = lr
        self._epoch = epoch
        self._x_train = x_train.reshape(60000, 28 * 28).astype('float32') / 255.0
        self._y_train = y_train
        self._x_test = x_test.reshape(10000, 28 * 28).astype('float32') / 255.0
        self._y_test = y_test


# load data
x_train, y_train, x_test, y_test = loadData()

# Data Visualization
image = x_train[0]
label = y_train[0]

image = image.reshape(28, 28)

# 1차원 —> 2차원 (28x28)
# img_show(image)  # 이미지 출력(.png)

clf1 = KNN(x_train[:10000], y_train[:10000], x_test[:100], y_test[:100])

knn_start_time = time.time()
clf1.run()
knn_end_time = time.time()
print(f"소요시간: {knn_end_time-knn_start_time:.5f} sec")