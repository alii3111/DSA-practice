# using insertion sort, sort the following list in asscending order
# list_a = [4,2,7,9,1,3]

def insertion_sort(list):
    for i in range(1, len(list)):
        values_to_sort = list[i]