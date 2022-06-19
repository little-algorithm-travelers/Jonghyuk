# BAEKJOON 1018

N, M = map(int, input().split()) # N, M 입력받기
chessbord = []
res_list = []
for i in range(N): # 체스판 입력받기
    chessbord.append(input())

for i in range(N - 7): 
    for j in range(M - 7): # 8*8 체스판을 만들기 위해 i ~ N-7, j ~ M-7
        first_w = 0
        first_b = 0
        for a in range(i, i + 8): # range 마지막 숫자는 포함 X
            for b in range(j, j + 8):

                # 체스판 색깔은 번갈아 가면서 나옴 
                # 격자판 좌표를 더한 값으로 계산
                if (a + b) % 2 == 0: 
                    if chessbord[a][b] != "W": # 첫 격자 색이 백색이 아니라면
                        first_w += 1           # 첫 격자의 색이 백색일 경우 바꾸어야할 칸 +1
                    if chessbord[a][b] != "B": # 첫 격자 색이 흑색이 아니라면
                        first_b += 1           # 첫 격자의 색이 흑색일 경우 바꾸어야할 칸 +1
                else:
                    if chessbord[a][b] != "W": # 첫 격자 옆칸 색이 백색이 아니라면
                        first_b += 1           # 첫 격자의 색이 흑색일 경우 바꾸어야할 칸 +1
                    if chessbord[a][b] != "B": # 첫 격자 옆칸 색이 흑색이 아니라면
                        first_w += 1           # 첫 격자의 색이 백색일 경우 바꾸어야할 칸 +1
        res_list.append(first_w) # 첫 격자 색이 백색일 경우
        res_list.append(first_b) # 첫 격자 색이 흑색일 경우

# print(res_list)
print(min(res_list))