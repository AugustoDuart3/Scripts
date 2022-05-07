##Euclid's algorithm for finding a GreatestCommonDivisor

##recursively
def GreatestCommonDivisorRecursive(a,b):
    #base
    if(b==0): return a
    if(a==0 or a==b): return b
    #recursive, use the place of the biggest one for the remainder
    if(b>a): return GreatestCommonDivisorRecursive(a,b%a)
    if(a>b): return GreatestCommonDivisorRecursive(a%b,b)

    
def GreatestCommonDivisor(a,b):
    #unfinised
    #edge cases: both zeroes, only one 0
    if(a==b): return b
    if(a<b):
        GreaterValue=b
        LesserValue=a
    if(a>b):
        GreaterValue=a
        LesserValue=b
    while(LesserValue>0):
        Stored=LesserValue #store it for a line
        LesserValue=GreaterValue%LesserValue
        GreaterValue=Stored
    return GreaterValue
