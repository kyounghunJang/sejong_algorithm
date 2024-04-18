#백준 s3, 그리디, 19941 햄버거 분배
a, b = map(int, input().split())
inp = list(input())

total = 0
for i in range(a):
    if inp[i] == 'P':
        for idx in range(i-b, i+b+1):
            if idx>=0 and idx<a:
                if inp[idx] == 'H':
                    inp[idx] = 'X'
                    total += 1
                    break

print(total)