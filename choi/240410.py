#오등큰수
import sys
from collections import Counter

n= int(sys.stdin.readline())
inp = list(map(int, sys.stdin.readline().split()))
dict = {}
stack=[]
answer = [-1]*n

dict = Counter(inp)

for i in range(n):
    while stack and dict[inp[stack[-1]]] < dict[inp[i]]:
        idx = stack.pop()
        answer[idx] = inp[i]
    stack.append(i)

print()
print(*answer)
