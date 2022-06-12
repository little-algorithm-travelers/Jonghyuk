# BAEKJOON 2739

a = int(input())

if (a < 1) | (a > 9):
    print("잘못 입력하셨습니다.")

else:
    for i in range(9):
        print(a, "*", i + 1, "=", a * (i+1))