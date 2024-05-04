// # If given a square matrix is the matrix sorted [a][b][c]
// # left to right -> ascending                    [d][e][f]
// # ascending as a column going down              [g][h][i]
// # if not can they be sorted this way

function gridChallenge(grid) {
    // # first sort each row within the matrix.
    // The Grid is a list of list items. Knowing this, we get each list
    // Within each list divide those items using split("") then sort()
    // return temp
    var sortedGrid = grid.map(item => {
        let temp = item.split("").sort()
        return temp;
    })

    // For each (i or column) go through each (row or j) and grab the value.
    // This builds a column each time then we push to list 
    for(let column = 0; column<sortedGrid.length; column++){
        for(let row = 0; row<sortedGrid.length-1; row++){
            if (sortedGrid[row][column] > sortedGrid[row+1][column]) {
                return "NO"
            }
        }
    }
    return "YES"
}
export { gridChallenge }