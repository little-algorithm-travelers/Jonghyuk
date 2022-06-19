# BAEKJOON 1978
# 소수 찾기

N = int(input())
N_list = list(map(int, input().split()))
res_list = []

def prime_num(a):
    if a == 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


for j in N_list:
    if prime_num(j):
        res_list.append(j)

print(len(res_list))