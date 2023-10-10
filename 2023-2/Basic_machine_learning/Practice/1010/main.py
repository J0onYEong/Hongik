import numpy as np

# Numpy array

"""
    np.random의 random매서드는 [0,1)범위의 난수를 요소로 하는 배열을 생성한다.
    튜플을 전달하면 nxn배열을 생성할 수 있다.
"""
arr1 = np.random.random((3, 4))

# 0th, 2th열을 출력
print(arr1[[0, 2], :])

# 2th열의 1~2요소를 선택
"""
    특정 범위의 요소들을 출력하고 싶다면 ':'을 사용하여 표기하면 된더. a:b일 경우 [a:b)룰 의미한다.
    아래의 1:3 은 1~2인덱스 요소들을 의미한다.
"""
print(arr1[2, 1:3])

# 각 요소에 대해 해당 연산이 적용된 결과를 요소로 가지는 배열을 반환
boolValue = arr1 > 0.5
print(boolValue)

# Numpy Broad Casting
x = np.random.random((3, 4))
y = np.random.random((3, 1))
z = np.random.random((1, 4))
w = np.random.random(3,)
print("x ----")
print(x)
print("y ----")
print(y)
print("z ----")
print(z)
print("w ----")
print(w)

# x+y
"""
   결과를 보면 y배열이 3x1 -> 3x4로 브로드 캐스팅되어 모든 x의 요소에 값이 더해진 것을 확인할 수 있다. 
"""
print("x+y -----\n {}".format(x+y))
# x*z
"""
    1x4인 z배열이 3x4로 로우가 복사되어 같은 위치에 있는 요소들 끼리 곱해진 것을 확인할 수 있다.
"""
print("x*z -----\n {}".format(x*z))
# y+y.T
"""
   y - 3x1 -> 3x3
   yT- 1x3 -> 3x3 
   이렇게 변경후 더해진 것을 확인할 수 있다.  
"""
print("y+yT -----\n {}".format(y+y.T))
# x+w
"""
    오류가 발생한 연산이다.
    행과 열중 하나라도 일치하지 않는 경우 브로드캐스팅이 발생하지 않고 오류가 발생하는 것을 확인할 수 있다.
"""
# print("x+w -----\n {}".format(x+w))
# y+w
print("y+w -----\n {}".format(y+w))


# Efficient skill
arr2 = np.random.random((1000, 1000))
print("제곱전 arr2: \n{}".format(arr2))
arr2 **= 2
print("제곱후 arr2: \n{}".format(arr2))

"""
    2~3열의 요소들에만 5가 더해진 것을 확인할 수 있다.
"""
arr3 = np.random.random((5, 5))
print("덧셈전 arr3\n", arr3)
arr3[2:4, :] += 5
print("덧셈전 arr3\n", arr3)






