# BAEKJOON 10871

N, X = map(int, input().split())
num_list = list(map(int, input().split()))

for i in range(N):
    if num_list[i] < X:
        print(num_list[i], end = " ")