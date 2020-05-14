class SortStack():
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def is_empty(self):
        return len(self.st1) + len(self.st2) == 0

    def push(self, input):
        if len(self.st1) == 0 or input <= self.st1[-1]:
            self.st1.append(input)
        else:
            while len(self.st1) > 0 and self.st1[-1] < input:
                self.st2.append(self.st1.pop())
            
            self.st1.append(input)

            while len(self.st2) > 0:
                self.st1.append(self.st2.pop())

    
x = SortStack()

x.push(6)
x.push(1)
x.push(9)
x.push(0)
x.push(-1)

print(x.st1)