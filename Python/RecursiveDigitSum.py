# // We define super digit of an integer x using the following rules:

# // Given an integer, we need to find the super digit of the integer.

# // If x has only 1 digit, then its super digit is x.
# // Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

def superDigit(n, k):
    # if the length of the number string is 1 like just entering '1'
    # return the number
    inputLength = len(n)
    
    if inputLength == 1:
        return n
    # This is big part; in digits store ->
    # string(n) converted to a list to seperate chars in the string
    # and use the map function to convert them all to integers.
    digits = map(int, list(n))
    
    # sum the digits
    newValue = sum(digits)
    
    # Add as many of those as listed
    newValue *= k
    
    # convert to string for recursive use of function
    finalString = str(newValue)

    # Just return it with k=1 as we don't add any more through this method after.    
    return superDigit(finalString, 1)
        