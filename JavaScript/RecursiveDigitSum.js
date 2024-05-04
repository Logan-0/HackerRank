// We define super digit of an integer x using the following rules:

// Given an integer, we need to find the super digit of the integer.

// If x has only 1 digit, then its super digit is x.
// Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

function superDigit(n, k) {
    // # if the length of the number string is 1 like just entering '1'
    // # return the number
    const inputLength = n.length
    const chars = n.split("")
    
    if (inputLength == 1) {
        return n
    }
    var arr = []
    // Go through each convert to a number and add to the list
    for (let i=0; i < inputLength; i++) {
        var el = parseInt(chars[i])
        arr.push(el)
    }
    
    // Sum the new array of values
    var newValue = 0
    for(let j=0; j < arr.length; j++) {
        newValue += arr[j]
    }
    // Multiply by K value
    newValue *= k
    
    // Convert to string for recursive use of function
    const finalString = String(newValue)

    // Only 1 is the k value since no more user input
    // call the function again for recursive finish
    return superDigit(finalString, 1)
        
}
export { superDigit }