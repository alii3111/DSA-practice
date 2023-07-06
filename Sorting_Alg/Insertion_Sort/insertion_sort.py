# using insertion sort, sort the following list in asscending order
# list_a = [4,2,7,9,1,3]

def insertion_sort(list):
    for i in range(1, len(list)):
        values_to_sort = list[i]
        while list[i-1] > values_to_sort and i > 0:
            list[i-1], list[i] = list[i], list[i-1]
            i = i-1
    print(list)
    return list
    list_a = [4,2,7,9,1,3]
insertion_sort(list_a)