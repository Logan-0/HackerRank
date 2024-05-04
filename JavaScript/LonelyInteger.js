// Given an array of integers, where all elements but one occur twice, find the unique element.

function lonelyInteger(a) {

    var unique = 0
    
    // # This one has a rough solution placed out and for the future I will always keep reference.
    // # This one line to find a unique within integers is the best solution for this situation.
    a.forEach((element) => unique^=element)

    return unique
}
export {lonelyInteger}