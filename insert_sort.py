def insertion_sort(array):
    for index in range(1, len(array)): #loop beginning from index 1 through the entire array , j goes from 1 entire array
        j = array[index] # save "lifted value" to a variable
        i = index -1

        while i >= 0: #as long a the valus of i is NOT negative
            if array[i] > j: # if the left value is greater than the temp value --- do
                array[i + 1] = array[i] #shift left value one to the right
                i = i - 1 # decrement index of left value to compare the next left value against the current value of temp
            else: 
                break #if we encounter a value at left of j that is greater or equal to the temp value, end pass through using break
        array [i + 1] = j # move the j value into the vacated index
    return array
#driver code
array = [4,2,7,1,3]
print(insertion_sort(array))

#thought process -----
"""
***1st pass through***
temp at index = 1, value = 2
left of temp, index = 0, value = 4

as long as left is NOT negative -- do the comparisons
if left value is greater than the temp value "lifted value" shift the left value one to the right


"""