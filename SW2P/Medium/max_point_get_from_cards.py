# Two Pointer

cardScore = [1, 2, 3, 4, 5, 6] 
k = 3
n = len(cardScore)

max_score = 0
    
current_score = sum(cardScore[:k])
max_score = current_score
j = n - 1

for i in range(1, k + 1):
    card_to_remove = cardScore[k - i]
    current_score -= card_to_remove
    
    card_to_add = cardScore[j]
    current_score += card_to_add
    
    j -= 1
    max_score = max(max_score, current_score)
print(max_score)


# Sliding Window

# cardScore = [1, 2, 3, 4, 5, 6] 
# k = 3
# n = len(cardScore)

# window = n - k
# total_sum = sum(cardScore)

# if window == 0:
#     print(total_sum)
    
# current_window_sum = sum(cardScore[:window])
# min_window_sum = current_window_sum

# for i in range(window, n):
#     current_window_sum = current_window_sum + cardScore[i] - cardScore[i-window]
#     min_window_sum = min(min_window_sum, current_window_sum)
    
# max_chosen_score = total_sum - min_window_sum

# print(max_chosen_score)

