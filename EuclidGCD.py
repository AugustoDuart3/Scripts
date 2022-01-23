##Euclid's algorithm for finding a GreatestCommonDivisor

def GreatestCommonDivisor(a,b):
    rem1=a%b
    remPrev=b%rem1
    rem=rem1%remPrev
    
    while rem!=0:
        remNext=remPrev%rem
        remPrev=rem
        rem=remNext
    return remPrev

print(GreatestCommonDivisor(1147,899)) #31
