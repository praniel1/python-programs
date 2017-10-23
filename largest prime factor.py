import sys
def prime(n):
    l = []
    for i in range(2,n+1):
        flag = 1
        for j in range(2,i):
            if (i%j==0):
                flag = 2
        if (flag==1):
            l.append(i)
    return l

def factors(pr,n):
    l = []
    for i in range(0,len(pr)):
        if(n % pr[i]==0):
            l.append(pr[i])
    return l

t = int(raw_input().strip())
for a in xrange(t):
    n = long(raw_input().strip())
    prime1 = prime(n)
    factor = factors(prime1, n)
    print factor[len(factor) - 1]