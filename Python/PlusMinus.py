# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal.

def plusMinus(arr):
    
    # Set init variables
    pos = 0
    neg = 0
    zero = 0
    arrayLength = len(arr)

    # for each item in the length of the array
    for i in range(arrayLength):

        # If positive;increment
        if arr[i] > 0:
            pos+=1

        # If negative;increment
        elif arr[i] < 0:
            neg+=1

        # If negative;increment
        else:
            zero+=1
    # Return the values

    return ("Ratio of Positive Numbers: " + str(pos/arrayLength) + "\n"
            +"Ratio of Negative Numbers: " + str(neg/arrayLength) + "\n"
            +"Ratio of Zero to Other Numbers: " + str(zero/arrayLength) + "\n")
