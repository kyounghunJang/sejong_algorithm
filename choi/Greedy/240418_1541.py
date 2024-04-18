# 백준 s2, 그리디, 1541 잃어버린 괄호
inp = input()

li = inp.split('-')

for i in range(len(li)):
    if '+' in li[i]:
        tmp = li[i].split('+')
        tmp = map(int, tmp)
        li[i] = sum(tmp)

li = list(map(int, li))

for i in range(len(li)-1):
    tmp = li[i] - li[i+1]
    li[i+1] = tmp

print(li[-1])
