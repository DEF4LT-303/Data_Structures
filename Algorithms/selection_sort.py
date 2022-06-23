def selection_sort(a):

  for index in range(len(my_list)):

    min_val = index

    for j in range(index+1, len(my_list)):
        if my_list[j] < my_list[min_val]:

            min_val = j

    my_list[min_val], my_list[index] = my_list[index], my_list[min_val]
      


my_list=[2,3,4,1,6]

selection_sort(my_list)

print(my_list)