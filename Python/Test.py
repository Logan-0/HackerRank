from PlusMinus import plusMinus
from MiniMaxSum import miniMaxSum
from TimeConversion import timeConversion
from LonelyInteger import lonelyInteger
from DiagonalDifference import diagonalDifference

# Generic Small Test Array, All values unique, containes pos and neg
smallTestArray = [-987, 123, 7, 17, 26, -1, -759, 0]

# Pyramid Small Test Array, unique is 7, pos and neg values
smallDuplicateValueArray = [-999, -999, -999, 999, 999, 999, -42, -42, 11, 11, 7]

# Time String [00:00:00PM]
timeString = "07:05:45PM"

# Small Square Matrix
smallSquareMatrix = [[11, 2, 4], [4, 5, 6], [10,8,-12]]

if __name__ == "__main__":
    
    plusMinusResult = plusMinus(smallTestArray)
    print("Testing PlusMinus.py: \n",plusMinusResult)
    print()

    miniMaxSumResult = miniMaxSum(smallTestArray)
    print("Testing MiniMaxSum.py: \n",miniMaxSumResult)
    print()

    timeConversionResult = timeConversion(timeString)
    print("Testing TimeConversion.py: \n",timeConversionResult)
    print()

    lonelyIntegerResult = lonelyInteger(smallDuplicateValueArray)
    print("Testing LonelyInteger.py: ",lonelyIntegerResult)
    print()

    diagonalDifferenceResult = diagonalDifference(smallSquareMatrix)
    print("Testing DiagonalDifference.py: ",diagonalDifferenceResult)


