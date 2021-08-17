def circularize(linear,start,size):

    circular=[0]*len(linear)

    index=start

    i=0

    for i in range(size):

      circular[index] = linear[i]

      index = (index+1)%len(circular)

    return circular

source=[10,20,30,40,50,0,0]
print(circularize(source,4,5))