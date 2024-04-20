# 백준 s2, 그리디, 16953 A->B
a, b = map(int, input().split())

total = 1
while 1:
    if b%10 == 1:
        b = b//10
        total += 1
    elif b%2 == 0:
        b = b//2
        total += 1
    else:
        total = -1
        break
    if b<a:
        total = -1
        break
    if b==a:
        break

print(total)