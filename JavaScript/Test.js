import { miniMaxSum } from "./MiniMaxSum.js"
import { plusMinus } from "./PlusMinus.js"
import { timeConversion } from "./TimeConversion.js"
import { lonelyInteger } from "./LonelyInteger.js"
import { diagonalDifference } from "./DiagonalDifference.js"
import { countingSort } from "./CountingSort.js"
import { towerBreakers } from "./TowerBreakers.js"
import { caesarCipher } from "./CaesarCipher.js"
import { gridChallenge } from "./GridChallenge.js"
import { superDigit } from "./RecursiveDigitSum.js"
import { minimumBribes } from "./NewYearsChaos.js"
import { mergeLists } from "./MergeTwoSortedLinkedLists.js"

function testingFunction() {

    // # Generic Small Test Array, All values unique, containes pos and neg
    const smallTestArray = [-987, 123, 7, 17, 26, -1, -759, 0]

    // # Small Seq Array for when the numbers must be contained or related
    const smallSeqArray = [1, 4, 5, 3, 2, 6]

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


    // SINGLE LINKED LIST SETUP
    // SINGLE LINKED LIST SETUP
    // SINGLE LINKED LIST SETUP
    const SinglyLinkedListNode = class {
        constructor(nodeData) {
            this.data = nodeData;
            this.next = null;
        }
    };

    const SinglyLinkedList = class {
        constructor() {
            this.head = null;
            this.tail = null;
        }

        insertNode(nodeData) {
            const node = new SinglyLinkedListNode(nodeData);

            if (this.head == null) {
                this.head = node;
            } else {
                this.tail.next = node;
            }

            this.tail = node;
        }
    };

    // Singly Linked List 1 & 2
    var llist1 = new SinglyLinkedList();
    const llist1Item1 = 1
    const llist1Item2 = 2
    const llist1Item3 = 3
    llist1.insertNode(llist1Item1)
    llist1.insertNode(llist1Item2)
    llist1.insertNode(llist1Item3)

    var llist2 = new SinglyLinkedList();
    const llist2Item1 = 2
    const llist2Item2 = 4
    const llist2Item3 = 6
    llist2.insertNode(llist2Item1)
    llist2.insertNode(llist2Item2)
    llist2.insertNode(llist2Item3)

    // SINGLE LINKED LIST SETUP END
    // SINGLE LINKED LIST SETUP END
    // SINGLE LINKED LIST SETUP END


    const plusMinusResult = plusMinus(smallTestArray)
    console.log("Testing PlusMinus.js: \n", plusMinusResult)
    console.log()


    const miniMaxSumResult = miniMaxSum(smallTestArray)
    console.log("Testing MiniMaxSum.js: \n", "Min: " + miniMaxSumResult[0] + " Max: " + miniMaxSumResult[1])
    console.log()


    const timeConversionResult = timeConversion(timeString)
    console.log("Testing TimeConversion.js: \n", timeConversionResult)
    console.log()


    const lonelyIntegerResult = lonelyInteger(smallDuplicateValueArray)
    console.log("Testing LonelyInteger.js: \n", lonelyIntegerResult)
    console.log()


    const diagonalDifferenceResult = diagonalDifference(smallSquareMatrix)
    console.log("Testing DiagonalDifference.js: \n", diagonalDifferenceResult)
    console.log()


    const countingSortResult = countingSort(largeTestArray)
    console.log("Testing CountingSort.js: \n", countingSortResult)
    console.log()

    const towerBreakersResult1 = towerBreakers(twoTwoDoubleArray[0], twoTwoDoubleArray[1])
    const towerBreakersResult2 = towerBreakers(oneFourDoubleArray[0], oneFourDoubleArray[1])
    console.log("Testing TowerBreakers.js: \n Result1: ", towerBreakersResult1, " Result2: ", towerBreakersResult2)
    console.log()

    const caesarCipherResult = caesarCipher(alphaSymbolTestString, 7)
    console.log("Testing CaesarCipher.js: \n", caesarCipherResult)
    console.log()


    const gridChallengeResult = gridChallenge(alphabetGrid)
    console.log("Testing GridChallenge.js: \n", gridChallengeResult)
    console.log()


    const superDigitResult = superDigit('9875', 4)
    console.log("Testing RecursiveDigitSum.js: \n", superDigitResult)
    console.log()


    const minimumBribesResult = minimumBribes(smallSeqArray)
    console.log("Testing NewYearChaos.js: ", minimumBribesResult)
    console.log()


    const mergeListsResults = mergeLists(llist1, llist2)
    console.log("Testing MergeTwoSortedLinkedLists.js: ", mergeListsResults)
    console.log()



}

testingFunction()