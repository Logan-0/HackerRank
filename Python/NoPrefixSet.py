# // There is a given list of strings where each string contains only lowercase letters from [a-j], inclusive. The set of strings is said to be a GOOD SET if no string is a prefix of another string. In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.

def noPrefix(words):
    length = int(words[0])
    words = words[1:len(words)]
    words.sort();

    for i in range(length):
        temp = words[i]
        for j in range(1, length):
            if (temp == words[j][0:len(temp)]):
                print("BAD SET")
                print(words[j])
                return
        
    print("GOOD SET")
    return