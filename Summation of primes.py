# import math
#
# def is_prime(num):
#     for i in range(2,int(math.sqrt(num))+1,2):
#         if num%i == 0:
#             return False
#     return True
# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())
#     s=2
#     for i in range(3,n+1):
#         if(is_prime(i)):
#             s+=i
#     print s

import math
t = input()
for i in range(t):
    n = input()
    l = []
    l.extend(range(2,n+1))
    for a in range(len(l)):
        num=l[a]
        if(num<101):
            if(num==2 or num==3 or num==5 or num==7):
                pass
            elif (num%2==0 or num%3==0 or num%5==0 or num%7==0):
                l[a]=0
        elif(num>100):
            sq = int(math.sqrt(num))
            if(num%2==0 or num%3==0 or num%5==0 or num%7==0 or num%11==0):
                l[a]=0
            elif(math.pow(sq,2)== num):
                l[a]=0
    l[:] = (value for value in l if value != 0)
    print sum(l)