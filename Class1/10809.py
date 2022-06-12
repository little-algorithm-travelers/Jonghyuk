# BAEKJOON 10809

S = list(input())
alpabet = "abcdefghijklmnopqrstuvwxyz" 

for i in alpabet: # 알파벳 처음부터 끝까지 반복
    if i in S: # 해당하는 알파벳이 S 안에 있다면?
        print(S.index(i), end=" ") # S안에 몇번째인지, 띄어쓰기 포함
    else:
        print("-1", end=" ")