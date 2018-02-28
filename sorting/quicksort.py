def quicksort(ar):
    quicksortrecur(ar, 0, len(x)-1)

def quicksortrecur(ar, start, end):
    if(start<end):
        pivot = getpivotpoint(ar, start, end)
        quicksortrecur(ar, start, pivot-1)
        quicksortrecur(ar, pivot+1, end)

def getpivotpoint(ar, start, end):
    pivotvalue = ar[start]
    leftpointer = start+1
    rightpointer = end
    done = False
    while not done:
        while ar[leftpointer]<=pivotvalue and leftpointer<=rightpointer:
            leftpointer = leftpointer + 1
        while ar[rightpointer]>=pivotvalue and rightpointer>=leftpointer:
            rightpointer = rightpointer - 1
        if(rightpointer<leftpointer):
            done = True
        else:
            temp = ar[leftpointer]
            ar[leftpointer] = ar[rightpointer]
            ar[rightpointer] = temp
    ar[start] = ar[leftpointer]
    ar[leftpointer] = pivotvalue
    return leftpointer


x = [3,2,1,7]
quicksort(x)
print(x)