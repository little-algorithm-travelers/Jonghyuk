# BAEKJOON 1157

a = input().upper() # 결과는 대문자로
a_list = list(set(a)) # set는 중복 제거, list는 배열만들기
cnt = [] 

for i in a_list: # 배열 첫번째부터 끝까지 반복
    count = a.count(i) 
    cnt.append(count) # count한 숫자를 cnt에 추가

if cnt.count(max(cnt)) > 1: # 최대 cnt가 여러개면 ? 출력
    print("?")
else: 
    print(a_list[(cnt.index(max(cnt)))]) # 아니면 최대 cnt의 문자 출력