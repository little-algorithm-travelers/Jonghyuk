# BAEKJOON 1929
# 소수 찾기

N, M = map(int, input().split())

def prime_num(a): # 소수 구하는 함수
    if a == 1:
        return False
    for i in range(2, int(a ** 0.5) + 1): # 2 ~ 해당숫자까지 계산 (하지않아도 되고 제곱근까지만 판별하면 됨)
        if a % i == 0:    # 나눠지는 숫자가 있다면 소수가 아니다
            return False
    return True

for j in range(N, M + 1):
    if prime_num(j):
        print(j)

''' 시간 초과
N, M = map(int, input().split())

def prime_num(a): # 소수 구하는 함수
    for i in range(2, a): # 2 ~ 해당숫자까지 계산
        if a % i == 0:    # 나눠지는 숫자가 있다면 소수가 아니다
            return False
    print(a)
    return True

for j in range(N, M):
    prime_num(j)
'''