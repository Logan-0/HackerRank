

def legoBlocks(height, width):

    MOD = 1000000007
        
    # The number of combinations to build a single row
    row_combinations = [1, 1, 2, 4]
    
    # Build row combinations up to this wall's width
    # if row shorter than or equal to width
    # sum the values and append to the end the sum of the list
    # otherwise don't worry about it

    while len(row_combinations) <= width:
        row_combinations.append(sum(row_combinations[-4:]) % MOD)
    
    # W/O List Comprehension
    # let summation = 0
    # while(row_combinations.length <= width) || (m) {
    #   summation += row_combinations[-4:]
    #   row_combinations.append(summation % MOD)
    #}
    
    
    # Compute total combinations for constructing a wall of height N of varying widths
    # W/O List Comprehension
    # let total = [0,0,0,0]
    # row_combinations.array.forEach((element) => {
    #   sum += (element^height) % MOD
    #})
    total = [pow(c, height, MOD) for c in row_combinations]
    # total = [(c^height%MOD),(c^height%MOD),(c^height%MOD),(c^height%MOD),?(c^height%MOD)]
    # may be 4 or 5 values depending on wall width
    
    # Find the number of unstable wall configurations for a wall of height (n) of varying widths
    # Unstable defined as
    unstable = [0, 0]
    
    # For each from 2 -> width + 1
    # for each in range(1 -> i)
    for i in range(2, width + 1):
            # THIS RIGHT HERE IS THE PART I NEEDED TO LOOK UP
            # THIS IS REVERSE ENGINEERING AN ALGORITHM OR FORMULA
            # Subtract then Multiply
            # Sum from previous
            # MOD OP
        unstable.append(sum((total[j] - unstable[j]) * total[i - j] for j in range(1, i)) % MOD)
    
    
    # Print the number of stable wall combinations
    print((total[width] - unstable[width]) % MOD)