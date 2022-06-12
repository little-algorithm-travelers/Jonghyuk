# BAEKJOON 8958

T = int(input())
score = 0 # 최종 점수
num = 0 # 연속 정답 시 추가 점수

for _ in range(T):
    quiz = list(input()) # 입력받기
    for i in quiz: 
        if i == "O": # 맞았으면
            num += 1 # 1점, 연속이면 추가 점수
            score += num # 최종 점수 계산
        elif i == "X": # 틀렸으면
            num = 0 # 추가 점수 모두 제거
    print(score) 
    num = 0
    score = 0