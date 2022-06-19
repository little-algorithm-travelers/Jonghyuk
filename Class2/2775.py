# BAEKJOON 2775
# 부녀회장이 될테야

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    floor_list = [i for i in range(1, n + 1)] # 0층 사람 수
    for i in range(k): # k층만큼 반복
        for j in range(1, n): # 각 호수만큼 반복(인덱스)
            floor_list[j] += floor_list[j - 1] # 각 호수의 사람 수 구하기
    
    print(floor_list[-1]) # k층의 n호 사람 수 출력