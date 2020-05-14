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
    
def get_dups_and_remove(head_ori):
    head = head_ori
    hash_map = {}
    if not head:
        return None
    
    hash_map[head.data] = True

    while head.next:
        head_bak = head
        head = head.next

        if hash_map.get(head.data):
            #stitch
            head_bak.next = head.next
            head = head_bak
        else:
            #regis
            hash_map[head.data] = True
    return head_ori

print_ll(get_dups_and_remove(create_ll([1,4,6,4,5])))