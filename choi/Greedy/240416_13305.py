#백준 s3, 그리디, 13305 주유소
n = int(input())
oil = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
total = 0

#제일 최소값으로 많이 사야하므로 
for i in range(n-1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    total += min_cost*oil[i]

print(total)