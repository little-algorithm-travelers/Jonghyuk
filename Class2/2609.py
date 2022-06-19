# BAEKJOON 2609
# 최대공약수와 최소공배수
# 유클리드 호제법

N, M = map(int, input().split())
n, m = N, M
while M != 0:
    N = N % M
    N, M = M, N

print(N)

print((n * m) // N)