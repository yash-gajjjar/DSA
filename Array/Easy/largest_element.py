def find_largest_element(arr):
    if not arr:
        return None
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

a = find_largest_element(arr=[3,3,6,1,8,4,2])
print(a)