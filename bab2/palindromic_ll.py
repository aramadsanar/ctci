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

def reverse_ll(head):
    head_copy = head
    result = None
    reshead = None
    if not head_copy.next and not result:
        result = Node(head_copy.data)
        reshead = result
        return reshead, result
    
    reshead, result = reverse_ll(head_copy.next)
    
    if head_copy.next:
        result.next = Node(head_copy.data)
        result = result.next

    return reshead, result

def is_ll_palindromic(head_ori, head_rev):
    while head_ori and head_rev:
        if head_ori.data != head_rev.data:
            return False

        head_ori = head_ori.next
        head_rev = head_rev.next

    if head_ori or head_rev:
        return False

    return True

def get_ll_len(head):
    result = 0
    while head:
        result += 1
        head = head.next
    return result

def is_ll_palindromic_recursive(head):
    len_head = get_ll_len(head)

    

lll = create_ll([3,2,1,2,3])
print(get_ll_len(lll))
print(is_ll_palindromic(lll, reverse_ll(lll)[0]))

# def is_ll_palindromic(head):


# def check_ll_palindrome(head):
#     return is_ll_palindromic(head, )