class StackMin():
    def __init__(self):
        self.data = []
        self.mintrack = []
    
    def push(self, data):
        if len(self.data) == 0 and len(self.mintrack) == 0:
            self.data.append(data)
            self.mintrack.append(data)
        else:
            if data < self.mintrack[-1]:
                self.mintrack.append(data)
            else:
                self.mintrack.append(self.mintrack[-1])
            self.data.append(data)
    def min(self):
        if len(self.mintrack) == 0:
            return None
        return self.mintrack[-1]
    def pop(self):
        self.mintrack.pop()
        self.data.pop()

    def peek(self):
        return self.data[-1]


sm = StackMin()

for i in [-1, 9, 7, 0, -33, 1, -44]:
    sm.push(i)

print(sm.min())