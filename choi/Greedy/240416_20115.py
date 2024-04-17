#백준 s3, 그리디, 20115 에너지 드링크
n = int(input())
drink = list(map(int, input().split()))
drink.sort(reverse=True)

total = drink[0]

for i in range(1, n):
    total += drink[i]/2

print(total)