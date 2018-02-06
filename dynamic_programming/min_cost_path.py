#https://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/

cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]

memo = {}
memo['0-0'] = 1



def minCost(cost, x, y):
    state = str(x) + '-' + str(y)
    if state in memo:
        return memo[state]
    curMinCost=999
    if(x>0 and y>0):
        c = minCost(cost, x-1, y-1) + cost[x][y]
        if c < curMinCost:
            curMinCost = c
    if(x>0): 
        c = minCost(cost, x-1, y) + cost[x][y]
        if c < curMinCost:
            curMinCost = c
    if(y>0):
        c = minCost(cost, x, y-1) + cost[x][y]
        if c < curMinCost:
            curMinCost = c
    memo[state] = curMinCost
    return curMinCost

print(minCost(cost, 2, 2))  
