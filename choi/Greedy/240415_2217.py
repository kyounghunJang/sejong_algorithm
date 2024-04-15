#백준 s4, 그리디, 2217 로프
n = int(input())

li = []
max = -1

for _ in range(n):
    li.append(int(input()))
li.sort()

for i in range(n):
    if max < li[i]*(n-i):
        max = li[i]*(n-i)

print(max)