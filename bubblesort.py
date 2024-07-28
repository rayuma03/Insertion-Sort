def bubble_sort(list):
    unsorted_until_index = len(list) - 1 #final index of the array, keeps track of the rightmost index that has not been sorted
    sorted = False #array initially unsorted

    while not sorted:
        sorted = True #assume the array i sorted
        for i in range(unsorted_until_index):
            if list[i] > list [i+1]:
                list[i],list[i+1] = list[i+1],list[i] #swap
                sorted = False #after a swap is encountered change the variable back to False
        unsorted_until_index = unsorted_until_index -  1
    return list

print(bubble_sort([65,75,55,45,35,25,15,10]))
