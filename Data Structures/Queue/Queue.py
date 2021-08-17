class queue:

    def __init__(self, start, size):            # circular array constructor

        self.arr = [0]*size
        self.start = start
        self.size = size
        self.idx = start

    def enqueue(self, item):                    # adds at the end

        self.arr[self.idx] = item
        self.idx = (self.idx+1)%len(self.arr)

    def dequeue(self):                          # removes at the beginning

        remove = self.arr[self.start]
        self.arr[self.start] = 0

        self.start += 1
        
        return remove

    def peek(self):

        return self.arr[self.start]

    def print(self):

        print(self.arr)



q = queue(0, 5)


q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print()
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.print()

print(q.peek())