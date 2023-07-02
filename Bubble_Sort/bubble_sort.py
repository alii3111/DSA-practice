# list = [12,8,3,1,6,4]
# sort this list in an ascending order using bubble sort

def bubble_sort(list):
    size = len(list) - 1
    sorted = False

    steps = 0
    while not sorted:
        sorted = True
        for i in range(size):
            steps+=1
            if list[i] > list[i + 1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    print(list)
    print(steps)
list = [12,8,3,1,6,4]

bubble_sort(list)