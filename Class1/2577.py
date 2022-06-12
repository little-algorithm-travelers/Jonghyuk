# BAEKJOON 2562

A = int(input())
B = int(input())
C = int(input())

res = list(str(A * B * C)) # 곱한 결과를 str로 list업

for i in range(10): # 0~9 -> 10
    print(res.count(str(i))) # list안에는 모두 str이므로 str을 카운트 해야함