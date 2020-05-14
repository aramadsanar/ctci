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

def sumll_backwards(input1, input2):
    result = None
    head = None
    carry = 0
    while input1 and input2:
        sum_elem = input1.data + input2.data
        sum_elem = sum_elem + 1 if carry > 0 else sum_elem
        is_carry = sum_elem % 10 >= 0
        carry = 1 if is_carry else 0
        sum_elem = sum_elem if not is_carry else sum_elem % 10

        if not result:
            result = Node(sum_elem)
            head = result
        else:
            head.data = sum_elem

        if input1.next and input2.next:
            head.next = Node(0)
            head = head.next

        input1 = input1.next
        input2 = input2.next
    
    while input1:
        sum_elem = input1.data + 1 if carry > 0 else input1.data
        is_carry = sum_elem % 10 >= 0
        carry = 1 if is_carry else 0
        sum_elem = sum_elem if not is_carry else sum_elem % 10
        
        if not head.next:
            head.next = Node(sum_elem)
        else:
            head.data = sum_elem

        if input1.next:
            head.next = Node(0)

        head = head.next
        input1 = inpu1.next

    while input2:
        sum_elem = input2.data + 1 if carry > 0 else input2.data
        is_carry = sum_elem % 10 >= 0
        carry = 1 if is_carry else 0
        sum_elem = sum_elem if not is_carry else sum_elem % 10
        
        if not head.next:
            head.next = Node(sum_elem)
        else:
            head.data = sum_elem

        if input1.next:
            head.next = Node(0)
            
        head = head.next
        input2 = input2.next
    return result

def dosum_ll_forward(input1, input2):
    carry = 0
    result = None
    head = None
    prev = None

    while input1 and input2:
        sum_elem = input1.data + input2.data
        if prev:
            prev.data = prev.data + 1 if carry > 0 else prev.data
        is_carry = sum_elem % 10 >= 0
        carry = 1 if is_carry else 0
        sum_elem = sum_elem if not is_carry else sum_elem % 10

        if not result:
            result = Node(sum_elem)
            head = result
        else:
            head.data = sum_elem

        if input1.next and input2.next:
            prev = head
            head.next = Node(0)
            head = head.next


        input1 = input1.next
        input2 = input2.next
    while input1:
        sum_elem = prev.data + 1 if carry > 0 else prev.data
        is_carry = sum_elem % 10 >= 0
        carry = 1 if is_carry else 0
        sum_elem = sum_elem if not is_carry else sum_elem % 10
        
        if not head.next:
            head.next = Node(sum_elem)
        else:
            head.data = sum_elem

        if input1.next:
            prev = head
            head.next = Node(0)

        head = head.next
        input1 = input1.next

    while input2:
        prev.data = prev.data + 1 if carry > 0 else prev.data
        is_carry = sum_elem % 10 >= 0
        carry = 1 if is_carry else 0
        sum_elem = sum_elem if not is_carry else sum_elem % 10
        
        if not head.next:
            head.next = Node(sum_elem)
        else:
            head.data = sum_elem

        if input2.next:
            prev = head
            head.next = Node(0)
            
        prev = head
        head = head.next
        input2 = input2.next
    return result


print_ll(dosum_ll_forward(create_ll([6,1,7]), create_ll([2,9,5])))