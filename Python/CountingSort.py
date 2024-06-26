# Quicksort usually has a running time of (n x log(n)), but is there an algorithm that can sort even faster?
# In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another.
#  A comparison sort algorithm cannot beat (n x log(n)) (worst-case) running time, since (n x log(n)) represents the minimum number of comparisons needed to know where to place each element.

def countingSort(arr):
    # create an array using string comprehension of only the value '0', 100 times.
    array = [0 for element in range(100)]
    
    # for each value in the array param
    for x in range(len(arr)):

        # increment the value in the array
        # e.g. [0, 1, 2, 1, 2, 3] makes values in new array 
        # = [1 (There exists one zero), 2 ( There exists two ones), 2 (There exists two twos), 1 (There exists one three)] = [1,2,2,1]
        val = arr[x]
        array[val] += 1
    return array