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
