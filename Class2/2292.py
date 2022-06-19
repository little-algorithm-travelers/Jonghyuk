# BAEKJOON 2292
# 벌집

N = int(input())
room, cnt = 1, 1

while room < N:
    room += cnt * 6
    cnt += 1

print(cnt)