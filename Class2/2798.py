# BAEKJOON 2798
# 블랙잭

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
max = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if card_list[i] + card_list[j] + card_list[k] <= M:
                if max < card_list[i] + card_list[j] + card_list[k]:
                    max = card_list[i] + card_list[j] + card_list[k]
print(max)     