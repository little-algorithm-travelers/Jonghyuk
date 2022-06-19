# BAEKJOON 2164
# 카드2
# queue, deque 사용

from collections import deque
N = int(input())
N_list = []

for i in range(1, N + 1):
    N_list.append(i)

N_list = deque(N_list)

while len(N_list) != 1:
    N_list.popleft()
    N_list.rotate(-1)

print(N_list[0])   

''' 시간초과
N = int(input())
N_list = []

for i in range(1, N + 1):
    N_list.append(i)

while len(N_list) != 1:
    N_list.pop(0)
    a = N_list.pop(0)
    N_list.append(a)

print(N_list[0])    
'''