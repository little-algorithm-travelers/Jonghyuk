# BAEKJOON 4153
# 직각삼각형

while 1:
    a = list(map(int, input().split()))
    c = max(a)
    a.remove(c)

    if a[0] == 0 and a[1] == 0 and c == 0:
        break
    if a[0] ** 2 + a[1] ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")