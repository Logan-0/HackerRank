// There is a given list of strings where each string contains only lowercase letters from [a-j], inclusive. The set of strings is said to be a GOOD SET if no string is a prefix of another string. In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.

function noPrefix(words) {
    const length = words[0]
    words = words.splice(1,words.length)
    words.sort((a, b) => a.length - b.length);

    for (let i = 0; i < length; i++){
        let temp = words[i]
        for (let j=1; j < length; j++) {
            if (temp === words[j].substring(0, temp.length)) {
                console.log("BAD SET")
                console.log(words[j])
                return
            }
        }
    }

    console.log("GOOD SET")
}

export {noPrefix}