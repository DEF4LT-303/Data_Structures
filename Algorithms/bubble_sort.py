def bubble_sort(a):

  for i in range(len(a)-1,-1,-1):

    for j in range(0,i):

      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]

        
my_list=[10,1,20,3,6,2,5,11,15,2,12,14,17,18,29]   
bubble_sort(my_list)
print(my_list)