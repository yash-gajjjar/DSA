def find_first_one(row, m):
    low = 0
    high = m - 1
    first_idx = m 
    
    while low <= high:
        mid = low + (high - low) // 2
        if row[mid] == 1:
            first_idx = mid
            high = mid - 1 # Look further left for an earlier 1
        else:
            low = mid + 1
    return first_idx


def row_with_max_ones(mat):
    n = len(mat)  # row    
    m = len(mat[0])   # column
    
    max_ones = 0
    ans_row = -1
    
    for i in range(n):
        first_one_idx = find_first_one(mat[i], m)
        
        count_ones = m - first_one_idx
        
        if count_ones > max_ones:
            max_ones = count_ones
            ans_row = i
            
    return ans_row

mat = [ [0, 0], [0, 0] ]
print(row_with_max_ones(mat))