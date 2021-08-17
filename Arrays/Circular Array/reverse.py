def printForward(c,start,size):

  for i in range((size+start)-1, start-1, -1): # starting from last index (12) to first (8)

    idx = i % len(c)  # handle array out of range
    print(c[idx])
    # print(i)


circularArray=[40,50,0,0,0,0,0,0,10,20,30] #creating a circular array with start 8 and size 5

printForward(circularArray,8,5)
