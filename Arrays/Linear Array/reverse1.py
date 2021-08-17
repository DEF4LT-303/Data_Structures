#reversing an array: out of place

def reverse(source):

    final = [0]*len(source)

    i = 0
    j = len(source) - 1

    for x in range(len(source)):

      final[i] = source[j]

      i += 1
      j -= 1

    return final



a=[10,20,30,40,50]

b=reverse(a)

print(b)