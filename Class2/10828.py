# BAEKJOON 10828
# 스택
# 시간 초과
import sys

N = int(sys.stdin.readline())
N_list = []
res_list = []
for _ in range(N):
    N_list = sys.stdin.readline().split()

    if N_list[0] == "push":
        res_list.append(int(N_list[1]))

    elif N_list[0] == "top":
        if len(res_list) > 0:
            print(res_list[-1])
        else:
            print(-1)

    elif N_list[0] == "size":
        print(len(res_list))

    elif N_list[0] == "empty":
        if len(res_list) == 0:
            print(1)
        else:
            print(0)

    elif N_list[0] == "pop":
        if len(res_list) > 0:
            print(res_list.pop())
        else:
            print(-1)