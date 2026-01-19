def search_2d_matrix(mat, target):
    if not mat or not mat[0]:
        return False
        
    n = len(mat)      # Number of rows
    m = len(mat[0])   # Number of columns
    
    low = 0
    high = (n * m) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        # Convert 1D 'mid' index to 2D row and column
        row = mid // m
        col = mid % m
        
        element = mat[row][col]
        
        if element == target:
            return True
        elif element < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False

mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
target = 80
print(search_2d_matrix(mat, target)) 



def find_kth_positive(arr, k):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        missing = arr[mid] - (mid + 1)
        
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
            
    return k + high + 1

print(find_kth_positive([3, 5, 7, 10], 6))