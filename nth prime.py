import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def nth(num):
    # l=[2]
    # count = 1
    # i=3
    # flag = 1 #prime
    # while count<=num :
    #     for j in range(2,i):
    #         if i%j == 0:
    #             flag = 2 #not prime
    #     if flag == 1:
    #         l.append(i)
    #         count += 1
    #     i+=1
    # print l
    count=1
    i=3
    while count < num:
        if is_prime(i):
            count += 1
        i += 1
    i-=1
    print i


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    nth(n)