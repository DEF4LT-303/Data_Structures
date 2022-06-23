def insertion_sort(a):

    for i in range(len(a)):

        for j in range(i-1, -1, -1):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

            else:
                break

my_list=[2,3,4,1,6,-1]

insertion_sort(my_list)

print(my_list)