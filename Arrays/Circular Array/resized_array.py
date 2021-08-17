#resizing a circular array

def resize(circ,start,size, resize):

    resizedCirc=[0]*(len(circ) + resize)

    index_circ=start

    index_resizedCirc=start

    for i in range(size):

      resizedCirc[index_resizedCirc] = circ[index_circ]

      index_resizedCirc = (index_resizedCirc+1) % len(resizedCirc)
      index_circ = (index_circ+1) % len(circ)

    return resizedCirc



circ=[20,30,40,50,10] #creating a circular array with start 4 and size 5

circ=resize(circ,4,5,3) 

print(circ)