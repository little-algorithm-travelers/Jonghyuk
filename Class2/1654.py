# BAEKJOON 1654
# 이진탐색, 보고 풀었음;(왜 내가 한 방식대로는 안될까)

K, N = map(int, input().split()) # 입력받기
lan_list = [] # 랜선 리스트

for _ in range(K): # K개의 랜선 입력받기
    lan_list.append(int(input()))

start, end = 1, max(lan_list) # 시작과 끝지점

while start <= end: # 양쪽끝에서 시작해서 만나는 지점 (이진탐색)
    mid = (start + end) // 2
    sum_lan = 0
    for i in lan_list: # K번 반복
        sum_lan += int(i // mid) # 자르고 난 뒤의 랜선 개수
    if sum_lan >= N: # 자른 개수가 N보다 더 많다면 더 크게 잘라야함 (이 조건이 없어서 실패한듯)
        start = mid + 1
    else:
        end = mid - 1

print(end)

'''
K, N = map(int, input().split()) # 입력받기
lan_list = [] # 랜선 리스트
sum_lan = 0 # 자른 랜선의 합

for _ in range(K): # K개의 랜선 입력받기
    lan_list.append(int(input()))
 
min_list = min(lan_list) # 가장 짧은 선부터 자르기 시작
while 1:
    res_list = [] # 자르고 난 랜선 리스트
    for i in range(K): # K번 반복
        res_list.append(int(lan_list[i] / min_list)) # 자르고 난 뒤의 랜선 개수
    if sum(res_list) > N: # 랜선 개수의 합이 N개보다 높아지면 탈출
        break
    min_list -= 1 # 점차 줄은 짧아짐

print(min_list)
'''