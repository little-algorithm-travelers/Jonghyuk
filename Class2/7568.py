# BAEKJOON 7568
# 덩치
# 구현, 브루트포스 알고리즘

N = int(input())
N_list = []
res_list = []
for _ in range(N):
    x, y = map(int, input().split())
    N_list.append((x, y))

for i in range(len(N_list)): # N_list 길이만큼 반복
    cnt = 0
    for j in range(len(N_list)): # N_list 길이만큼 반복
        if N_list[i][0] < N_list[j][0] and N_list[i][1] < N_list[j][1]:
            cnt += 1
    res_list.append(cnt + 1) # 1위부터 시작이기 때문에 +1

for i in res_list:
    print(i, end=" ")