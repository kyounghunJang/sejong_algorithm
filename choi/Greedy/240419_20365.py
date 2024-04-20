# 백준 s3, 그리디, 20365 블로그2
n = int(input())
s = input()

tmp_b= ''
tmp_r = ''
li_b = []
li_r = []

for i in range(n):
    if s[i] == 'B':
        tmp_b += s[i]
        if tmp_r != '':
            li_r.append(tmp_r)
            tmp_r = ''
    else:
        tmp_r += s[i]
        if tmp_b != '':
            li_b.append(tmp_b)
            tmp_b = ''
if tmp_r != '':
    li_r.append(tmp_r)
if tmp_b != '':
    li_b.append(tmp_b)

print(min(len(li_r), len(li_b))+1)