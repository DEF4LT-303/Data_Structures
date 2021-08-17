class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList_Stack:

    def __init__(self, items=None):
        
        self.head = None

        if items is not None:
            for i in items:                         # iterates list

                if self.head is None:           # if list is empty
                    new_node = Node(i, None)
                    self.head = new_node

                else:                           # if not empty, inserts list data at the end
                    n = self.head
                    while n.next:

                        n = n.next

                    n.next = Node(i, None)

    def printStack(self):

        if self.head is None:
            print('Stack is empty')
            return

        n = self.head
        final = ''
        
        while n:
            
            if n.next is not None:
                final += str(n.data) + ' , '   # prints data on on present address
            
            else:                               # doesnt print '->' if last element
                final += str(n.data)        
            n = n.next                          #  goes to the referred address

        final = '[' + final + ']'
        print(final)

    def push(self, item):

        new_node = Node(item, self.head)
        self.head = new_node

class Stack:

    def __init__(self):
        
        self.stack = []

    def push(self, item):

        self.stack += [item]

    def pop(self):

        self.stack = self.stack[:-1]

    def peek(self):

        return self.stack[-1]

    def printStack(self):

        return self.stack

source = [1,2,3,4]

stk = Stack()
stk.push(0)
stk.push(1)
stk.pop()
stk.printStack()
print(stk.peek())