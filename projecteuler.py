#Problem 1
def sum_multof3and5(n):
	z = 0
	for x in range(1,n):
		if x % 3 == 0 and x % 5 != 0:
			z = z + x
	for y in range(1,n):
		if y % 5 == 0:
			z = z + y
	print z
sum_multof3and5(1000)
#Problem1 -- Alternative Solution
def sum_multof3and5_alternative(n):
	print sum(x for x in xrange(n) if not (x % 3 and x % 5)) 
#As long as x is not divisble by both 3 and 5, but still divisible 
#by either 3 or 5, take it and add all existing values of x
#It's interesting how this is observed with De Morgan's law: ~(P ^ Q) is the same as ~P v ~Q
sum_multof3and5_alternative(1000)
#Problem 2
def sum_of_even_fibonacci_numbers():
	x = 1
	y = 2
	z = x + y
	a = []
	a.append(y)
	while z < 4000000:
		x = z + y
		y = x + z
		z = x + y
		if x % 2 == 0:
			a.append(x)
		if y % 2 == 0:
			a.append(y)
		if z % 2 == 0:
			a.append(z)
	print sum(a)
sum_of_even_fibonacci_numbers()
