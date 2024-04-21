# If given a square matrix is the matrix sorted [a][b][c]
# left to right -> ascending                    [d][e][f]
# ascending as a column going down              [g][h][i]
# if not can they be sorted this way

def gridChallenge(grid):
    # first sort each row within the matrix.
    # string comprehension uses sorted method on row for each row(array) in the grid
    letters = [sorted(row) for row in grid]
    
    # create columns as a list
    # cast columns as a list for each column in letters
    # we use the unpacking operator '*' to unzip the columns from the sorted grid
    columns = [list(columns) for columns in zip(*letters)]

    # for each column in columns;                           for col in columns
    # if the original sort in the first statement;          col==sorted(col)

    # made each value sorted in column form also sorted; so if column is == to the sorted column from the original sort
    # return YES if else NO             
    if all(col==sorted(col) for col in columns):
        return "YES"
    else:
        return "NO"