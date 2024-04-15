#백준 s3, 그리디, 13305 주유소
# n = int(input())
# oil = list(map(int, input().split()))
# cost = list(map(int, input().split()))

# li1 = []
# li2 = []
# total = 0

# oil_pop = []
# cost_pop = []
# while oil:
#     if len(oil) == 1:
#         break
#     tmp = oil.pop(0)
#     if not oil_pop:
#         oil_pop.append(tmp)
#     cost_pop.append(cost.pop(0))

#     if oil_pop[0] >= oil[0]:
#         for c in cost_pop:
#             total += oil_pop[0]*c
#         oil_pop = []
    
# print(total)