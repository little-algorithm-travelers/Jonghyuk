# BAEKJOON 1181
# sort, sorted를 익히자

N = int(input()) # 개수 입력받기
word_list = []

for i in range(N): # 문자열 입력받기
    word_list.append(input())

word_list = list(set(word_list)) # list 중복 제거 후 다시 list화
res_list = sorted(word_list) # @@ = sorted(@@) 알파벳 순으로 정렬 후 다시 선언
res_list.sort(key = len) # @@.sort(key = len) -> 길이 순으로 정렬
for i in res_list:
    print(i)