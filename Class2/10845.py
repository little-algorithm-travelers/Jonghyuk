# BAEKJOON 10845
# 큐
# 자료 구조, 큐
import sys

N = int(sys.stdin.readline())
N_list = []
res_list = []
for _ in range(N):
    N_list = sys.stdin.readline().split()
    com = N_list[0]

    if com == "push":
        res_list.insert(0, N_list[1])

    elif com == "pop":
        if len(res_list) > 0:
            print(res_list.pop(-1))
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
            print(res_list[-1])
        else:
            print(-1)
    
    elif com == "back":
        if len(res_list) > 0:
            print(res_list[0])
        else:
            print(-1)