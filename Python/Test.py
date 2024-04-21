from PlusMinus import plusMinus
from MiniMaxSum import miniMaxSum
from TimeConversion import timeConversion
from LonelyInteger import lonelyInteger

# Generic Small Test Array, All values unique, containes pos and neg
smallTestArray = [-987, 123, 7, 17, 26, -1, -759, 0]

# Pyramid Small Test Array, unique is 7, pos and neg values
smallDuplicateValueArray = [-999, -999, -999, 999, 999, 999, -42, -42, 11, 11, 7]

# Time String [00:00:00PM]
timeString = "07:05:45PM"

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

    


