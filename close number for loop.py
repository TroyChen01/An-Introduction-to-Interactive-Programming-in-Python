def fac(x):
	for n in range (2, x):
		a = 0
		for i in range(1, n):
			if x % i == 0:
				a += i
		b = 0
		for j in range(1,a):
			if a % j == 0:
				b += j
		if n == b:
			print ("{}-{}".format(n, a))

m = int(input())
fac(m)



	

