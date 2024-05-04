// Given a square matrix, calculate the absolute difference between the sums of its diagonals.

function diagonalDifference(arr) {

    var diagOne = 0
    var diagTwo = 0
    var length = arr.length

    // # for each value in the row
    for (let i = 0; i < length; i++) {

        // # add the ith row &&&& ith column.
        // # creates downward diagonal to the right
        // #[x00][ 01][ 02]
        // #[ 10][x11][ 12]
        // #[ 20][ 21][x22]
        diagOne += arr[i][i]

        // # add the ith row &&&& (length of the array -1 to start from the end) - ith column.
        // # creates upward diagonal to the left
        // #[ 00][ 01][x02]
        // #[ 10][x11][ 12]
        // #[x20][ 21][ 22]
        diagTwo += arr[i][(length-1)-i]
    }

    
    // #Return difference and if it goes negative use math package to return absolute value
    const sum = "\n Diagonal One: " + diagOne + "\n Diagonal Two: " + diagTwo + "\n Difference of: " + Math.abs(diagOne-diagTwo);
    return sum

}
export {diagonalDifference}