// In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:

// 1 x: Enqueue element x into the end of the queue.
// 2: Dequeue the element at the front of the queue.
// 3: Print the element at the front of the queue.

function processData(input) {

    const lines = []
    for(let j = 0; j < input.length; j++) {
        lines.push(input[j])
    }

    const stack = []
    for (let i = 1; i < lines.length; i++) {
        const swCase = lines[i].split(" ")
        switch (swCase[0]) {
            case "1":
                stack.push(swCase[1])
                break;
            case "2":
                stack.shift()
                break;
            case "3":
                console.log(stack[0])
                break;
            default:
                break;
        }
    }
}
export { processData }