#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    sum=0
    for i in range(1,n):
        if (i%3==0):
            sum+=i
            print i
        elif(i%5==0):
            sum+=i
            print i
    print sum
    sum=0