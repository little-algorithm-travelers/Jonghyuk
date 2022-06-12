# BAEKJOON 10818

N = int(input())
num_list = list(map(int, input().split()))
max_num = num_list[0]
min_num = num_list[0]

for i in num_list:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print(min_num, max_num)