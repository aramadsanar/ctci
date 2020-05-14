class QueueStack():
    def __init__(self):
        self.queue = []
        self.temp = []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        result = self.queue[0]

        self.temp.extend(self.queue[1:])
        self.queue = []
        self.queue.extend(self.temp)
        self.temp = []

        return result

x = QueueStack()

x.enqueue(1)
x.enqueue(2)
x.enqueue(3)

print(x.dequeue())
print(x.dequeue())
print(x.dequeue())