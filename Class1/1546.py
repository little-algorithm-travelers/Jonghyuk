# BAEKJOON 1546

a = int(input()) # 첫째 줄 과목 개수
a_list = list(map(int, input().split())) # 입력받아 list화 시킴
max_a = max(a_list) # 최고점수
sum_a = 0  

for i in a_list:
    sum_a += (i / max_a) * 100 # 점수 계산

print(sum_a / a) # 평균내기