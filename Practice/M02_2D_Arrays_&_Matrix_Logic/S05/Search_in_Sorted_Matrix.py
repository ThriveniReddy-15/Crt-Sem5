#74 - Search of a 2d Matrix 
from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    '''
    arr = []
    for row in matrix:
        arr += row 
    left,right = 0,len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if target == arr[mid]:
            return True 
        elif target < arr[mid]:
            right = mid-1 
        else:
            left = mid+1
    return False
    '''
    if not matrix or not matrix[0]:
        return False
    rows,cols = len(matrix),len(matrix[0]) 
    left,right = 0,(rows*cols)-1
    while left <= right:
        mid = (left+right)//2
        mid_val = matrix[mid//cols][mid%cols]
        if  mid_val == target:
            return True 
        elif mid_val < target:
            left = mid+1 
        else:
            right = mid-1
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3 
print(searchMatrix(matrix,target))
# 240 - 
def searchMatrix1(matrix: List[List[int]], target: int) -> bool:
    m,n = len(matrix),len(matrix[0])
    row,col = 0,n-1
    while row <m and col >= 0:
        if target == matrix[row][col]:
            return True 
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1 
    return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix1) 
# 378