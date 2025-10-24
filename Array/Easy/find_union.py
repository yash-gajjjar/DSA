nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]

n1_unique_sorted = sorted(list(set(nums1))) 
n2_unique_sorted = sorted(list(set(nums2)))

new = []
i, j = 0, 0

while i < len(n1_unique_sorted) and j < len(n2_unique_sorted):
    if n1_unique_sorted[i] < n2_unique_sorted[j]:
        new.append(n1_unique_sorted[i])
        i += 1
    elif n2_unique_sorted[j] < n1_unique_sorted[i]:
        new.append(n2_unique_sorted[j])
        j += 1
    else:
        new.append(n1_unique_sorted[i])
        i += 1
        j += 1

new.extend(n1_unique_sorted[i:])
new.extend(n2_unique_sorted[j:])

print(new)


#M2

nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]

union_set = set(nums1) | set(nums2)

output = sorted(list(union_set))

print(output)