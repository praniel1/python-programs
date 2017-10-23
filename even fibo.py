import sys
def fibo(n):
    f1 = 0
    f2 = 1
    s = 0
    l = [f1,f2]
    for i in range(2,n):
        s = f1+f2
        l.append(s)
        f1 = f2
        f2=s
        if(l[i]>=n):
            l.pop()
            break
    #print l
    return l

t = int(raw_input())
for a in range(t):
    n = int(raw_input("Enter n : "))
    li = fibo(n)
    s = 0
    for i in range(len(li)):
        if(li[i]%2==0):
            #print li[i]
            s+=li[i]

    print s