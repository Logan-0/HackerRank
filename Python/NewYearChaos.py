# It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
# Each person wears a sticker indicating their initial position in the queue from 1 to n.
# Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker.
# One person can bribe at most two others.

# Determine the minimum number of bribes that took place to get to a given queue order.
# Print the number of bribes, or, if anyone has bribed more than two people, print "Too chaotic".

def minimumBribes(q):
    # Set Vars
    bribes = 0
    
    # Start Example
    # [2, 1, 5, 3, 5]
    #  0  1  2  3  4
    
    # First Pass
    # Start from the back. if 5 i starts at 4 (len - 1)
    for i in range(len(q)-1, -1, -1):
        
        # Check for anything too far up
        if q[i] - (i + 1) > 2:
            return print('Too chaotic')
        
        # For each element in range of
        # Max between 0 < value < q[i]-2 = q[2] = 5
        # In example commented this is range max(0, 2)
        # e.g. for each from 5 -> (i=4)
        # if q
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
                
    return bribes