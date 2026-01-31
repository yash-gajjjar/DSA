def insert_at_tail(head, x):
    new_node = {
        'data': x,
        'next': None 
    }

    if head is None:
        return new_node
    
    # Traverse to the last node
    current = head
    while current['next'] is not None:
        current = current['next']
        
    # Link the last node to the new node
    current['next'] = new_node
    
    # Return the original head
    return head

head = {'data': 7, 'next': {'data': 1, 'next': None}}

head = insert_at_tail(head, 100)
print(head)