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

class AnimalShelter():
    def __init__(self):
        self.queue_ll = None
        self.queue_tail = None
    def enqueue(self, animal_type):
        if not self.queue_ll:

            self.queue_ll = Node(animal_type)
            self.queue_tail = self.queue_ll
        else:
            self.queue_tail.next = Node(animal_type)
            self.queue_tail = self.queue_tail.next
        # print(self.queue_tail.data)
    
    def print_queue(self):
        print_ll(self.queue_ll)
        print('-----------------')
    
    def dequeue_any(self):
        head = self.queue_ll
        self.queue_ll = self.queue_ll.next

        head.next = None
        return head
    def dequeue_by_animal_type(self, animal_type):
        head = self.queue_ll
        prev = None
        while head and head.data != animal_type:
            if head.data == animal_type:
                break
            prev = head
            head = head.next
        
        if not head:
            return None
        if prev:
            prev.next = head.next
        
    
        head.next = None

        return head

x = AnimalShelter()
x.enqueue("dog")
x.enqueue("cat")
x.enqueue("dog")
x.enqueue("dog")
x.enqueue("cat")
x.enqueue("cat")

x.dequeue_by_animal_type('cat')

x.print_queue()

# x.dequeue_by_animal_type

x.dequeue_by_animal_type('cat')

x.print_queue()
