# Jesse loves cookies and wants the sweetness of some cookies to be greater than value k. To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

# sweetness = (1 x Least sweet cookie) + (2 x 2nd least sweet cookie).

# This occurs until all the cookies have a sweetness >= k.

# Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return -1.

def  cookies(k, A):
    sortedList = sorted(A)
    count = 0
    if sortedList[0] >= k:
        if count == 0 or len(sortedList) == 1:
            return -1
        else:
            return count
        
    temp = sortedList[0] + 2 * sortedList[1]
    newList = [temp]

    for i in range(2, len(sortedList)):
        newList.append(sortedList[i])
        count+=1
    return count