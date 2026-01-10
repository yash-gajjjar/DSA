def find_nth_root(n, m):
    if m == 1: return 1
    low = 1
    high = m
    
    while low <= high:
        mid = low + (high - low) // 2
        
        val = mid ** n
        
        if val == m:
            return mid
        
        elif val < m:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

print(find_nth_root(4, 81))