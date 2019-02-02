try:
	num1 = int (input("Please enter a number:"))
	print (1/num1)
except Exception as err:
    print("please enter a  number over 1!")
    print (err)
else:
	print ("everything is ok")
