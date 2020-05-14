class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def create_ll(arr):
    result = None
    head = None
    print(arr)
    for i in range(len(arr)):
        n = arr[i]

        if head:
            head.next = Node(n)
            head = head.next
        if not result:
            head = Node(n)
            result = head
        

    return result

def print_ll(head):
    while head:
        print(head.data)
        head = head.next
    
def get_kth_elem(head, k):
    head1 = head
    head2 = head

    #park the head2 to kth elem
    i = 0
    while i < k:
        if head2.next:
            head2 = head2.next
        else:
            break
        i += 1

    if i != k:
        return None

    while head2.next:
        head2 = head2.next
        head1 = head1.next

    return head1

def get_kth_last_recursive(head, k):
    if not head.next:
        return 0

    nthlast= get_kth_last_recursive(head.next, k)

    if type(nthlast) is dict:
        return nthlast

    result = 1 + nthlast

    if result == k:
        result = {
            'k': k,
            'node': head.data
        }
        
    return result

print_ll(get_kth_elem(create_ll([1,4,6,4,5, 9, 7, 3]), 2))

print(get_kth_last_recursive(create_ll([1,4,6,4,5, 9, 7, 3]), 2))

# print(get_kth_elem(create_ll([1,4]), 2))