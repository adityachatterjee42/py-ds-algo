def mergesort(x):
    if(len(x)>1):
        l=x[:len(x)//2]
        r=x[len(x)//2:]
        mergesort(l)
        mergesort(r)
        i=0
        j=0
        k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                x[k]=l[i]
                i=i+1
            else:
                x[k]=r[j]
                j=j+1
            k=k+1
        while i<len(l):
            x[k]=l[i]
            i=i+1
            k=k+1
        while j<len(r):
            x[k]=r[j]
            j=j+1
            k=k+1
x=[4,8,1,9,3,6]
mergesort(x)
print(x)


        