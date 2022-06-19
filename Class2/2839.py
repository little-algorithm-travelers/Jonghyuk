# BAEKJOON 2839
# 설탕 배달
# 다이나믹 프로그래밍, 그리디 알고리즘

N = int(input())
a = 0

while N >= 0:
    if N % 5 == 0:
        a += (N // 5)
        print(a)
        break
    N -= 3
    a += 1
else:
    print(-1)