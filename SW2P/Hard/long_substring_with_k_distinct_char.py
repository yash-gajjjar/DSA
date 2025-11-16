s = "aababbcaacc" 
k = 2
unique_ele = len(set(s))
print(unique_ele)

max_length = 0

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substring = s[i:j]
        if len(set(substring)) <=k:
            max_length = max(max_length, len(substring))
    
print(max_length)