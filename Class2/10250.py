# BAEKJOON 10250
# ACM호텔
# 수학, 구현, 사칙연산
# 딱 나눠 떨어질때 예외처리를 못했음

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    num   = N // H + 1
    if N % H == 0:
        floor = H
        num   = N // H

    print(floor * 100 + num) 