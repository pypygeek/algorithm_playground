# 세 정수의 최댓값 구하기

# 스위트(Suitre) : 같은 블럭안의 처리 코드를 스위트(suite)라고 부른다.

def max3(a, b, c):
    """a, b, c의 최댁밧을 구하여 반환"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')
print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')