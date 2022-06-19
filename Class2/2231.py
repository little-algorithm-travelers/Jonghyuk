# BAEKJOON 2231
# 분해합

N = int(input())

def decompose(n):
    a, m = 0, n
    while n != 0:
        a = int(a + (n % 10))
        n = int(n / 10)
    return int(a + m)

def findSum(A):
    for i in range(abs(A - (len(str(A)) * 9)), A): # 시간 최적화 (왜안되지?)
        if N == decompose(i):
            return i
    return 0
        
print(findSum(N))