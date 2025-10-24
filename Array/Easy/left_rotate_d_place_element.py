a = [1, 2, 3, 4, 5, 6, 7]
k = 2
n = len(a)

temp = a[:k]

for i in range(n - k):
    a[i] = a[i + k] 
    
for i in range(k):
    a[n - k + i] = temp[i]
    
print(a)

