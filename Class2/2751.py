# BAEKJOON 2751
# 수 정렬하기 2
import sys
N = int(input())
N_list = []
for _ in range(N):
    N_list.append(int(sys.stdin.readline()))
N_list.sort()
for i in N_list:
    print(i)