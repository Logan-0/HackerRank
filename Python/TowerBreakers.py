#Two players are playing a game of Tower Breakers!
#Player  always moves first, and both players always play optimally.The rules of the game are as follows:

#Initially there are 'n' towers.
#Each tower is of 'm' height.
#The players move in alternating turns.
#In each turn, a player can choose a tower of height and reduce its height to, where and evenly divides .
#If the current player is unable to make a move, they lose the game.
#Given the values of and, determine which player will win. If the first player wins, return 1. Otherwise, return 2.

def towerBreakers(n, m):
    # if we start with either a 1 height or the number of towers divided by 2 has a 0 remainder.
    # if we start with one height the first player cant move and 2 winds
    # if we start with a tower number divisible by two
    # the second player can remove a tower to 1 height each turn removing a tower. hence removing a possible turn.
    # easy win for player 2.
    if (m==1 or n%2==0):
        return 2
    else:
        return 1