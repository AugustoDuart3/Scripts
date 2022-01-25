##To calculate how far it's possible to go into the fibonacci
##sequence by alternating
##two decks of cards(red and blue), using one colour per number,
##and as many cards as fibonacci(number) requires
def fibonacci(n):
	a = 0
	b = 1
	
	# Check is n is less
	# than 0
	if n < 0:
		print("Incorrect input")
		
	# Check is n is equal
	# to 0
	elif n == 0:
		return 0
	
	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b


red=0
blue=0
i=0
while red<=52 and blue<=52:
    i+=1
    if i%2==0: red+=fibonacci(i)
    if i%2!=0: blue+=fibonacci(i)

print(i,fibonacci(i),red,blue-fibonacci(i))
