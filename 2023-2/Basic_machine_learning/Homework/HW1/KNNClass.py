import numpy as np
class MyKNNClass:
    def __init__(self, K):
        # 근접 이웃 수
        self.K = K

    def set_train_data(self, features, targets):
        self.X = features
        self.Y = targets

    def __calculate_distance(self, point):
        # X는 4*140벡터이고 point는 4*1벡터입니다.
        # 해당 연산의 결과는 1*140벡터로, point와 X리스트의 모든 점들의 유클리드 거리를 요소로 가지는 리스트입니다.
        return np.sqrt(np.sum((self.X-point)**2, axis=1))

    def obtain_k_nearest_neighbor(self, test_input):
        distances = self.__calculate_distance(test_input)
        # argsort함수는 정렬한 리스트의 요소와 매칭되는 정렬전 배열의 인덱스들의 리스트입니다.
        ordered_index = np.argsort(distances)
        # 가장가까운 k개의 이웃의 분류(class)를 저장하는 리스트
        k_nearest_neighbor = []

        for i in ordered_index[:self.K]:
            # 길이가 가장 가까윤 K개의 요소를 k_nearest_neighbor리스트에 저장한니다.
            # 가중치 연산을 위해 해당 이웃의 품종과 거리를 튜플로 리스트에 저장합니다.
            k_nearest_neighbor.append((self.Y[i], distances[i]))
        return k_nearest_neighbor

    def obtain_majority_vote(self, k_nearest_neighbor):
        # 가장 많은 수가 존재하는 이웃의 class를 선정한다.
        class_dic = {
            0: 0,
            1: 0,
            2: 0
        }
        for result, _ in k_nearest_neighbor:
            class_dic[result] += 1

        # 가장많이 등장한 class의 수를 측정합니다.
        max_count_class = 0
        max_count = 0
        for result, _ in k_nearest_neighbor:
            if max_count < class_dic[result]:
                max_count = class_dic[result]
                max_count_class = result

        return max_count_class

    def weighted_majority_vote(self, k_nearest_neighbor):
        class_dic = {
            0: 0,
            1: 0,
            2: 0
        }

        # "1 / (1+distance)"를 가중치로 더하여 사용합니다.
        for result, distance in k_nearest_neighbor:
            class_dic[result] += 1 / (1+distance)

        max_count_class = 0
        max_count = 0
        for result, _ in k_nearest_neighbor:
            if max_count < class_dic[result]:
                max_count = class_dic[result]
                max_count_class = result

        return max_count_class

# 특징(feature)별 평균과 표준편차 연산을 위한 클래스
class MyScalar:
    def caculate_means_and_stds(self, data):
        # 특성별 평균과 표준편차를 저장
        self.means_of_features = np.mean(data, axis=0)
        self.stds_of_features = np.std(data, axis=0)

    def normalize(self, data):
        # caculate_means_and_stds의 실행이 선행되야합니다.
        # 특징(feature)별로 "(데이터 - 평균) / 표준편차" 로 normalize한 데이터를 반환합니다.
        data_structure = data.shape
        normalized = np.empty(data_structure)
        for row in range(data_structure[0]):  # row 개수만큼 반복
            for col in range(data_structure[1]):  # column 개수만큼 반복
                # x_new = (x - mean) / std
                normalized[row, col] = (data[row, col] - self.means_of_features[col]) / \
                                        self.stds_of_features[col]
        return normalized
