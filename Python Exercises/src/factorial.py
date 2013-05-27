'''
Created on May 23, 2013

@author: Kevin
'''

def factorial(n):
    fac_this = range(1,(n+1))
    result = reduce(lambda first, second: first * second, fac_this)
    print "The factorial of %d is %d." % (n, result)
    
factorial(4)
factorial(5)
factorial(6)
factorial(7)
factorial(8)

def factorial_2(n):
    facs = range(1,(n+1))
    for i in facs:
        print i, facs[i]
        
factorial_2(4)