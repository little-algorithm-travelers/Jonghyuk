# BAEKJOON 11050
# 이항 계수
# 수학, 구현, 조합론

N, K = map(int, input().split())

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

num = 1
for i in range(K):
    num *= N - i

num1 = factorial(K)

print(num // num1)