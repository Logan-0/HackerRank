# Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyInteger(a):
    # Init Vars
    total = len(a)
    unique = 0
    
    # This one frankly has a rough solution placed out and for the future I will always keep reference.
    # This one line to find a unique within integers is the best solution for this situation.
    for i in range(total):
        unique^=a[i]
    
    return unique