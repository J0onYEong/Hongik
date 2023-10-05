import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.datasets import load_iris
from KNNClass import MyScalar, MyKNNClass


# k값과 class를 산출하는 방법에 따라 결과를 출력하는 함수
def compare_test_results_with(k, isMajorityVote):
    #.1 knn객체 생성 & k값설정
    knnInstance = MyKNNClass(k)
    #.2 학습데이터, 결과 전달
    knnInstance.set_train_data(iris_train_inputs_normalized, iris_train_results)
    #.3 가장가까운 거리의 k개의 이웃 산출
    for index in range(len(iris_test_inputs_normalized)):
        k_nearest_neighbor = knnInstance.obtain_k_nearest_neighbor(iris_test_inputs_normalized[index])
        #.4 선별방식에 따라 분류
        computed_class = knnInstance.obtain_majority_vote(k_nearest_neighbor) \
            if isMajorityVote \
            else knnInstance.weighted_majority_vote(k_nearest_neighbor)
        true_class = iris_test_results[index]

        print("Test Data Index: {} Compuited Class: {}, True class: {}"
              .format(index, iris_class_names[computed_class], iris_class_names[true_class]))

# iris 데이터 로드
iris_dataset = load_iris()

# iris의 4가지 특성이름, 분류결과명
iris_feature_names = iris_dataset['feature_names']

print(iris_feature_names)

iris_class_names = iris_dataset['target_names']

print(iris_class_names)

# test, train분리전 인풋, 결과 데이터
iris_feature_inputs = np.array(iris_dataset['data'])
iris_class_results = np.array(iris_dataset['target'])

# 차례대로 학습데이터, 학습데이터결과, 테스트데이터, 테스트데이터결과
iris_train_inputs = []
iris_train_results = []
iris_test_inputs = []
iris_test_results = []

# 데이터 전처리, train, test데이터 분리
for index in range(len(iris_feature_inputs)):
    # 매 15번째 데이터는 test
    if index % 15 == 0:
        iris_test_inputs.append(iris_feature_inputs[index])
        iris_test_results.append(iris_class_results[index])
        continue
    # 나머지는 train
    iris_train_inputs.append(iris_feature_inputs[index])
    iris_train_results.append(iris_class_results[index])

iris_train_inputs = np.array(iris_train_inputs)
iris_train_results = np.array(iris_train_results)
iris_test_inputs = np.array(iris_test_inputs)
iris_test_results = np.array(iris_test_results)

# 데이터 전처리, Normalize
train_scalar = MyScalar()
train_scalar.caculate_means_and_stds(iris_train_inputs)
iris_train_inputs_normalized = train_scalar.normalize(iris_train_inputs)

test_scalar = MyScalar()
test_scalar.caculate_means_and_stds(iris_test_inputs)
iris_test_inputs_normalized = test_scalar.normalize(iris_test_inputs)

# matplotlib을 활용한 시각데이터
# 4가지 특정중 3가지만 사용하여 표시하였음
classes = [[],[],[]]

for index in range(len(iris_train_inputs_normalized)):
    classes[iris_train_results[index]].append(iris_train_inputs_normalized[index])

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
colorList = ['Greens', 'winter', 'Reds']

for index in range(len(classes)):
    xs = np.array(classes[index])[:,0]
    ys = np.array(classes[index])[:,1]
    zs = np.array(classes[index])[:,2]
    cmin, cmax = 0, 2
    color = np.array([(cmax - cmin) * np.random.random_sample() + cmin for i in range(len(classes[index]))])
    ax.scatter(xs, ys, zs, c=color, marker='o', s=20, cmap=colorList[index])

plt.show()

# 테스트할 k값 리스트
k_list = [3, 5, 7]

print("\n\n----------obtain_majority_vote매서드 사용----------\n")
for k in k_list:
    print("\nk값이 {}일 때의 결과입니다.\n".format(k))
    compare_test_results_with(k, True)

print("\n\n----------weighted_majority_vote매서드 사용----------\n")
for k in k_list:
    print("\nk값이 {}일 때의 결과입니다.\n".format(k))
    compare_test_results_with(k, False)



















