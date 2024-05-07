# // Implement a simple text editor. The editor initially contains an empty string, S. Perform Q operations of the following 4 types:

# // append(W) - Append string W to the end of S.
# // delete(k) - Delete the last k characters of S.
# // print(k) - Print the (k^th) character of S.
# // undo() - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior to that operation.

# // operation
# // index   S       ops[index]  explanation
# // -----   ------  ----------  -----------
# // 0       abcde   1 fg        append fg
# // 1       abcdefg 3 6         print the 6th letter - f
# // 2       abcdefg 2 5         delete the last 5 letters
# // 3       ab      4           undo the last operation, index 2
# // 4       abcdefg 3 7         print the 7th characgter - g
# // 5       abcdefg 4           undo the last operation, index 0
# // 6       abcde   3 4         print the 4th character - d

def simpleTextEditor(input):
    # split by new line
    lines = list(input.split("\n"))
    # Start string
    s = ""
    # prep stack
    stack = []
    # start stack with init'd string
    stack.append(s)

    # stating after the first number until we run out
    for i in range(1, len(lines)):

        # strip the whitespace
        lines[i] = lines[i].strip()
        # split by the space between them
        line = lines[i].split(" ")
        # get the command
        if line[0] == "1":
            stack.append(s)
            s += line[1]

        elif line[0] == "2":
            stack.append(s)
            s = s[0: -int(line[1])]

        elif line[0] == "3":
            print(s[int(line[1]) - 1])

        elif line[0] == "4":
            s = stack.pop()