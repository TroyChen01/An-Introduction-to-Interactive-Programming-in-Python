#prime number
from math import sqrt
j = 2
while j <=100:
	i = 2
	k = sqrt(j)
	while i <= k:
		if j % i == 0: break
		i = i + 1
	if i > k:
		print (j, end = " ")
	j += 1
# for loop for prime unmber
for a in range (2, 101, 1):
	b = int (sqrt(a))
	flag = 1
	for c in range (2, b+1):
	    if a % c == 0:
	    	flag = 0 
	    	break
	if flag == 1:
		print (a, end = " ")
