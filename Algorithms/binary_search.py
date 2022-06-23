def binary_search(array, item):

    start = 0
    end = len(array) - 1

    while start <= end:

        mid = (start + end) // 2

        if item == array[mid]:
            return mid

        elif item > array[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return None

my_list = [1,2,3,4,5,6]

print(binary_search(my_list, 6))