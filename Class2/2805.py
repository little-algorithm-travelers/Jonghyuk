# BAEKJOON 2805
# 나무 자르기
# 이분탐색

N, M = map(int, input().split())
tree_H = list(map(int, input().split()))

start, end = 0, max(tree_H)

while start <= end:
    mid = (start + end) // 2
    tree = 0

    for i in tree_H:
        if i > mid:
            tree += i - mid
    
    if tree >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)