#백준 s3, 그리디, 20300 서강근육맨
n = int(input())
li = list(map(int, input().split()))
li.sort()

max = 0
if n%2 != 0:
    max = li.pop(-1)
    n -= 1
for i in range(n//2):
        if max < li[i]+li[n-i-1]:
            max = li[i]+li[n-i-1]

print(max)
