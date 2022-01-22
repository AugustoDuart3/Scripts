##fast exponentiation algorithm, from MIT's 6.042J
##a is Real, b is natural
##the invariant is that z is real and y*x**z=a**b

def FastExponentiation(x,z):
    while True:
        if z==0: return 1
        r=z%2
        z=z/2
        if r==1: return x
        x=x*x

a=4
b=2
print(FastExponentiation(a,b))
