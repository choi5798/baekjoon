from collections import Counter, deque

def row_check(arr):
    for i in range(9):
        counter = Counter(arr[i])
        values = set(counter.values())
        if len(values) != 1:
            return False
        
    return True

def col_check(arr: list):
    
    for i in range(9):
        col = []
        for j in range(9):
            col.append(arr[j][i])
            
        counter = Counter(col)
        values = set(counter.values())
        if len(values) != 1:
            return False
        
    return True

def box_check(arr, target_i, target_j):
    pass
        
    
def is_proof(arr):
    if row_check(arr) and col_check(arr) and box_check(arr):
        return True
    return False

def back_tracking():
    sudoku = []
    zeros = deque()

    for i in range(9):
        row = list(map(int, input().split()))
        sudoku.append(row)
        if 0 in row:
            idx = row.index(0)
            zeros.append((i,idx))
        
    while zeros:
        zero_i, zero_j = zeros.popleft()
        
back_tracking()