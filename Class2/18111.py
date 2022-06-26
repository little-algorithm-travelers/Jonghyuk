# BAEKJOON 18111
# 마인크래프트

import sys

input_a = sys.stdin.readline
N, M, B = map(int, input_a().split())
# N_list = []
time = sys.maxsize
idx = 0

N_list = [list(map(int, input_a().split())) for _ in range(N)]

for target in range(257):
    max_a, min_a = 0, 0

    for i in range(N):
        for j in range(M):
            if N_list[i][j] >= target:
                max_a += N_list[i][j] - target
            else:
                min_a += target - N_list[i][j]
    
    if max_a + B >= min_a:
        if min_a + (max_a * 2) <= time:
            time = min_a + (max_a * 2)
            idx = target
print(time, idx)