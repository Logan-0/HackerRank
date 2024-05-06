# // Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

def isBalanced(s):
    braks = []
    for i in range(len(s)):
        if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
            braks.append(s[i])
        elif (s[i] == ']'):
            possBracket = braks.pop()
            if (possBracket != '['):
                return "NO"
            
        elif (s[i] == ')'):
            possBracket = braks.pop()
            if (possBracket != '('):
                return "NO"

        elif (s[i] == '}'):
            possBracket = braks.pop()
            if (possBracket != '{'):
                return "NO"

    return "YES"