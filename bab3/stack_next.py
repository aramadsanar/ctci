class StackNext():
    def __init__(self, threshold):
        self.threshold = threshold
        self.stack_arr = []
    
    def push(self, data):
        if len(self.stack_arr) == 0 or len(self.stack_arr[-1]) >= self.threshold:
            self.stack_arr.append([])
        if len(self.stack_arr[-1]) < self.threshold:
            self.stack_arr[-1].append(data)

    def pop(self):
        data = None
        if len(self.stack_arr) > 0 and len(self.stack_arr[-1]) > 0:
            data = self.stack_arr[-1][-1]

            self.stack_arr[-1].pop()

            if (len(self.stack_arr[-1]) == 0):
                self.stack_arr.pop()
            
        return data
    
    def pop_at(self, idx):
        temp = []
        result = None
        if idx == 0:
            return result
        
        else:
            while idx > 0:
                temp.append(self.pop())
                idx -= 1

            result = temp.pop()

            while len(temp) > 0:
                self.push(temp.pop())

        return result

x = StackNext(5)

for y in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
    x.push(y)

print(x.pop())
print(x.pop_at(3))
