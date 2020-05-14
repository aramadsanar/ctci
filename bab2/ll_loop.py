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

def get_ll_end(head):
    head_copy = head
    while head_copy.next:
        head_copy = head_copy.next

    return head_copy



ll_a = create_ll([9, 6, 7, 3, 4])
ll_end = get_ll_end(ll_a)
# print(ll_end.data)
ll_end.next = ll_a.next.next

# print(ll_end.next.data)
def has_loop(head):
    fast = head
    slow = head.next.next

    while fast and head and fast != slow:
        if fast == slow:
            print(fast.data)
            print(slow.data)
            break

        fast = fast.next.next
        slow = slow.next
    
    slow = head

    while fast != slow:
        if fast == slow:
            break
        slow = slow.next
        fast = fast.next
    
    return fast

print(has_loop(ll_a).data)