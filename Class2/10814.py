# BAEKJOON 10814
# 나이순 정렬
# 정렬

N = int(input())
N_list = []
for _ in range(N):
    a, b = input().split()
    N_list.append((int(a), b))
    
N_list.sort(key=lambda A:A[0])

for i in range(N):
    print(N_list[i][0], N_list[i][1])