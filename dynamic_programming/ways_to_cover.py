#this is a generalized solution to the problem outlined in
#https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/


memo={}
def ways(totdist, curdist, stepsizes):
    state = ''
    state+=str(totdist)
    state+='-'
    state+=str(curdist)
    if state in memo:
        return memo[state]
    wayscount=0
    for i in stepsizes:
        if curdist + i == totdist:
            wayscount = wayscount + 1
        elif curdist + i < totdist:
            wayscount = wayscount + ways(totdist, curdist + i, stepsizes)
    memo[state]=wayscount
    return wayscount

print(ways(10, 0, [1,2,3]))
    