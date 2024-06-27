// # Julius Caesar protected his confidential information by encrypting it using a cipher. 
// # Caesar's cipher shifts each letter by a number of letters. 
// # If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
// # In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

function caesarCipher(s, k) {
    // # Init vars
    var output = ""

    // # for each char letter in the string
    for (let i =0; i < s.length; i++) {

        // # get the ascii value and get a temp char ready
        var numVal = s.charCodeAt(i)
        var newChar = ""

        // # if the letter is 65 > x < 90 its lowercase
        if (numVal >= 65 && numVal <= 90) {

            // # if the shift value makes the letter a symbol
            // # subtract or add the alphabet length to shift to the start or end of the alphabet string
            // # set the newChar = char(incrementVal(k) + asciiValue(numVal))
            if ((numVal + k) > 90) {
                k -= 26
                newChar = String.fromCharCode(numVal + k);
            } else if ((numVal + k) < 65) {
                k += 26
                newChar = String.fromCharCode(numVal + k)
            } else {
                newChar = String.fromCharCode(numVal + k)
            }

            // # if the letter is 97 > x < 122 its uppercase
        } else if (numVal >= 97 && numVal <= 122) {

            if ((numVal + k) > 122) {
                k -= 26
                newChar = String.fromCharCode(numVal + k);
            } else if ((numVal + k) < 97) {
                k += 26
                newChar = String.fromCharCode(numVal + k);
            } else {
                newChar = String.fromCharCode(numVal + k)
            }

        } else {
            // # if not an alphancharacter originally don't shift just add it to the end
            newChar = String.fromCharCode(numVal)
        }

        output += newChar
    }
    return "Original: " + s + "\nCipher: " + output
}
export { caesarCipher }