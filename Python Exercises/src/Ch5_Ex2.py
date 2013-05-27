'''
Created on May 17, 2013

@author: Kevin

Write a function called 'do_plus' that accepts two parameters /n
and adds them together with the '+' operation.
'''

def do_plus(a,b):
    #Verify that the arguments supplied are type(int)
    if (type(a) == int) and (type(b) == int):
        return a+b
    else:
        raise TypeError, "Arguments must both be integers."
        

#print do_plus("a",3)
#rint do_plus(2,"b")
#rint do_plus("a","b")
#print do_plus("2","3")
print do_plus(2,3)

