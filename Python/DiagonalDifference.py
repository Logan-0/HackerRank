# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    # Init Vars
    diagOne = 0
    diagTwo = 0
    length = len(arr)

    # for each value in the row
    for i in range(length):

        # add the ith row &&&& ith column.
        # creates downward diagonal to the right
        #[x00][ 01][ 02]
        #[ 10][x11][ 12]
        #[ 20][ 21][x22]
        diagOne += arr[i][i]

        # add the ith row &&&& (length of the array -1 to start from the end) - ith column.
        # creates upward diagonal to the left
        #[ 00][ 01][x02]
        #[ 10][x11][ 12]
        #[x20][ 21][ 22]
        diagTwo += arr[i][(length-1)-i]

    #Check for correct values
    print("Diag One: "+str(diagOne))
    print("Diag Two: "+str(diagTwo))
    
    #Return difference and if it goes negative use math package to return absolute value
    sum=abs(diagOne-diagTwo);
    return sum