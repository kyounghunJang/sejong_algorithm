#프로그래머스 행렬의 곱셈
#틀렸어요,, so sad
# arr1 = [[1, 4], [3, 2], [4, 1]]
# arr2 = [[3, 3], [3, 3]]

# def solution(arr1, arr2):
#     l1 = len(arr1)
#     l2 = len(arr2)
#     new_arr2 = [[] for _ in range(len(arr2[0]))]
#     for i in range(l2):
#         for j in range(l2):
#             new_arr2[j].append(arr2[i][j])

#     answer = [[] for _ in range(l1)]
#     for i in range(l1):
#         for j in range(l2):
#             answer[i].append(sum([i*j for (i, j) in zip(arr1[i], new_arr2[j])]))
    
#     print(answer)




# solution(arr1, arr2)

import numpy as np

def solution(arr1, arr2):
    answer = np.dot(arr1, arr2).tolist()
    
    return answer