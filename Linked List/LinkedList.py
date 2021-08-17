import Node as Node

class LinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):

        node = Node.Node(data, self.head)   # create obj with previrous address refference
        self.head = node                    # assign node to head

    def append(self, data):

        if self.head is None:               # if list is empty, creates nodes
            node = Node.Node(data, None)    
            self.head = node                # assigns created node to head
            return

        n = self.head
        while n.next:                       # iterates through the list until next is null

            n = n.next

        n.next = Node.Node(data, None)
    
    def printList(self):

        if self.head is None:
            print('Linked list is empty')
            return

        n = self.head
        final = ''
        while n:
            
            if n.next is not None:
                final += str(n.data) + ' -> '   # prints data on on present address
            
            else:                               # doesnt print '->' if last element
                final += str(n.data)        
            n = n.next                          #  goes to the referred address


        print(final)
        print('Length of list ->', self.node_counter())

    def node_counter(self):

        count = 1
        current = self.head
        
        if current is None:
            return 0
            
        while current.next is not None:

            current = current.next
            count += 1

        return count

    def remove(self, index):

        if index < 0 or index > self.node_counter():
            print('Invalid Index!')

        elif index == 0:
            self.head = self.head.next

        else:
            count = 0
            n = self.head

            while n:

                if count == index - 1:
                    n.next = n.next.next

                    break

                n = n.next
                count += 1

    def remove_value(self, deleteKey):

        n = self.head
        index = 0
        while n.data != deleteKey:        # finds the index of value to be removed

            index += 1
            n = n.next

        value = None
        if index == 0:
            value = self.head.data
            self.head = self.head.next

        count = 0
        n = self.head
        while n:

            if count == index - 1:          # stops before the value to be removed
                value = n.next.data           # stores deleted value
                n.next = n.next.next          # updates address of deleted value to next address

                break
            
            count += 1
            n = n.next
        print('Deleted Value: ', value)

    def add_list(self, lst):

        self.head = None

        for element in lst:

            if self.head is None:

                new_node = Node.Node(element, None)
                self.head = new_node
            
            else:

                n = self.head
                while n.next:

                    n = n.next

                n.next = Node.Node(element, None)

#----------------Tester---------------#

first = LinkedList()
first.append(5)
first.append(9)
first.append(6)
first.append(9)
first.prepend(69)
first.prepend(96)
first.remove(2)
first.remove_value(96)

first.printList()

lst = [1,2,3]

first.add_list(lst)
first.printList()