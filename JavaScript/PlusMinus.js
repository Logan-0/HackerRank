// Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
// Print the decimal value of each fraction on a new line with 6 places after the decimal.

function plusMinus(arr) {
    const length = arr.length
    var pos = 0
    var neg = 0
    var zero = 0
    for(let i =0; i < length; i++) {
        if (arr[i] < 0) {
            neg +=1;
        } else if (arr[i] > 0) {
            pos +=1;
        } else {
            zero +=1;
        }
    }
    const arra = ["Positive Ratio: " + (pos/length), "Negative Ratio: " + (neg/length), "Zero Ratio: " + (zero/length)]

    return arra;
}

export {plusMinus}