from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    
    for i in course:
        menu=[]
        for j in orders:
            comb = combinations(sorted(j), i)
            menu+=comb
        counter=Counter(menu)
        if len(counter) != 0 and max(counter.values()) !=1:
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))
    return sorted(answer)