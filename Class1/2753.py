# BAEKJOON 2753

year = int(input())

if (year % 4 == 0): # 4의 배수이면서
    if (year % 100 != 0) | (year % 400 == 0): # 100의 배수가 아니거나 400의 배수일 때
        print(1)
    else:
        print(0)
else:
    print(0)