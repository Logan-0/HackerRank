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
