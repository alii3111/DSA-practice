# given list below sort this list in an ascending order
# list_a = [6,3,7,1,9,2]

def selection_sort(list_a):
    size = len(list_a) -1
    for i in range(size):
        min_value = i

        for j in range (i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
         
        if min_value !=i:
            list_a[i], list_a[min_value]=list_a[min_value], list_a[i]

    return list_a
print(selection_sort([6,3,7,1,9,2]))