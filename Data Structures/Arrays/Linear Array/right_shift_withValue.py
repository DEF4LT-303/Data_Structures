#right shifting an array by k places

def rightShift(source,k):

  for i in range(len(source)-1, k-1, -1):

    source[i] = source[i-k]

  for i in range(k):

    source[i] = 0


a=[10,20,30,40,50]

rightShift(a, 3)

print(a)
