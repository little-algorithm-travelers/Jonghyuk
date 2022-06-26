# BAEKJOON 11866
# 요세푸스 문제 0
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque(range(1, N + 1))
N_list = []

# for i in range(1, N + 1):
#     queue.append(i)

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())        
    N_list.append(queue.popleft())

print("<", end = "")
print(*N_list, sep = ", ", end = "")
print(">", end = "")