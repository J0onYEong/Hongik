
def input_string():
    s1 = input("첫번째 문자열을 입력하시오 : ")
    s2 = input("두번째 문자열을 입력하시오 : ")
    return s1, s2

def print_concated_str(p1, p2):
    print("합쳐진 문자열 : {}".format(p1 + ' ' + p2))

def input_floats():
    l1, l2 = map(float, input("실수 2개를 입력하시오 : ").split())
    return l1, l2;

def extraction(f1, f2):
    if f1 > f2:
        return f1 - f2
    else:
        return f2 - f1

str1, str2 = input_string()

print_concated_str(str1, str2)

f1, f2 = input_floats()

print(f"두 실수의 차 : {extraction(f1, f2)}")

