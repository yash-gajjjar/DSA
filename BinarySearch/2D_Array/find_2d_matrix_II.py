def search_matrix_ii(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    n = len(matrix)      # Rows
    m = len(matrix[0])   # Columns
    
    # Start at the Top-Right corner
    row = 0
    col = m - 1
    
    while row < n and col >= 0:
        current = matrix[row][col]
        
        if current == target:
            return True
        
        elif target < current:
            col -= 1
        else:
            row += 1
            
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

print(search_matrix_ii(matrix, 5))
print(search_matrix_ii(matrix, 20))