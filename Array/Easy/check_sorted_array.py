def check_sorted_array(arr):
    if not arr:
        return True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

c = check_sorted_array(arr=[1,2,2,3,4,5])
print(c)