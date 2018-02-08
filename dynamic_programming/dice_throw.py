memo = {}

def dice_throw(sumleft, diceleft):
    state = "{0}-{1}".format(sumleft, diceleft)
    if state in memo:
        return memo[state]
    if sumleft == 0 and diceleft == 0:
        return 1
    if sumleft < 0 or diceleft == 0:
        return 0
    ways = 0
    for i in range(1,7):
        ways = ways + dice_throw(sumleft-i, diceleft-1)
    memo[state] = ways
    return ways

print(dice_throw(100,20))


