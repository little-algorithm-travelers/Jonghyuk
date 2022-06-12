# BAEKJOON 2475

num_list = list(map(int, input().split()))
sum = 0 
res_num = 0

for i in num_list:
    # sum += pow(i, 2) n제곱 구하는 법 -> pow(i, n) -> i는 제곱의 대상, n은 몇번 제곱할건지
    sum += i * i # 노가다

res_num = sum % 10
print(res_num)