def insert_at_head(head, x):
    new_node = {
        'data': x,
        'next': head 
    }
    return new_node

def print_list(head):
    temp = head
    while temp is not None:
        print(temp['data'], end=" ")
        temp = temp['next']
    print("None")

head = {'data': 1, 'next': {'data': 2, 'next': {'data': 3, 'next': None}}}
print_list(head)
head = insert_at_head(head, 7)
print_list(head)