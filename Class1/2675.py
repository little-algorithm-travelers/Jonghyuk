# BAEKJOON 2675

T = int(input())

for i in range(T):
    R, word = input().split() # 입력받기, int도 str도 아니다.
    for j in word: # word 처음부터 반복
        print(j*int(R), end="") # R을 int화 시켜주고 반복, end=""는 줄바꿈 안하도록 하기
    print()