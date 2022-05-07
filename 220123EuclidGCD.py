##Euclid's algorithm for finding a GreatestCommonDivisor

##recursively
def GreatestCommonDivisorRecursive(a,b):
    #base
    if(b==0): return a
    if(a==0): return b
    if(a==b): return b
    #recursive, use the place of the biggest one for the remainder
    if(b>a): return GreatestCommonDivisorRecursive(a,b%a)
    if(a>b): return GreatestCommonDivisorRecursive(a%b,b)
