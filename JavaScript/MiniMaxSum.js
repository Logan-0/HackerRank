// Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
// Then print the respective minimum and maximum values as a single line of two space-separated long integers.

function miniMaxSum(arr) {
    
    // Initialize
    var min = 0;
    var max = 0;
    
    // Sort the Array
    arr.sort(function(a, b){return a-b})

    // Loop short of the end to get the minimum sum
    for(let i=0; i < arr.length-1; i++) {
        min += arr[i]
        max += arr[i+1]
    }
    
    const list = [min,max]
    return list
}

export {miniMaxSum}