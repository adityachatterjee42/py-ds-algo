values = {}
values[1] = 1
values[2] = 5
values[3] = 8 
values[4] = 9
values[5] = 10
values[6] = 17
values[7] = 17
values[8] = 20    
    
maxvals = {}    

def rodCut(len):
    if len in maxvals:
        return maxvals[len]
    maxval = 0
    if len in values:
        maxval = values[len]
    for i in range(1, int(len/2)):
        val1 = rodCut(i)
        val2 = rodCut(len-i)
        if val1 + val2 > maxval:
            maxval = val1 + val2
    maxvals[len] = maxval
    return maxval 

print(rodCut(8))