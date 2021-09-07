# Question 1
# In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.

# To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers.  
# You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

# So: what's the product of the following two 64-digit numbers?

# 3141592653589793238462643383279502884197169399375105820974944592

# 2718281828459045235360287471352662497757247093699959574966967627

import sys
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(10**6)

# def karastuba(x, y):
#     if x<10 or y <10:
#         return x*y
#     else:
#         n = max(len(str(x)), len(str(y)))
#         half = n/2

#         a = x / 10**(half)
#         b = x % 10**(half)
#         c = y / 10**half
#         d = y % 10**half

#         ac = karastuba(a,c)
#         bd = karastuba(b,d)
#         ad = karastuba(a,d)
#         bc = karastuba(b,c)

#         prod = (10**2*half)*ac + (10**half)*(ad+bc) + bd

#         return prod

def karastuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        nby2 = n / 2
        a = x / 10**(nby2)
        b = x % 10**(nby2)
        c = y / 10**(nby2)
        d = y % 10**(nby2)
        ac = karastuba(a,c)
        bd = karastuba(b,d)
        ad_plus_bc = karastuba(a+b,c+d) - ac - bd
        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        return prod

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(karastuba(x, y))







