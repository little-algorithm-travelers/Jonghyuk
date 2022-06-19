# BAEKJOON 1018

x, y, w, h = map(int, input().split()) # 한수의 위치 (x, y), 오른쪽 위 꼭짓점 (w, h)

dis_x = w - x # 너비까지의 거리
dis_y = h - y # 높이까지의 거리

print(min(dis_x, dis_y, x, y)) # dis_x, dis_y 뿐만이 아닌 x축, y축 까지의 거리도 신경써야함