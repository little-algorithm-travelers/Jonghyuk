# BAEKJOON 10866
# 데큐

from collections import deque
import sys

N = int(sys.stdin.readline())
N_list = []
res_list = deque()
for _ in range(N):
    N_list = sys.stdin.readline().split()
    com = N_list[0]

    if com == "push_front":
        res_list.appendleft(N_list[1])

    elif com == "push_back":
        res_list.append(N_list[1])

    elif com == "pop_front":
        if len(res_list) > 0:
            print(res_list.popleft())
        else:
            print(-1)
    
    elif com == "pop_back":
        if len(res_list) > 0:
            print(res_list.pop())
        else:
            print(-1)
    
    elif com == "size":
        print(len(res_list))
    
    elif com == "empty":
        if len(res_list) > 0:
            print(0)
        else:
            print(1)
    
    elif com == "front":
        if len(res_list) > 0:
            print(res_list[0])
        else:
            print(-1)
    
    elif com == "back":
        if len(res_list) > 0:
            print(res_list[-1])
        else:
            print(-1)