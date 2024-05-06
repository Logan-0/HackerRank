// Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

function isBalanced(s) {

    var braks = []

    for (let i =0; i < s.length; i++) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
            braks.push(s[i])
        } else if (s[i] == ']') {
            const possBracket = braks.pop()
            if (possBracket != '[') {
                return "NO"
            } 
        } else if (s[i] == ')') {
            const possBracket = braks.pop()
            if (possBracket != '(') {
                return "NO"
            } 
        } else if (s[i] == '}') {
            const possBracket = braks.pop()
            if (possBracket != '{') {
                return "NO"
            } 
        }
    };

    return "YES"
}

export { isBalanced }