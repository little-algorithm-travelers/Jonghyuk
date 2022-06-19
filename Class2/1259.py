# BAEKJOON 1259
# 팰린드롬수 : 뒤에서 읽어도 똑같은 단어 ex radar sees
# reversed에 대해 익히자

while(1):

    x = list(input())
    if x == ["0"]:
        exit()
    y = list(reversed(x))

    if x == y:
        print("yes")
    elif x != y:
        print("no")