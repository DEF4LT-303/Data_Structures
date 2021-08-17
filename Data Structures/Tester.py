import LinkedList as LinkedList
import Stack as Stack

print('Linked List:')
print('==============================')
#-----------------------------------#
first = LinkedList.LinkedList()
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

print('\n==============================')
print('Stack:')
print('==============================')
#-----------------------------------#
stk = Stack.Stack()
stk.push(0)
stk.push(1)
stk.printStack()
