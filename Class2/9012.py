# BAEKJOON 9012
# 괄호
# 자료 구조, 문자열, 스택

N = int(input())
stack_list = []
for _ in range(N):
    a = input()
    for i in a:
        if i == "(":
            stack_list.append(i)
        elif i == ")":
            if len(stack_list) != 0 and stack_list[-1] == "(":
                stack_list.pop()
            else:
                stack_list.append(i)
    if len(stack_list) == 0:
        print("YES")
    else:
        print("NO")

    stack_list = []