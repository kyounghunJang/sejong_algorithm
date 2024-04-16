#백준 s4, 그리디, 1758 알바생 강호
money = []
n = int(input())
for i in range(n):
    money.append(int(input()))
money.sort(reverse=True)

total = 0
for i in range(1, n+1):
    if money[i-1]-(i-1) > 0:
        total += money[i-1]-(i-1)

print(total)