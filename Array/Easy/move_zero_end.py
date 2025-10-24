a = [0, 1, 0, 3, 12]
zero = []
non_zero = []

for i in range(len(a)):
    if a[i] == 0:
        zero.append(a[i])
    else:
        non_zero.append(a[i])

a = non_zero + zero
print(a)    


#M2

a = [1, 0, 3, 12]
n = len(a)
non_zero_index = 0

for i in range(n):
    if a[i] != 0:
        a[i], a[non_zero_index] = a[non_zero_index], a[i]
        non_zero_index += 1

print(a)
