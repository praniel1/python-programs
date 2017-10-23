#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    s1=0
    s2=0
    s3=0
    s1=(n*(n+1))/2
    s1*=s1
    s2=(n*(n+1)*(2*n+1))/6
    s3=s1-s2
    print s3