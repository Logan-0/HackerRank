# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. 
# If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

def caesarCipher(s, k):
    # Init vars
    output = ""

    # for each char letter in the string
    for char in s:

        # get the ascii value and get a temp char ready
        numVal = ord(char)
        newChar = ""

        # if the letter is 65 > x < 90 its lowercase
        if (numVal > 65 and numVal < 90):
            # if the shift value makes the letter a symbol
            # subtract or add the alphabet length to shift to the start or end of the alphabet string
            # set the newChar = char(incrementVal(k) + asciiValue(numVal))
            if (numVal + k) > 90:
                k-=25
                newChar = chr(numVal+k);
            elif (numVal + k) < 65:
                k+=25
                newChar = chr(numVal+k)
            else:
                newChar = chr(numVal+k)

        # if the letter is 97 > x < 122 its uppercase
        elif ( numVal > 97 and numVal < 122):
            if (numVal + k) > 122:
                k-=25
                newChar = chr(numVal+k);
            elif (numVal + k) < 97:
                k+=25
                newChar = chr(numVal+k);
            else:
                newChar = chr(numVal+k)
        
        # if not an alphancharacter originally don't shift just add it to the end
        else:
            newChar = chr(numVal)
        output += newChar

    return output