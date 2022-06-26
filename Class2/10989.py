# BAEKJOON 10989
# 수 정렬하기
# 정렬

import sys

N = int(sys.stdin.readline())
N_list = [0] * 10001 # 숫자가 0부터 10000까지이므로 10001까지
for _ in range(N):
    a = int(sys.stdin.readline())
    N_list[a] += 1 # 각 숫자에 맞는 위치에 +1

for i in range(10001): # 모든 숫자 확인
    if N_list[i] > 0: # 해당 숫자 개수가 0이 아닐때만 출력
        for _ in range(N_list[i]): # 해당 숫자 개수만큼 출력 
            print(i) 
        