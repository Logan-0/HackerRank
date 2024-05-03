import { miniMaxSum } from "./MiniMaxSum.js"
import {plusMinus} from "./PlusMinus.js"
import {timeConversion} from "./TimeConversion.js"

function testingFunction() {

    // # Generic Small Test Array, All values unique, containes pos and neg
    const smallTestArray = [-987, 123, 7, 17, 26, -1, -759, 0]

    // # Large Test Array
    const largeTestArray = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]

    // # Pyramid Small Test Array, unique is 7, pos and neg values
    const smallDuplicateValueArray = [-999, -999, -999, 999, 999, 999, -42, -42, 11, 11, 7]

    // # Time String [00:00:00PM]
    const timeString = "07:05:45PM"

    // # Small Square Matrix
    const smallSquareMatrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    // # 2 Length Array
    const twoTwoDoubleArray = [2, 2]
    const oneFourDoubleArray = [1, 4]

    // # AlphaSymbolString
    const alphaSymbolTestString = "Peppermint-Question"

    // # Alphabetgrid len(grid)=5, height(grid)=5
    const alphabetGrid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

    const plusMinusResult = plusMinus(smallTestArray)
    console.log("Testing PlusMinus.js: \n", plusMinusResult)
    console.log()


    const miniMaxSumResult = miniMaxSum(smallTestArray)
    console.log("Testing MiniMaxSum.js: \n", "Min: " + miniMaxSumResult[0] + " Max: " + miniMaxSumResult[1])
    console.log()


    const timeConversionResult = timeConversion(timeString)
    console.log("Testing TimeConversion.js: \n",timeConversionResult)
    console.log()
}

testingFunction()