# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

import math

def miniMaxSum(arr):

    # Initialize vars
    total = len(arr)
    max = -math.inf
    min = math.inf

    # Sort the array
    arr.sort()

    # For each number in the array
    for i in range(total):

        # if it is the new largest compared to the old. update
        if arr[i] > max:
            max = arr[i]

        # if it is the new smallest compared to the old. update
        if arr[i] < min:
            min = arr[i]
    
    # add together the elements leaving out the least effective item e.g. finding the most doesn't need the lowest number, and vice versa
    highest = 0
    lowest = 0
    
    for i in range(4):
        lowest += arr[i]
        highest += arr[-i-1]
        
    return "Least Possible Number: " + str(lowest) + ", Highest Possible Number: " + str(highest)