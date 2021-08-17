#right rotating an array by one place

def rightRotate(source):

    temp = source[len(source)-1]
    for i in range(len(source)-1, 0, -1):

      source[i] = source[i-1]

    source[0] = temp

a=[10,20,30,40,50, 0, 0, 0]

rightRotate(a)

print(a)
