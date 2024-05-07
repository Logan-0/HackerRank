// Implement a simple text editor. The editor initially contains an empty string, S. Perform Q operations of the following 4 types:

// append(W) - Append string W to the end of S.
// delete(k) - Delete the last k characters of S.
// print(k) - Print the (k^th) character of S.
// undo() - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior to that operation.

// operation
// index   S       ops[index]  explanation
// -----   ------  ----------  -----------
// 0       abcde   1 fg        append fg
// 1       abcdefg 3 6         print the 6th letter - f
// 2       abcdefg 2 5         delete the last 5 letters
// 3       ab      4           undo the last operation, index 2
// 4       abcdefg 3 7         print the 7th characgter - g
// 5       abcdefg 4           undo the last operation, index 0
// 6       abcde   3 4         print the 4th character - d

function simpleTextEditor(input) {
    const lines = input.split("\n")
    var str = ""
    var strStack = []
    strStack.push(str)
    const length = parseInt(lines[0])

    for (let i = 1; i <= length; i++) {
        const line = lines[i].trim().split(" ")
        const op = line[0]
        const arg = line[1]

        switch (op) {
            case "1":
                str += arg
                strStack.push(str)
                break;
            case "2":
                str = str.substring(0, str.length - parseInt(arg))
                strStack.push(str)
                break;
            case "3":
                console.log(str.charAt(parseInt(arg) - 1))
                break;
            case "4":
                strStack.pop()
                str = strStack[strStack.length - 1];
                break;
        }
    }
}
export { simpleTextEditor }