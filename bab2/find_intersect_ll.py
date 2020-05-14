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

def get_ll_len(head):
    result = 0
    while head:
        result += 1
        head = head.next
    return result

def get_intersect_ll(head_a, head_b):
    len_a = get_ll_len(head_a)
    len_b = get_ll_len(head_b)

    delta = abs(len_a - len_b)
    moved_head = head_a if len_a > len_b else head_b
    stay_head = head_a if len_a < len_b else head_b

    for i in range(delta):
        moved_head = moved_head.next

    while moved_head and stay_head:
        if moved_head == stay_head:
            return moved_head

        moved_head = moved_head.next
        stay_head = stay_head.next
    
    return None

ll_a = create_ll([1, 2, 3])
ll_b = create_ll([4, 5])
ll_c = create_ll([6, 7, 8])

def get_ll_end(head):
    head_copy = head
    while head_copy.next:
        head_copy = head_copy.next

    return head_copy


ll_end_a = get_ll_end(ll_a)
ll_end_b = get_ll_end(ll_b)

ll_end_a.next = ll_c
ll_end_b.next = ll_c

print(get_intersect_ll(ll_a, ll_b).data)