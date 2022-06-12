# BAEKJOON 2439

a = int(input()) # 정수 입력받기

for i in range(a): # 입력받은만큼 반복
    b = "*" * (i+1) # *의 개수는 줄번호에 맞게
    print(b.rjust(a)) # 오른쪽 정렬은 rjust(n) -> n은 n칸 자리수를 의미, 좌측은 ljust(n)