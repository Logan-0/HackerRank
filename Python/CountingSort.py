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