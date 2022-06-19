# BAEKJOON 2869
# 달팽이는 올라가고 싶다.
# 수학, (시간초과됐었음)

A, B, V = list(map(int, input().split()))
H, date = 0, 0

if (V - A) % (A - B) == 0: # 한방에 올라감
    date = int((V - A) // (A - B))
else:
    date = int((V - A) // (A - B)) + 1

print(date + 1) 