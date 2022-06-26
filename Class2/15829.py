# BAEKJOON 15829
# Hashing

l = int(input())
data = list(input())
sum = 0
for i in range(l):
    sum = sum + (ord(data[i]) % 96)*(31**i)
print(sum % 1234567891)