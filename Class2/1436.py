# BAEKJOON 1436

N = int(input())
num = 666

while N != 0: 
    if '666' in str(num):
        N = N-1
        if N == 0:
            break
    num += 1

print(num)
