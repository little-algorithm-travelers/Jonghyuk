# BAEKJOON 2562

num_list = []

for i in range(9):
    num_list.append(int(input())) # 한 줄씩 변수 받기

max_num = max(num_list) # 최대값 찾기

print(max_num) 
print(num_list.index(max_num)+1) # 최대값 자리 찾기