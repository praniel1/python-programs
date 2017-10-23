def pr(n):
    n=n-1
    s3 = 3 * ((n/3) * ((n/3)+1)) / 2
    s5= 5*((n/5)*((n/5)+1))/2
    s15 = 15 * ((n/15) * ((n/15) + 1)) / 2
    print s3+s5-s15

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    pr(n)