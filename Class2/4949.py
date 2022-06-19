# BAEKJOON 4949
# 균형잡힌 세상
# 자료 구조, 문자열, 스택

while True:
    a = input()
    stack_list = []

    if a == ".":
        break

    for i in a:
        if i == "[" or i == "(":
            stack_list.append(i)
        elif i == "]":
            if len(stack_list) != 0 and stack_list[-1] == "[":
                stack_list.pop()
            else:
                stack_list.append(i)
                break
        elif i == ")":
            if len(stack_list) != 0 and stack_list[-1] == "(":
                stack_list.pop()
            else:
                stack_list.append(i)
                break

    if len(stack_list) == 0:
        print("yes")
    else:
        print("no")