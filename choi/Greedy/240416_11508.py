#백준 s4, 그리디, 11508 2+1 세일
cost = []
n = int(input())
for i in range(n):
    cost.append(int(input()))

cost.sort(reverse=True)

p=2
total = 0
for i in range(n):
    if i != p:
        total += cost[i]
    else:
        p+=3

print(total)

