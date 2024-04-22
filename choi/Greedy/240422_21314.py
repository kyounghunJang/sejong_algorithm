#백준 s1, 그리디, 21314 민겸 수
# li = list(input())

# tmp_max = ''
# tmp_min = ''
# mx = []
# mn = []
# for c in li:
#     if c == 'K':
#         tmp_max += c
#         mx.append(tmp_max)
#         tmp_max = ''

#         if tmp_min != '':
#             mn.append(tmp_min)
#             tmp_min = ''

#     else:
#         tmp_max += c
#         tmp_min += c
# if tmp_max != '':
#     mx.append(tmp_max)
# if tmp_min != '':
#     mn.append(tmp_min)

# min_answer = ''
# max_answer = ''
# for comp in mx:
#     cnt_m = comp.count('M')
#     if comp[-1] != 'K':
#         max_answer += str(10**(cnt_m-1))
#     else:
#         max_answer += str(5*10**(cnt_m))

# for comp in mn:
#     cnt_m = comp.count('M')
#     if comp[-1] != 'K':
#         min_answer += str(10**(cnt_m-1))
#     else:
#         min_answer += str(5*10**(cnt_m))



# print(max_answer)
# print(min_answer)

data = input()
max = "" 
min = "" 
m = 0

for i in range(len(data)):
    if data[i] == 'M':
        m += 1 
    elif data[i] == 'K':
        if m: 
            min += str(10**m + 5) 
            max += str(5 * (10**m)) 
        else: 
            min += "5" 
            max += "5"
        m = 0
if m: 
    min += str(10 ** (m-1))
    while m:
        max += "1"
        m -= 1
print(max)
print(min)

