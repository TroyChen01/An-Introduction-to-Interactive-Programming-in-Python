allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'ham sanwiches': 3, 'apples': 3},
             'Carol': {'cups': 3, 'apple pies': 1}}
for j in allGuests.values():
	print (j)
for j in allGuests.keys():
	print (j)
for j in allGuests.items():
	print (j)
def totalBrought(guests, item):
	numBrought = 0
	for k, v in guests.items():
		numBrought = numBrought + v.get(item, 0)
	return numBrought

print ('Number of things being brought:')
print ('- Apples ' + str(totalBrought(allGuests, 'apples')))