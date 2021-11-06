#python 3.7
import math
def SmartPermutation(n,r):
    #simplifies factorials in the permutations formula nPr
    numerator=n
    for i in range(n-r+1,n):
        numerator=numerator*i
    return numerator

def SmartCombination(n,r):
    #simplifies factorials in the combinations formula nCr
    numerator=n
    if 2*r>=n:
        #simplifies r!
        for i in range(r+1,n):
            numerator=numerator*i
        return (numerator/math.factorial(n-r))
    if 2*r<n:
        #simplifies (n-r)!
        for i in range(n-r+1,n):
          numerator=numerator*i
        return (numerator/math.factorial(r))
