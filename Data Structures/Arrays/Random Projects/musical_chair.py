import random

def musical_chair():

    names = []

    for i in range(1, 8):

        name = input(f'Enter name {i}: ')
        names.append(name)

    length = 7
    while (length != 1):                  # loop runs till 1 player left

        random_num = random.randint(0, 3)
        delete = int(length/2)

        if random_num == 1:               # sets middle value to 0 and decreases length
            names[delete] = 0
            length -= 1

        else:                             # right-shifts for rotation
            temp = names[length-1]        

            for i in range(length-1, 0, -1):

                names[i] = names[i-1]

            names[0] = temp

        for i in range(length):           # sorts all the 0s to the right

            if names[i] == 0:
                temp = names[i+1]
                names[i+1] = names[i]
                names[i] = temp

        print('Random number = ', random_num)
        print(names)
           
    print(names[0])
        
musical_chair()