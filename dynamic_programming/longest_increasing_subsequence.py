#bottom-up
def lis(arr):
    n = len(arr)
    memo = [1 for i in range(0,n)]

    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j] and memo[i]<memo[j]+1:
                memo[i]=memo[j]+1
    max=0
    for i in range(n):
        if memo[i]>max:
            max=memo[i]
    
    return max

print(lis([1,0,3]))
print(lis([1,2,3]))
print(lis([1,1,1]))