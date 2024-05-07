// # Jesse loves cookies and wants the sweetness of some cookies to be greater than value k. To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

// # sweetness = (1 x Least sweet cookie) + (2 x 2nd least sweet cookie).

// # This occurs until all the cookies have a sweetness >= k.

// # Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return -1.

function cookies(k, A) {
    var sortedList = A.sort()
    var count = 0
    if (sortedList[0] >= k) {
        if (count == 0 || sortedList.length == 1) {
            return -1
        } else {
            return count
        }
    }
    const temp = sortedList[0] + 2 * sortedList[1]
    const newList = [temp]

    for (let i = 2; i < sortedList.length; i++) {
        newList.push(sortedList[i])
        count += 1
    }
    return count
}
export { cookies }