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

print(find_kth_positive([3, 5, 7, 10], 3))