from NewYearChaos import minimumBribes
from PlusMinus import plusMinus
from MiniMaxSum import miniMaxSum
from TimeConversion import timeConversion
from LonelyInteger import lonelyInteger
from DiagonalDifference import diagonalDifference
from CountingSort import countingSort
from TowerBreakers import towerBreakers
from CaesarCipher import caesarCipher
from GridChallenge import gridChallenge
from RecursiveDigitSum import superDigit

# Generic Small Test Array, All values unique, containes pos and neg
smallTestArray = [-987, 123, 7, 17, 26, -1, -759, 0]

# Small Seq Array for when the numbers must be contained or related
smallSeqArray = [1,4,5,3,2,6]

# Large Test Array
largeTestArray = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]

# Pyramid Small Test Array, unique is 7, pos and neg values
smallDuplicateValueArray = [-999, -999, -999, 999, 999, 999, -42, -42, 11, 11, 7]

# Time String [00:00:00PM]
timeString = "07:05:45PM"

# Small Square Matrix
smallSquareMatrix = [[11, 2, 4], [4, 5, 6], [10,8,-12]]

# 2 Length Array
twoTwoDoubleArray=[2, 2]
oneFourDoubleArray=[1, 4]

# AlphaSymbolString
alphaSymbolTestString = "Peppermint-Question"

#alphabetgrid len(grid)=5, height(grid)=5
alphabetGrid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']


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
    print()

    countingSortResult = countingSort(largeTestArray)
    print("Testing CountingSort.py: \n",countingSortResult)
    print()

    towerBreakersResult1 = towerBreakers(twoTwoDoubleArray[0], twoTwoDoubleArray[1])
    towerBreakersResult2 = towerBreakers(oneFourDoubleArray[0], oneFourDoubleArray[1])
    print("Testing TowerBreakers.py: \n Result1: ",towerBreakersResult1," Result2: ",towerBreakersResult2)
    print()

    caesarCipherResult = caesarCipher(alphaSymbolTestString, 7)
    print("Testing CaesarCipher.py: ",caesarCipherResult)
    print()

    gridChallengeResult = gridChallenge(alphabetGrid)
    print("Testing GridChallenge.py: ",gridChallengeResult)
    print()

    superDigitResult = superDigit('9875', 4)
    print("Testing RecursiveDigitSum.py: ",superDigitResult)
    print()

    minimumBribesResult = minimumBribes(smallSeqArray)
    print("Testing NewYearChaos.py: ", minimumBribesResult)
    print()