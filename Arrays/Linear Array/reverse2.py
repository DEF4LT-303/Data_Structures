#reversing an array: in place

def reverse(source):

    i = 0
    j = len(source) - 1

    for x in range(len(source)//2):

      temp = source[i]
      source[i] = source[j]
      source[j] = temp

      i += 1
      j -= 1

    
    return source


a=[10,20,30,40,50]

print(reverse(a))
