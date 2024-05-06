# // In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:

# // 1 x: Enqueue element x into the end of the queue.
# // 2: Dequeue the element at the front of the queue.
# // 3: Print the element at the front of the queue.

def processData(input):
    # Setup Length
    lines=[]
    length = int(input[0])
    inputs = input[1:]
    # for eachsplit and decide
    for i in range(length-1):

        swCase = inputs[i].split(" ")

        if (swCase[0] == '1'):
            lines.append(swCase[1])
        if (swCase[0] == '2'):
            lines.pop()
        if (swCase[0] == '3'):
            print(lines[0])