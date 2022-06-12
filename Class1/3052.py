# BAEKJOON 3052

num_list = []
for _ in range(10):
    a = int(input())
    b = a % 42
    num_list.append(b)

result_list = set(num_list) # set은 중복 제거, 순서 고려하지 않음

print(len(result_list))