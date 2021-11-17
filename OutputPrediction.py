#A solution to a problem that goes
#input=[1 2 3]
#output=[5 10 55]. What would be the output of input=10?
#my solution(not the only one) assumes the pattern to be a sequence

OnMinusOne=5
On=10

for i in range(2,10):
    OnPlusOne=OnMinusOne*(On+1)
    OnMinusOne=On
    On=OnPlusOne

print(OnPlusOne)
#45249625789158536446143123130829333347152074792960
