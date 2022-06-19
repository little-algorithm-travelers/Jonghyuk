# BAEKJOON 2108
# 통계학
# 최빈값 Counter쓰면 편하지만 안쓰고 해봄
import sys
''' 시간초과!!
N = int(input())
N_list = []
for _ in range(N):
N_list.append(int(input()))
'''
N = int(sys.stdin.readline().strip())
N_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 산술평균
print(round(sum(N_list) / N)) 

# 중앙값
S_list = sorted(N_list) 
print(S_list[int(N / 2)])

# 최빈값
M_list = {} # dict 사용
for i in S_list: # sort된 list 사용
    if i in M_list: # dict에 해당 숫자가 존재하지 않으면 1, 존재하면 + 1
        M_list[i] += 1
    else:
        M_list[i] = 1
max_cnt = max(M_list.values()) # dict의 value중 가장 큰 값 찾기 (최빈값)
tmp_list = [] 
for i in M_list: # dict 사용
    if max_cnt == M_list[i]: # 최빈값이 여러개일 수 있음
        tmp_list.append(i)
tmp_list.sort() # 크기순으로 정렬시키기
if len(tmp_list) > 1: # 최빈값이 여러개라면 두번째로 작은 수 출력, 아니면 최빈값 출력
    print(tmp_list[1])
else:
    print(tmp_list[0])

# 범위
print(S_list[-1] - S_list[0])