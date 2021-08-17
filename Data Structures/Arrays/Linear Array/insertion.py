#array insertion

def insert(s, index, value, size):

  if size == len(s):

    print('No space in array!')
    return

  if index < 0 or index > size:

    print('Wrong Index!')
    return

  for i in range(size, index, -1):

    s[i] = s[i-1]

  s[index] = value

source = [10, 20, 30, 40, 50, 0, 0, 0]
insert(source, 4, 200, 5)

print(source)