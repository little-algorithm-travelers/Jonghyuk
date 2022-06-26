# BAEKJOON 10816
# 숫자 카드 2

# 시간초과났음

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

N_dict = {}

for i in N_list:
    if i in N_dict:
        N_dict[i] += 1
    else:
        N_dict[i] = 1

for i in M_list:
    if i in N_dict:
        print(N_dict[i], end = " ")
    else:
        print(0, end = " ")