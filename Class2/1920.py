# BAEKJOON 1920
# if i in N_list -> 시간 초과 ->> 이분 탐색으로 풀어야함

N = int(input())
N_list = list(map(int, input().split()))
N_list = sorted(N_list) # 이분 탐색을 위한 정렬

M = int(input())
M_list = list(map(int, input().split()))

for i in M_list: # 5개 숫자 모두 확인
    start, end = 0, N - 1 # [0] ~ [4]
    confirm = False # 숫자가 확인되면 True
    while start <= end: # 이분 탐색 시작
        mid = (start + end) // 2
        if i == N_list[mid]: # 찾을 때
            print(1)
            confirm = True
            break
        elif i > N_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if not confirm:
        print(0)